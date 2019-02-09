# EECS598 Assignment 1: A Tour of Apache Spark

Gain a hands-on understanding of Apache Spark, Spark SQL, and Spark Streaming over HDFS and Alluxio.

Due: __Feb 20, 2019, 11:59 PM__

## Overview

First introduced in [2010](https://www.usenix.org/legacy/event/hotcloud10/tech/full_papers/Zaharia.pdf), Apache Spark remains one of the most popular modern cluster computing frameworks.
By leveraging its innovative distributed memory abstraction -- Resilient Distributed Datasets (RDDs) -- Apache Spark provides an effective solution to the I/O inefficiency of MapReduce, while retaining its scalability and fault tolerance.

In this assignment, you are going to deploy Spark and HDFS, write a Spark program generating a web graph from the entire Wikipedia, and write a PageRank program to analyze the web graph.

You will run those applications using Spark over HDFS in a distributed cluster and understand the benefits of in-memory caching using Alluxio.

Finally, you will write a stream emitter using Spark Streaming and a parser using Spark Structured Streaming to play with the recent trend of working with streaming data.

As a well-maintained open-source framework, Apache Spark has well-written official documents; you will find a lot of useful information by simply reading the official tutorials and documents.
When you encounter an issue regarding on cluster deployment or write Spark programs, you are encouraged to utilize online resources before posting questions on Piazza.

## Learning Outcomes

After completing this programming assignment, students should be able to:

* Deploy and configure Apache Spark, HDFS, and Alluxio in a real cluster.
* Write Spark applications using Scala/Java/Python and launch them in the cluster.
* Describe how Apache Spark, Spark SQL, Spark Streaming, HDFS, and Alluxio work, and interact with each other.

## Environment Setup

You will complete your assignment in CloudLab.
You should complete [Assignment 0](/Assignments/Assignment0/README.md) first to learn how to register a CloudLab account and start a new experiment.

In this assignment, we provide you a CloudLab profile called `topology-assignment1` under the `Michigan-BigData` project for you to start your experiment. Please select `Cloudlab Utah` as the cluster when instantiating the profile.
The profile is a simple 3-node cluster (`node-0, node-1, node-2`) with Ubuntu 16.04 pre-installed. The `fsnode` is used only to provide you data. You can safely ignore it and its links between other nodes. In the rest of this assignment, when refering to nodes in the cluster, we mean `node-{0,1,2}`.

You will have full control of those machines once the experiment is started, so feel free to download any missing packages you need in the assignment.

All required resources and files are located under `/bigdata`.
Inside it we provide JDK 1.8 for you so you do not have to install it by yourself.

### Setup software

You need to first set up the correct `JAVA_HOME` and add it to the shell search `PATH`. For each node in the cluster, log in and execute the following commands in the terminal:

```bash
echo "export JAVA_HOME=/bigdata/jdk1.8.0_201
export PATH=\${JAVA_HOME}/bin:\$PATH" >> ~/.bashrc
source !$
```

### Setup Programming Language

You choose either Java or Scala to finish this assignment. You will need to install the corresponding build tool.

#### Scala

Another thing you may soon find useful is the Simple Build Tool (sbt), run the following command to install it:

```bash
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt
```

#### Java

You can use Maven to to build your java application as an uber jar. We provide an example project located at `/bigdata/examples/a1-java` which you can use as an start point.

To install maven, run the following command:

```bash
tar xvf /bigdata/software/apache-maven-3.6.0-bin.tar.gz -C $HOME
echo "export PATH=$HOME/apache-maven-3.6.0/bin:\$PATH" >> $HOME/.bashrc
source !$
```

### Configure SSH

Another important step here is to enable the SSH service among the nodes in the cluster.
A simple way to do this is to enable agent forwarding when you ssh from your local machine. Edit `~/.ssh/config` on your **local** machine (i.e. your laptop), add the following section

```plain
Host node-*
    StrictHostKeyChecking no
    ForwardAgent yes
```

Then ssh keys available on your local machine will also be available on remote nodes.

Note: Do **NOT** enable ssh agent forwarding on hosts you don't trust. This will expose your private key to the remote host, which can then be accessed by any other users on the host.

The previous documented method of modifying `~/.ssh/authorized_keys` will not work in cloudlab environment, as the file will be refreshed periodically, and any edit will be lost.

If you setup the keys correctly, you should be able to ssh from one node to another, as well as ssh into itself:

```bash
# from node-0
ssh localhost
exit
ssh node-1
exit
ssh node-2
exit
# from node-1
ssh localhost
exit
ssh node-0
exit
ssh node-2
exit
# from node-2
ssh localhost
exit
ssh node-0
exit
ssh node-1
exit
```

Remember to type `exit` to exit from the ssh login before doing another ssh command.

### The address of a node

The nodes in the experiment are configured to use unqualified names to connect to each other. You should be able to access other nodes using simply
`node-0`, `node-1` and `node-2`. These are the addresses you should use in any configuration files you need to modify.

There is also a public address associated with each node, i.e.,the last part of the ssh command you used to log into that node. If the command is

```bash
ssh -p 22 peifeng@hp174.utah.cloudlab.us
```

then the address is `hp174.utah.cloudlab.us`.

This public address should be used if you want to access the node from outside of the experiment, for example, your laptop. So if you want to access the web UI of any application from your laptop's browser, you should use the qualified address.

**Note: Never use public address in any of the configuration files, it will cause your experiment be terminated immediately.**

### Extend disk

The original disk capacity CloudLab provides you is small. To be able to use HDFS to handle big files, we need to first mount to a larger disk partition. To do this, execute the following comands to your console:

```bash
sudo mkdir /new_disk
sudo /usr/local/etc/emulab/mkextrafs.pl /new_disk
```

Use

```bash
df -h
```

to check if it is successfully mounted. You should see a new entry about `/new_disk` with much larger spack available.

The newly mounted disk has permission issue which prevents you from deploying HDFS. To fix that, do the following:

```bash
sudo chown $(id -u -n):$(id -g -n) -R /new_disk
```

## Part 0: Deploy Spark, HDFS, and Alluxio

### [Apache Spark](https://spark.apache.org/docs/latest/index.html)

Apache Spark works on top of distributed file systems to perform parallel computations within the cluster.
The following diagram illustrates how a simple Spark cluster works.

![cluster-overview](./cluster-overview.png)

The Spark Context (now contained in the **Spark Session**) created by the master node talks to a cluster manager which allocates resources across the application.
The executors on the worker nodes carry out the computation tasks and store data in a distributed way.
Across the assignment, you will deploy Spark in the **Standalone** mode, meaning Spark will run using its own standalone cluster manager, and no other resource managers (such as Apache YARN or Apache Mesos) are needed. For more information on Spark cluster overview, click [here](https://spark.apache.org/docs/latest/cluster-overview.html).

The Spark cluster you will deploy in this assignment looks exactly like the cluster in the above diagram.
Pick your favorite node among the three to be the master node and launch your applications there.

#### Install spark on each node

To install spark, decompress the spark binary on each node in the cluster:

```bash
tar xvf /bigdata/software/spark-2.2.3-bin-hadoop2.7.tgz -C $HOME
```

Instructions on building a spark cluster can be found in Spark's [official document](http://spark.apache.org/docs/2.2.3/spark-standalone.html).

#### Configurate Spark

By default, Spark can automatically discover some network settings. However, to ensure Spark do not use public addresses, we need to configure it.

We will use `node-0` as the Spark Master, and `node-1`, `node-2` as Spark Worker. The following config files should be edited on all three nodes.

##### `spark-2.2.3-bin-hadoop2.7/conf/slaves`

This file tells Spark where its workers are. First copy this file from its template

```bash
cp spark-2.2.3-bin-hadoop2.7/conf/slaves{.template,}
```

Edit it to include only 2 lines

```plain
node-1
node-2
```

##### `spark-2.2.3-bin-hadoop2.7/conf/spark-env.sh`

This file tells Spark which address it should bind to for master. Start by copying from template

```bash
cp spark-2.2.3-bin-hadoop2.7/conf/spark-env.sh{.template,}
```

Add a line containing

```plain
SPARK_MASTER_HOST=node-0
```

#### Start Spark

On the master node (`node-0`), do

```bash
spark-2.2.3-bin-hadoop2.7/sbin/start-all.sh
```

This will start master as well as workers on corresponding nodes.

You can go to `<master_node_public_address>:8080` to check the status of the Spark cluster.

#### Verify

After a while, you should be able to see two workers in the master's WebUI. Make sure their status is `ALIVE`.

To stop all spark related process on the current node, do

```bash
spark-2.2.3-bin-hadoop2.7/sbin/stop-all.sh
```

### [Apache Hadoop](http://hadoop.apache.org/)

Apache Spark typically needs an underlying distributed file system to store its input data.
Apache Hadoop is an open-source framework that provides simple programming models distributed for processing of large data sets.
It mainly consists of the Hadoop Distribited File System (HDFS) and Hadoop YARN.
Since we use Spark's standalone manager in this assignment, we will only deploy HDFS.

First, let us get the latest stable version of Hadoop on every machine in the cluster.

```bash
tar xvf /bigdata/software/hadoop-2.7.7.tar.gz -C $HOME
echo "export PATH=$(pwd)/hadoop-2.7.7/bin:\$PATH" >> ~/.bashrc
source !$
```

You can find the deployment instructions at this [link](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html).
To make your life easier, we have provided the instructions for you.

#### Configure Hadoop

There are two type of nodes in HDFS -- the name node and data nodes.
Think of the name node as the master node, which is in control of the file system.
The data nodes, on the other hand, actually store the data. These two types of nodes are independent to each other, meaning, they can co-exist on the same physical machine.

In our case, we will use one machine as both name node and data node, and the other two machines as data nodes.

There are a few configuration files you need to edit. They are originally empty so users have to manually set them. Also remember to do the same editing on all three nodes.

##### `hadoop-2.7.7/etc/hadoop/core-site.xml`

Add the following contents in the `<property>` field in `hadoop-2.7.7/etc/hadoop/core-site.xml`, replacing `namenode_IP` with your master node's address (**NOT** the public address, but something like `node-{1,2,3}`):

```xml
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://namenode_IP:8020</value>
    </property>
</configuration>
```

##### `hadoop-2.7.7/etc/hadoop/hdfs-site.xml`

Also you need to add the following in `hadoop-2.7.7/etc/hadoop/hdfs-site.xml`. This configures the path under which Hadoop actually stores data. Make sure this is some directory under `/new_disk`, which we already created with plenty of space.

```xml
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/path/to/namenode/dir/</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/path/to/datanode/dir</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/path/to/hadoop/tmp</value>
    </property>
</configuration>
```

Of course, you need to make sure the directory paths you specify do exist.

On the master node, which we will start both a namenode daemon and a datanode daemon, you will need to create all three of these directories.

On other two machines, only the datanode directory is needed to be created.

##### `hadoop-2.7.7/etc/hadoop/slaves`

We also need to edit `hadoop-2.7.7/etc/hadoop/slaves` to add the address of all the datanodes. Since `localhost` already exists, we need to add the addresses for the other two nodes in the cluster, so every node can store data. **This only need to be done on the name node.**

##### `hadoop-2.7.7/etc/hadoop/hadoop-env.sh`

Lastly, even though we have set `JAVA_HOME` in our environment, to make sure the start-dfs script picking up the value, we set it again in `hadoop-env.sh`. Fine the line of

```plain
export JAVA_HOME=${JAVA_HOME}
```

and change it to

```plain
export JAVA_HOME=/bigdata/jdk1.8.0_201
```

#### Initialize and start

Now, we proceed to format the name node and start the daemon on the name node of your choice.

```bash
hdfs namenode -format
hadoop-2.7.7/sbin/start-dfs.sh
```

The command should start the namenode daemon as well as all the datanode daemons on the data nodes.

To check the HDFS status, go to:

```bash
<namenode_IP>:50070/dfshealth.html
```

make sure there are 3 datanodes.

Now, the HDFS is setup. Type the following to see the available commands in HDFS.

```bash
hdfs dfs -help
```

### [Alluxio](https://www.alluxio.com/)

Alluxio is a memory-speed virtual distributed storage system that bridges applications and underlying storage systems.
It provides much faster unified data access and can be used to improve the performance and consistency of distributed file systems such as HDFS.
In this assignment, we will see how much performance improvement Alluxio can bring over HDFS by acting as a caching layer.

To deploy Alluxio, use the binary file located under `/bigdata` and decompress it:

```bash
tar xvf /bigdata/software/alluxio-1.5.0-hadoop-2.7-bin.tar.gz -C $HOME
```

To make sure Spark be aware of your Alluxio setup, add the following two lines to your `spark-default.conf` under you Spark/conf directory (this need to be done on all three nodes). Make sure you specify the correct path:

```bash
cp spark-2.2.3-bin-hadoop2.7/conf/spark-defaults.conf.template spark-2.2.3-bin-hadoop2.7/conf/spark-defaults.conf
echo "spark.driver.extraClassPath /path/to/alluxio/client/spark/alluxio-1.5.0-spark-client.jar" >> !$
echo "spark.executor.extraClassPath /path/to/alluxio/client/spark/alluxio-1.5.0-spark-client.jar" >> !$
```

#### Configuration

Edit two files on all three nodes.

##### `alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties`

You need to edit `alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties`.

First copy it from the template

```bash
cp alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties.template alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties
```

Now uncomment `alluxio.master.hostname` inside the file, update the value to the address of the machine you plan to run Alluxio Master on.

##### `alluxio-1.5.0-hadoop-2.7/conf/workers`

This file specifies all works of Alluxio. In our experiment, similar to the hadoop setup, we will have a node acting as both Alluxio master and worker, while the other two nodes acting as worker.

Therefore, replace the file content with the address of all three nodes in the cluster. Remember to remove the `localhost` line.

#### Format and start

Now you can format and start the Alluxio master on master node.

```bash
alluxio-1.5.0-hadoop-2.7/bin/alluxio format
alluxio-1.5.0-hadoop-2.7/bin/alluxio-start.sh master
```

On all three nodes, do the following to start Alluxio slave:

```bash
alluxio-1.5.0-hadoop-2.7/bin/alluxio-start.sh worker
```

To check the status of Alluxio, go to:

`http://<alluxio_master_hostname>:19999`

## Part 1: Spark and Spark SQL

In this part of the assignment, you will perform 3 tasks

* Ingesting a Wikipedia database into HDFS
* Parsing the Wikipedia database to generate a webgraph of the internal links
* Use the generated graph as an input to a Spark PageRank program to generate the ranks of the internal links.

### Task 1: Ingest Data into HDFS

In this task, we provide you a big Wikipedia database in xml format. It can be found at `/bigdata/assignments/assignment1/enwiki-20110115-pages-articles_whole.xml`.

This input file is very big and you have to use a distributed file system like HDFS to handle it. The file is also divided into 11 smaller files named `enwiki-20110115-pages-articles{1-15}.xml` in the same directory for debugging purposes.

The xml file is structured as follow:

```xml
<mediawiki>
    <siteinfo>
        ...
    </siteinfo>
    <page>
        <title>Title A</title>
        <revision>
            <text>Some text</text>
        </revision>
    </page>
    <page>
        ...
    </page>
    ...
</mediawiki>
```

To get a sense of how a Wiki page transfers to a xml file, take a look at the following examples:

* [Apple (orig)](https://en.wikipedia.org/wiki/Apple)
* [Apple (xml)](https://en.wikipedia.org/wiki/Special:Export/Apple)

Note that the database we provide you is not up-to-date, but they should be pretty close to what you will find in the above examples.

**Question 1.** What is the default block size on HDFS? What is the default replication factor?

### Task 2: Webgraph on Internal Links

You are going to write a Spark program which takes the xml file you just ingested as input (`enwiki-20110115-pages-articles_whole.xml`), and generate a csv file which describes the webgraph of the internal links in Wikipedia. The csv file should look like the following:

```csv
article1	article0
article1	article2
article1	article3
article2	article3
article2	article0
...
```

It is hard and tedious to find every internal link on a page. We have made the following asumptions to simplify the string parsing for you. For each page element, the article on the left column corresponds to the string between `<title>` and `</title>`, while the article on the right column are those surrounded by a pair of double brackets `[[ ]]` in the `<text>` field in the xml file with the following requirements:

1. All the letters should be convert to lower case.
2. If the internal link contains a `:`, you should ignore the entire link unless it starts with `Category:`.
3. Ignore links that contain a `#`.
4. If multiple links appear in the brackets, take the first one; e.g., take `A` in `[[A|B]]`.

Those assumptions help you filter out some unnecessary links. Note if the remaining string becomes empty after the filtering, you should also ignore them. When we say ignoring a link, we mean it will not show up in the output file of this task.

The two columns in the output file should be by separated by a `Tab`. You may assume there is no other `Tab`s in the article name.

To get started, you can use the [spark-xml package](https://github.com/databricks/spark-xml) to first read the input xml file into a [DataFrame](http://spark.apache.org/docs/2.2.3/sql-programming-guide.html#datasets-and-dataframes), and go from there.

Note: if you use the Java API, the format should be `com.databricks.xml` rather than `xml` in the spark-xml example on their home page.

You will need to figure out how to compile your program and submit as a Spark application and answer the following questions.

**You should use the default configuration of Spark, HDFS, and Alluxio unless we specify a different one.** To be clear, you should use the default deploy mode, which is "client". For more information on the two deploy modes Spark supports and when to use them, read the [official document](https://spark.apache.org/docs/latest/submitting-applications.html).

Set the Spark driver memory to 1GB and the Spark executor memory to 5GB to answer Question 2-4.

**Question 2.**  Use `enwiki-20110115-pages-articles1.xml` as input and run the program locally on the master node using 4 cores. What is the completion time of the task?

**Question 3.** Use `enwiki-20110115-pages-articles1.xml` as input and run the program under HDFS inside the Spark cluster you deploy. Is the performance getting better or worse in terms of completion time? Briefly explain.

**Question 4.** Only for this question, change the default block size in HDFS to be 64MB and repeat Question 3. Is the performance getting better or worse in terms of completion time? Briefly explain.

Set the Spark driver memory to 5GB and the Spark executor memory to 5GB to answer Question 5-6. Use this configuration across the entire assignment whenever you generate a web graph from `enwiki-20110115-pages-articles_whole.xml`.

**Question 5.** Use `enwiki-20110115-pages-articles_whole.xml` as input and run the program under HDFS inside the Spark cluster you deploy. Record the completion time. Now, kill the Spark process in one of the worker nodes (use command `jps` to find out the worker process ID) . Rerun the job and record the completion time. Does the job still finish? Do you observe any difference in the completion time? Briefly explain your observations.

**Question 6.** Only for this question, change the replication factor of `enwiki-20110115-pages-articles_whole.xml` to 2 and repeat Question 5 without killing one of the worker nodes. Do you observe any difference in the completion time? Briefly explain.

### Task 3: Spark PageRank

In this task, you are going to implement the PageRank algorithm, which Google uses to rank the website in the Google Search. We will use it to calculate the rank of the articles in Wikipedia. The algorithm can be summarized as follows:

1. Each article has an initial rank of 1.
2. On each iteration, the contribution of an article is calculated as `its rank / # of neighbors`.
3. Update the rank of the article to be `0.15 + 0.85 * contribution`
4. Go to the next iteration.

The output should be a `txt` file containing two columns.
The first column is the article and the other column describes its rank.

Set the Spark driver memory to 5GB and the Spark executor memory to 5GB whenever you run your PageRank program. Write a script to first run Task 2, and then run Task 3 using the csv output generated by Task 2, and answer the following questions. Always use 10 iterations for the PageRank program.

**Question 7.** First run Task 2 and Task 3 using HDFS without Alluxio. What is the completion time of the entire task? When running Task 2, use `enwiki-20110115-pages-articles_whole.xml` as input.

**Question 8.** Repeat using Alluxio (i.e., write the output of Task 1 to Alluxio and use that as input). How does the performance change? Briefly explain.

**Question 9.** Re-ingest `enwiki-20110115-pages-articles_whole.xml` with block size 64MB. Repeat Question 5 without killing one of the worker nodes. Report how much performance in terms of completion time changes. Briefly explain.

## Part 2: Spark Streaming

In the second part of the assignment, you will learn Spark Streaming as well as Spark Structured Streaming, and write a program for each of them.

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.

![streaming-arch](./streaming-arch.png)

Internally, Spark Streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches. More information about Spark Streaming can be found [here](https://spark.apache.org/docs/latest/streaming-programming-guide.html).

![streaming-flow](./streaming-flow.png)

Spark Structured Streaming is a new high-level API introduced after Apache Spark 2.0 to support continuous applications. It provides fast, scalable, fault-tolerant, and end-to-end exactly-once stream processing without the user having to reason about streaming. The key idea here is to treat a live data stream as a table that is being continuously appended. You are encouraged to read its [programming guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html).

![structured-streaming](./structured-streaming.png)

### Task 1: Stream Receiver

In this task, you are going to write a stream receiver using **Spark Structured Streaming** to read file source while the file is being generated. The input source should be `txt` files. Your receiver should keep a list of articles whose rank is greater than **0.5** and store the file inside the HDFS. The list should be updated dynamically while the Pagerank program is dumping the output and should be saved inside the HDFS.

The output file should be `csv` whose the format should look like the following. Separate the columns with a `Tab`.

```
article0	rank0
article1	rank1
article2	rank2
...
```

**Question 10** Start a PageRank program you wrote in Part 1 Task 2 whose input is the link graph generated from "enwiki-20110115-pages-articles_whole.xml" and store the output to a directory inside HDFS. Set your stream receiver to read the files generated by the PageRank program. Kill the receiver when the PageRank task is finished. How many articles in the database has a rank greater than **0.5**? You can start with 'hdfs dfs -mv' or 'mv' to help you write your program.

### Task 2: Stream Emitter

In this task, you are going to write a stream emitter using **Spark Streaming** to emit the 'txt' file output generated by the PageRank program to a directory to emulate the case you see in the previous task. Run your stream receiver to catch the stream you are emitting and check if you get the same result as in Question 10. You may configure `spark.cores.max` to run multiple Spark jobs in parallel.

**Question 11** Spark Streaming can also be used to send data via TCP sockets. The Emitter in this case will wait on a socket connection request from the receiver, and upon accepting the connection request it will start sending data. Do you think such data server design is feasible and efficient? Briefly explain.

**Questions 12 (Bonus Question)** How many hours did you spend in this assignment?

## Submission Instructions

### File name

Each group should submit one tar.gz file to `eecs598-bigdata-staff@umich.edu`.

Name the file as `<group_num>_assignment1.tar.gz`.
For example, `g1_mosharaf_peifeng_assignment1.tar.gz`. You can find your group name/number at this [link](https://www.cloudlab.us/show-project.php?project=Michigan-BigData#groups).

### Content - Code

4 Spark projects from Part 1 Task 2-3 and Part 2 Task 1-2 should goes under folder names
`p1t2`, `p1t3`, `p2t1`, `p2t2` accordingly.

Inside each folder, in addition to source code and build system, there should be an additional folder named `config` which contains Spark configuration files you need to run the three tasks mentioned below.

The structure should be something like (using Java as example)

```plain
g1.tar.gz
├── p1t2
│   ├── config
│   ├── pom.xml
│   └── src
├── p1t3
├── p2t1
├── p2t2
└── README (see below)
```

### Content - README

Each submission should also include a README to record the answers to the 12 questions mentioned in this assignment.

You also need to provide instructions (such as commands or scripts) to run the **following 3 tasks on Spark master node locally using 4 cores:**

1. Use the program in Part 1 Task 2 to take "enwiki-20110115-pages-articles1.xml" as input to generate the graph.
2. Use the program in Part 1 Task 3 to take the graph you just generated and output a rank list of the articles in the dataset.
3. Use the stream emitter you wrote in Part 2 Task 2 to emit the rank list output in the previous step to a local directory while using the stream emitter you wrote in Part 2 Task 1 to dynamically read the files and generate the output mentioned in Part 2 Task 1.

Try to be clear about the instructions to run these steps. The purpose of doing this is to check if your program does what we mention in the spec. Do not worry whether your program has the lowest completion time.

## Acknowledgements

This assignment uses insights from Aditya Akella's Assignment 2 from WISC CS 838: Big Data Systems course.
