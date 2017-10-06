# EECS598 Assignment1: A Tour of Apache Spark

### *Gain a hands-on understanding of Apache Spark, Spark SQL, and Spark Streaming over HDFS and Alluxio.*
##

### Due: Oct 11, 2017, 11:59 PM

## Overview
First introduced in [2010](https://www.usenix.org/legacy/event/hotcloud10/tech/full_papers/Zaharia.pdf), Apache Spark remains one of the most popular modern cluster computing frameworks. 
By leveraging its innovative distributed memory abstraction -- Resilient Distributed Datasets (RDDs) -- Apache Spark provides an effective solution to the I/O inefficiency of MapReduce, while retaining its scalability and fault tolerance. 
In this assignment, you are going to deploy Spark and HDFS, write a Spark program which creates a web graph from the entire Wikipedia, and write a PageRank program to analyze the web graph. 
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
You should complete [Assignment 0](/Assignments/Assignment0/README.md) to learn how to register a CloudLab account and start a new experiment if you have not done so already. 
In this assignment, we provide you a CloudLab profile called "spark-cluster" under "Michigan-BigData" project for you to start your experiment. 
The profile is a simple 3-node cluster with Ubuntu 14.04 installed on each machine. 
You get full control of the machines once the experiment is created, so feel free to download any missing packages you need in the assignment.

In the project group directory, we provide JDK 1.8 for you so you do not have to install it by yourself. **To emphasize again, you are not allowed to modify, remove, or add anything from/to the group directory (/proj/michigan-bigdata-PG0), which is shared by every member in the Michigan-BigData project.** 
To set the correct JAVA_HOME and add it to the binary path, simply login into each machine in the cluster and execute the following commands in the terminal:
```bash
echo "export JAVA_HOME=/proj/michigan-bigdata-PG0/jdk1.8.0_144
export PATH=\${JAVA_HOME}/bin:\$PATH" >> ~/.bashrc
source !$
```
Another thing you may soon find useful is the Simple Build Tool (sbt), run the following command to install it:
```bash
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt
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
To install spark, download and decompress the spark binary on each node in the cluster:
```
wget https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz
tar zvxf spark-2.2.0-bin-hadoop2.7.tgz
```
Instructions on building a spark cluster can be found in Spark's [official document](http://spark.apache.org/docs/2.2.0/spark-standalone.html).

To start the Spark master daemon on one of the nodes, do
```
spark-2.2.0-bin-hadoop2.7/sbin/start-master.sh
```
You can go to `<master_node_IP>:8080` to check the status of the Spark cluster.

To start the Spark slave daemon on the other two nodes, do
```
spark-2.2.0-bin-hadoop2.7/sbin/start-slave.sh <master-spark-URL>
```
where the `<master-spark-URL>` is what you found in the cluster webpage.

To stop all nodes in the cluster, do
```
spark-2.2.0-bin-hadoop2.7/sbin/stop-all.sh
```

### [Apache Hadoop](http://hadoop.apache.org/)
Apache Spark typically needs an underlying distributed file system to store its input data. 
Apache Hadoop is an open-source framework that provides simple programming models distributed for processing of large data sets. 
It mainly consists of the Hadoop Distribited File System (HDFS) and Hadoop YARN. 
Since we use Spark's standalone manager in this assignment, we will only deploy HDFS. 

First, let us get the latest stable version of Hadoop on every machine in the cluster.
```
wget http://apache.mirrors.hoobly.com/hadoop/common/hadoop-2.7.4/hadoop-2.7.4.tar.gz
tar zvxf hadoop-2.7.4.tar.gz
```
You can find the deployment instructions in this [link](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html). 
To make your life easier, we have provided the instructions for you.

There are a few configuration files we need to edit. They are originally empty so users have to manually set them.
Add the following contents in the `<property>` field in `hadoop-2.7.4/etc/hadoop/core-site.xml`:
```
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://namonode_IP:8020</value>
</property>
</configuration>
```
Also you need to add the following in `hadoop-2.7.4/etc/hadoop/hdfs-site.xml`. Make sure you specify the path by yourself.
```
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
Of course, you need to make sure the directory paths you specify do exist. Make the same edits to the config files in the other two machines. 
Make sure the datanode directory path on the other two machines exist as well.

As you have noticed in the lines we added to the configuration file, there are two type of nodes in HDFS -- the namenode and datanodes. 
Think of the namenode as the master node, which is in control of the file system. 
The datanodes, on the other hand, actually store the data.

We also need to edit `hadoop-2.7.4/etc/hadoop/slaves` to add the IP address of all the datanodes. 
In our case, we need to add the IP addresses for all the nodes in the cluster, so every node can store data.

IMPORTANT: You also need to manually specify `JAVA_HOME` in `hadoop-2.7.4/etc/hadoop/hadoop-env.sh`.

Another important step here is to enable the SSH service among the nodes in the cluster. It might seem a little tricky to achieve this in CloudLab. To do this, you have to manually copy the public key of the namenode to the `authorized_keys` file in all the datanodes under `~/.ssh/`. To get the content of the public key, do:
```
cat ~/.ssh/id_rsa.pub
```
When you copy the content, make sure you do not append any newlines. Otherwise, it will not work.

The original disk capacity CloudLab provides you is small. To be able to use HDFS to handle big files, we need to first mount to a larger disk partition. To do this, entering the following comands to your console:
```
sudo mkdir /new_disk
sudo /usr/local/etc/emulab/mkextrafs.pl /new_disk
```
Now /new_disk should mount on /dev/sda4. Use 
```
df -h
```
to check if it is successfully mounted.

The newly mounted disk has permission issue which prevents you from deploying HDFS. To fix that, do the following:
```
sudo chown YOUR_USER_NAME:root -R /new_disk/path_to_hdfs_dir/
```

Now, we start to format the namenode and start the namenode daemon. 
Here, I have already added Hadoop bin directory to my $PATH.
```
hdfs namenode -format
./hadoop-2.7.4/sbin/start-dfs.sh
```
This will also start all the datanode daemons:

To check the HDFS status, go to:
```
<namenode_IP>:50070/dfshealth.html
```
Now, the HDFS is setup. Type the following to see the available commands in HDFS.
```
hdfs dfs -help
```

### [Alluxio](https://www.alluxio.com/)
Alluxio is a memory-speed virtual distributed storage system that bridges applications and underlying storage systems. 
It provides much faster unified data access and can be used to improve the performance and consistency of distributed file systems such as HDFS. 
In this assignment, we will see how much performance improvement Alluxio can bring over HDFS by acting as a caching layer.

To deploy Alluxio, first copy the binary file from the group directory and decompress it:
```
cp /proj/michigan-bigdata-PG0/assignments/assignment1/alluxio-1.5.0-hadoop-2.7-bin.tar.gz ~
cd ~; tar zvxf alluxio-1.5.0-hadoop-2.7-bin.tar.gz
```

You need to edit `alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties`. Copy from the template
```
cp alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties.template alluxio-1.5.0-hadoop-2.7/conf/alluxio-site.properties
```
and update `alluxio.master.hostname` inside the file with the hostname of the machine you plan to run Alluxio Master on. 

You also want to add the IP addresses or hostnames of all the worker nodes to the `conf/workers` file. Then sync all the information to the worker nodes by doing:
```
alluxio-1.5.0-hadoop-2.7/bin/alluxio copyDir alluxio-1.5.0-hadoop-2.7
```
If this command failed, you just need to do it manually.

Another important step here is to add the following two lines to your `spark-default.conf` under you Spark/conf directory. Make sure you specify the correct path:
```
cp spark-2.2.0-bin-hadoop2.7/conf/spark-defaults.conf.template spark-2.2.0-bin-hadoop2.7/conf/spark-defaults.conf
echo "spark.driver.extraClassPath /path/to/alluxio/client/spark/alluxio-1.5.0-spark-client.jar" >> !$
echo "spark.executor.extraClassPath /path/to/alluxio/client/spark/alluxio-1.5.0-spark-client.jar" >> !$
```

Now you can format and start the Alluxio master node.
```
alluxio-1.5.0-hadoop-2.7/bin/alluxio format
alluxio-1.5.0-hadoop-2.7/bin/alluxio-start.sh master
```
To start slave nodes, do:
```
alluxio-1.5.0-hadoop-2.7/bin/alluxio-start.sh worker
```
To check the status of Alluxio, go to:
```
http://<alluxio_master_hostname>:19999
```

## Part 1: Spark and Spark SQL

In the first part of the assignment, you will perform 3 tasks -- ingesting a Wikipedia database into HDFS, parsing the Wikipedia database to generate a webgraph of the internal links, and then use the generated graph as an input to your Spark PageRank program to generate the ranks of the internal links.

### Task 1: Ingest Data into HDFS
In this task, we provide you a big Wikipedia database in xml format. It can be found in the project group directory at `/proj/michigan-bigdata-PG0/assignments/assignment1/enwiki-20110115-pages-articles_whole.xml`. This input file is very big and you have to use distributed file system like HDFS to handle it. The file is also divided into 11 smaller files named `enwiki-20110115-pages-articlesN.xml` in the same directory for debugging purposes. 

To get a sense of how a Wiki page transfers to a xml file, take a look at the following examples:

* [Apple (orig)](https://en.wikipedia.org/wiki/Apple)
* [Apple (xml)](https://en.wikipedia.org/wiki/Special:Export/Apple)

Note that the database we provide you is not up-to-date, but they should be pretty close to what you will find in the above examples.

**Question 1.** What is the default block size on HDFS? What is the default replication factor? 

### Task 2: Webgraph on Internal Links
You are going to write a Spark program which takes the xml file you just ingested as input (enwiki-20110115-pages-articles_whole.xml), and generate a csv file which describes the webgraph of the internal links in Wikipedia. The csv file should look like the following:
```
article1	article0
article1	article2
article1	article3
article2	article3
article2	article0
...
```
It is hard and tedious to find every internal link on a page. We have made the following asumptions to simplify the string parsing for you. The article on the left column corresponds to the string between `<title>` and `</title>`, while the article on the right column are those surrounded by a pair of double brackets `[[ ]]` in the `<text>` field in the xml file with the following requirements:

1. All the letters should be convert to lower case.
2. If the internal link contains a `:`, you should ignore the entire link unless it starts with `Category:`.
3. Ignore links that contain a `#`.
4. If multiple links appear in the brackets, take the first one; e.g., take `A` in `[[A|B]]`.

Those assumptions help you filter out some unnecessary links. Note if the remaining string becomes empty after the filtering, you should also ignore them. When we say ignoring a link, we mean it will not show up in the output file of this task.

The two columns in the output file should be by separated by a `Tab`. You may assume there is no other `Tab`s in the article name.

To get started, you can use the [spark-xml package](https://github.com/databricks/spark-xml) to first read the input xml file into a [DataFrame](http://spark.apache.org/docs/2.2.0/sql-programming-guide.html#datasets-and-dataframes), and go from there.

You will need to figure out how to compile your program and submit as a Spark application and answer the following questions. **You should use the default configuration of Spark, HDFS, and Alluxio unless we specify a different one.** To be clear, you should use the default deploy mode, which is "client". For more information on the two deploy modes Spark supports and when to use them, read the [official document](https://spark.apache.org/docs/latest/submitting-applications.html). You can add dependencies package in your Spark configuration files according to your need although they can also be specified in the command line.

Set the Spark driver memory to 1GB and the Spark executor memory to 5GB to answer Question 2-4.

**Question 2.**  Use `enwiki-20110115-pages-articles1.xml` as input and run the program locally on the master node using 4 cores. What is the completion time of the task?

**Question 3.** Use `enwiki-20110115-pages-articles1.xml` as input and run the program under HDFS inside the Spark cluster you deploy. Is the performance getting better or worse in terms of completion time? Briefly explain.

**Question 4.** Only for this question, change the default block size in HDFS to be 64MB and repeat Question 3. Is the performance getting better or worse in terms of completion time? Briefly explain.

Set the Spark driver memory to 5GB and the Spark executor memory to 5GB to answer Question 5-6. Use this configuration across the entire assignment whenever you generate a web graph from `enwiki-20110115-pages-articles_whole.xml`.

**Question 5.** Use `enwiki-20110115-pages-articles_whole.xml` as input and run the program under HDFS inside the Spark cluster you deploy. Record the completion time. Now, kill the Spark process in one of the worker nodes (use command "jps" to find out the worker process ID) . Rerun the job and record the completion time. Does the job still finish? Do you observe any difference in the completion time? Briefly explain your observations.

**Question 6.** Only for this question, change the replication factor of `enwiki-20110115-pages-articles_whole.xml` to 2 and repeat Question 5 without killing one of the worker nodes. Do you observe any difference in the completion time? Briefly explain.

### Task 3: Spark PageRank
In this task, you are going to implement the PageRank algorithm, which Google uses to rank the website in the Google Search. We will use it to calculate the rank of the articles in Wikipedia. The algorithm can be summarized as follows:

1. Each article has an initial rank of 1.
2. On each iteration, the contribution of an article is calculated as its rank / # of neighbors.
3. Update the rank of the article to be 0.15 + 0.85 * contribution
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
You are going to email a tar.gz file to `eecs598-bigdata-staff@umich.edu.`, which contains the Spark program codes and jar files(or Python files) in the Part 1 Task 2-3 and Part 2 Task 1-2 as well as the Spark configuration files you need to run the three tasks mentioned below. Give each of the 4 codes a meaningful name, such as "Part1Task2" or "CreateGraph".
Name the tar file to be `<uniqueName1>_<uniqueName2>_<uniqueName3>_assignment1.tar.gz`. For example, `mosharaf_yiwenzhg_assignment1.tar.gz`
Every group is going to include a README to record the answers to the 12 questions mentioned in this assignment.
In the README file, you will also provide the instructions (such as commands or scripts) to run the **following 3 tasks on Spark master node locally using 4 cores:** 

1. Use the program in Part 1 Task 2 to take "enwiki-20110115-pages-articles1.xml" as input to generate the graph.
2. Use the program in Part 1 Task 3 to take the graph you just generated and output a rank list of the articles in the dataset.
3. Use the stream emitter you wrote in Part 2 Task 2 to emit the rank list output in the previous step to a local directory while using the stream emitter you wrote in Part 2 Task 1 to dynamically read the files and generate the output mentioned in Part 2 Task 1.

Try to be clear about the instructions to run these steps. The purpose of doing this is to check if your program does what we mention in the spec. Do not worry whether your program has the lowest completion time.

## Acknowledgements
This assignment uses insights from Aditya Akella's Assignment 2 from WISC CS 838: Big Data Systems course. 
