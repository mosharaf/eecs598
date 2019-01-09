# EECS 598: Big Data Systems and Applications (W'19)

## Administrivia
* Catalog Number: 33058
* Lectures/Discussion: 3150 DOW, MW: 12:00 PM – 1:30 PM
* Projects/Makeup: 1200 EECS, F 12:00 PM – 1:00 PM

### Team

| Member (uniqname) | Role | Office Hours |
| :---------------- | :--- | :----------- |
| [Mosharaf Chowdhury](http://www.mosharaf.com/) (mosharaf) | Faculty | 4820 BBB. **By appointments only.**
| Peifeng Yu (peifeng) | GSI | BBB Learning Center, TBA |

### Piazza
**ALL** communication regarding this course must be via [Piazza](https://piazza.com/umich/winter2019/eecs598009w19/). 
This includes questions, discussions, announcements, as well as private messages.

Presentation slides and paper summaries should be emailed to [eecs598-bigdata-staff@umich.edu](mailto:eecs598-bigdata-staff@umich.edu).

## Course Description
This class will introduce you to the key concepts and the state-of-the-art in big data systems and encourage you to think about either building new tools or how to apply an existing one in your own research. 

Since datacenters and cloud computing form the backbone of modern big data systems, we will start with high-level overviews of the two and discuss emerging trends in both software and hardware. 
We will then take a deep dive into the big data systems landscape, focusing on different types of problems. 
A large part of the course this year will focus on the emerging AI systems that include *software systems for machine learning, deep learning, and reinforcement learning*.
We will cover topics from top conferences in systems, networking, and databases venues.

### Prerequisites
Students are expected to have good programming skills and must have taken *at least one* undergraduate-level systems-related course (from operating systems/EECS482, databases/EECS484, distributed systems/EECS491, and networking/EECS489). 

Undergraduates must receive explicit permission from the instructor to enroll, if space permits.


### Textbook
This course has no textbooks. 
We will read recent papers from top venues to understand trends in big data systems and their applications. 

## Tentative Schedule and Reading List
* **Mandatory**: Must read and review.
* **Optional**: Should read. No review.
* **Companion**: Mandatory for presenters. Optional for the rest.

| Date    | Readings                       | Presenter
| --------| -------------------------------| ---------
| Jan 9   | Introduction                   | [Mosharaf](Slides/010919-MChowdhury.pptx) 
|         | **Background**
| Jan 14  | [The Datacenter as a Computer (Chapters 1 and 2)](http://web.eecs.umich.edu/~mosharaf/Readings/DC-Computer.pdf) | Mosharaf
|         | [VL2: A Scalable and Flexible Data Center Network](http://web.eecs.umich.edu/~mosharaf/Readings/VL2.pdf) (Optional)
| Jan 16  | [The Google File System](http://web.eecs.umich.edu/~mosharaf/Readings/GFS.pdf) | Mosharaf
|         | [MapReduce: Simplified Data Processing on Large Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/MapReduce.pdf)
|         | [GFS: Evolution on Fast-Forward](http://web.eecs.umich.edu/~mosharaf/Readings/GFS-ACMQueue-2012.pdf) (Optional)
|         | **Storage and Computation**
| Jan 23  | [Flat Datacenter Storage](http://web.eecs.umich.edu/~mosharaf/Readings/FDS.pdf)
|         | [EC-Cache: Load-balanced, Low-latency Cluster Caching with Online Erasure Coding](http://web.eecs.umich.edu/~mosharaf/Readings/EC-Cache.pdf) (Companion)
|         | [f4: Facebook’s Warm BLOB Storage System](http://web.eecs.umich.edu/~mosharaf/Readings/f4.pdf) (Optional)
| Jan 28  | [Resilient Distributed Datasets: A Fault-tolerant Abstraction for In-Memory Cluster Computing](http://web.eecs.umich.edu/~mosharaf/Readings/Spark.pdf) | 
|         | [CIEL: A Universal Execution Engine for Distributed Data-Flow Computing](http://web.eecs.umich.edu/~mosharaf/Readings/CIEL.pdf) (Companion) | 
|         | [DryadLINQ: A System for General-Purpose Distributed Data-Parallel Computing Using a High-Level Language](http://web.eecs.umich.edu/~mosharaf/Readings/DryadLINQ.pdf) (Optional) | 
|         | **Resource Management and Scheduling**
| Jan 30  | [Borg: Large-Scale Cluster Management at Google with Borg](http://web.eecs.umich.edu/~mosharaf/Readings/Borg.pdf) | 
|         | [Borg, Omega, and Kubernetes](http://queue.acm.org/detail.cfm?id=2898444) (Companion)
|         | [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](http://web.eecs.umich.edu/~mosharaf/Readings/Mesos.pdf) (Optional)
|         | [YARN: Yet Another Resource Negotiator](http://web.eecs.umich.edu/~mosharaf/Readings/YARN.pdf) (Optional) | 
| Feb 4   | [Dominant Resource Fairness: Fair Allocation of Multiple Resource Types](http://web.eecs.umich.edu/~mosharaf/Readings/DRF.pdf) | 
|         | [Altruistic Scheduling in Multi-Resource Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Carbyne.pdf) (Companion)
|         | [Tetris:Multi-Resource Packing for Cluster Schedulers](http://web.eecs.umich.edu/~mosharaf/Readings/Tetris.pdf) (Optional)
|         | **Systems for AI**
| Feb 6   | [TensorFlow: A System for Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TensorFlow.pdf) | 
|         | [Ray: A Distributed Framework for Emerging AI Applications](http://web.eecs.umich.edu/~mosharaf/Readings/Ray.pdf) (Companion) |
| Feb 11  | [Scaling Distributed Machine Learning with the Parameter Server](http://web.eecs.umich.edu/~mosharaf/Readings/Parameter-Server.pdf) | 
|         | [STRADS: A Distributed Framework for Scheduled Model Parallel Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/STRADS.pdf) (Companion)
|         | [Project Adam: Building an Efficient and Scalable Deep Learning Training System](http://web.eecs.umich.edu/~mosharaf/Readings/Project-Adam.pdf) (Optional)
| Feb 13  | [Clipper: A Low-Latency Online Prediction Serving System](http://web.eecs.umich.edu/~mosharaf/Readings/Clipper.pdf) | 
|         | [DeepCPU: Serving RNN-based Deep Learning Models 10x Faster](http://web.eecs.umich.edu/~mosharaf/Readings/DeepCPU.pdf) (Companion)
|         | [Pretzel: Opening the Black Box of Machine Learning Prediction Serving Systems](http://web.eecs.umich.edu/~mosharaf/Readings/Pretzel.pdf) (Optional)
| Feb 18  | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TVM.pdf) | 
|         | [Janus: Fast and Flexible Deep Learning via Symbolic Graph Execution of Imperative Programs](http://web.eecs.umich.edu/~mosharaf/Readings/Janus.pdf) (Companion)
| Feb 20  | [Tiresias: A GPU Cluster Manager for Distributed Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Tiresias.pdf) | 
|         | [Optimus: An Efficient Dynamic Resource Scheduler for Deep Learning Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Optimus.pdf) (Companion)
|         | [Gandiva: Introspective Cluster Scheduling for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Gandiva.pdf) (Optional)
|         | **Video Analytics**
| Feb 25  | [Chameleon: Scalable Adaptation of Video Analytics](http://web.eecs.umich.edu/~mosharaf/Readings/Chameleon.pdf) | 
|         | [Focus: Querying Large Video Datasets with Low Latency and Low Cost](http://web.eecs.umich.edu/~mosharaf/Readings/Focus.pdf) (Companion)
|         | [NoScope: Optimizing Neural Network Queries over Video at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/NoScope.pdf) (Optional)
|         | **SQL**
| Mar 11  | [Spark SQL: Relational Data Processing in Spark](http://web.eecs.umich.edu/~mosharaf/Readings/SparkSQL.pdf) | 
|         | [Impala: A Modern, Open-Source SQL Engine for Hadoop](http://web.eecs.umich.edu/~mosharaf/Readings/Impala.pdf) (Companion)
|         | [Major Technical Advancements in Apache Hive](http://web.eecs.umich.edu/~mosharaf/Readings/Hive.pdf) (Optional)
|         | **Stream Processing**
| Mar 18  | [Discretized Streams: Fault-Tolerant Streaming Computation at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/Spark-Streaming.pdf) | 
|         | [Drizzle: Fast and Adaptable Stream Processing at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/Drizzle.pdf) (Companion)
| Mar 20  | [Storm @Twitter](http://web.eecs.umich.edu/~mosharaf/Readings/Storm-Twitter.pdf) | 
|         | [Twitter Heron: Stream Processing at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/Heron.pdf) (Companion)
|         | [Realtime Data Processing at Facebook](http://web.eecs.umich.edu/~mosharaf/Readings/Facebook-Streaming.pdf) (Optional) | 
| Mar 25  | [Apache Flink™: Stream and Batch Processing in a Single Engine](http://web.eecs.umich.edu/~mosharaf/Readings/Flink.pdf) | 
|         | [Naiad: A Timely Dataflow System](http://web.eecs.umich.edu/~mosharaf/Readings/Naiad.pdf) (Companion)
| Mar 27  | **Mid-Semester Presentations**
|         | **Graph Processing**
| Apr 1   | [PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs](http://web.eecs.umich.edu/~mosharaf/Readings/PowerGraph.pdf) | 
|         | [GraphX: Graph Processing in a Distributed Dataflow Framework](http://web.eecs.umich.edu/~mosharaf/Readings/GraphX.pdf) (Companion)
|         | **Approximate Big Data**
| Apr 3   | [BlinkDB: Queries with Bounded Errors and Bounded Response Times on Very Large Data](http://web.eecs.umich.edu/~mosharaf/Readings/BlinkDB.pdf) | 
|         | [BlinkML: Efficient Maximum Likelihood Estimation with Probabilistic Guarantees](http://web.eecs.umich.edu/~mosharaf/Readings/BlinkML.pdf) (Companion)
|         | [Quickr: Lazily Approximating Complex AdHoc Queries in BigData Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Quickr.pdf) (Optional)
|         | **New Hardware Trends**
| Apr 8   | [Efficient Memory Disaggregation with Infiniswap](http://web.eecs.umich.edu/~mosharaf/Readings/Infiniswap.pdf) | 
|         | [Accelerating Relational Databases by Leveraging Remote Memory and RDMA](http://web.eecs.umich.edu/~mosharaf/Readings/RDMA-DB.pdf) (Companion)
|         | [Remote Memory in the Age of Fast Networks](http://web.eecs.umich.edu/~mosharaf/Readings/RemMem-FastNet.pdf) (Optional)
| Apr 10  | [In-Datacenter Performance Analysis of a Tensor Processing Unit](http://web.eecs.umich.edu/~mosharaf/Readings/TPU.pdf) | 
|         | [Direct Universal Access: Making Data Center Resources Available to FPGA](http://web.eecs.umich.edu/~mosharaf/Readings/DUA.pdf) (Companion)
| Apr 15  | **Wrap Up** | Mosharaf
| Apr 22  | **Final Presentations** |

## Policies

### Honor Code
[The Engineering Honor Code](http://honorcode.engin.umich.edu/) applies to all activities related to this course.

### Groups
All activities of this course will be performed in **groups of 3 students** for the Assignment track.

[Declare your group's membership as well as preferences for track and papers](https://goo.gl/forms/ajVrsWsd7r81daTx2) by January 14, 2019. 
After this date, we will form groups from the remaining students.

Note that there will be *an equal number of groups in each of the two tracks*.
Declared track preference does not guarantee a specific track assignment.

Similarly, paper preferences are also only hints.

### Paper Presentation
The course will be conducted as a seminar. 
Only one group will present in each class.
Each group will be assigned to present two papers (mandatory and companion) on the same day at least once throughout the semester. 
Presentations should last **at most 45 minutes** without interruption.
However, presenters should expect questions and interruptions throughout. 
In the presentation, you should:

* Motivate the paper and provide background.
* Present the high level idea, approach, and/or insight (using examples, whenever appropriate). 
* Discuss technical details so that one can understand the key details without carefully reading it.
* Explain the difference between this paper and related work.
* Raise questions throughout the presentation to generate discussion.

*The slides for a presentation must be emailed to the instructor team at least 24 hours prior to the corresponding class.* 
You should use [this template](Slides/Template.pptx) for making your slides in powerpoint.

### Paper Reviews
Read all the papers of each day carefully and write your own paper review. Being able to critically judge others’ work is crucial for your understanding. For papers that require summaries, you must address a number of questions including:

* What is the problem addressed by the paper, and why is this problem important?
* What is the hypothesis of the work?
* What is the proposed solution, and what key insight guides their solution?
* What is one (or more) drawback or limitation of the proposal, and how will you improve it?

*The paper reviews of each day must be submitted electronically at least 24 hours prior to the corresponding class.*
Late reviews will not be counted. 
You can miss up to 4 paper reviews during the term without penalty. 
Each missing review beyond the fourth one will result in 25% decrease in grade for paper reviews. 
Meaning, failing to turn in 8 or more reviews on time will result in a zero for all paper reviews.

The grade for this part will be assigned as follows: at the end of the term, 2 of your reviews will be randomly selected and graded.
The higher grade of the two will be used for grading. 

Submit reviews via [HotCRP](TBA).

### Participation
You are expected to attend all lectures (you may skip up to 2 lectures due to legitimate reasons), and more importantly, participate in class discussions.

### Assignment Track
If your group is in the assignment track, you will have to complete two assignments on popular big data frameworks Apache Spark and TensorFlow.
The third assignment will likely be different for each group with specific goals, and this will resemble a small research exploration project.
Details of the assignments will be available over time.
Tentative deadlines for the assignments are February 13, March 27, and April 22.

### Research Track
If your group is in the research track, you will have to complete substantive work an instructor-approved problem and have original contribution. 
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work. 
You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Turn in a 2-page draft proposal (including references) by January 30. Remember to include the names and Michigan email addresses of the group members. 
* Keep revising your initial idea and incorporate instructor feedback. However, your team and project proposal must be finalized and approved on or before February 13.
* Each group must submit a 4-page mid-semester progress report and present mid-semester progress during class hours on the week of March 27.
* Each group must present their final results during a presentation or poster session on April 22.
* **Each group must turn in an 8-page final report and your code via email on or before 11:59PM EST on April 26.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.

## Grading
|                         | Assignment Track | Research Track |
| ------------------------| ----------------:| --------------:|
| Paper Summary           | 20%              | 20%
| Paper Presentation      | 20%              | 20%
| Participation           | 10%              | 10%
| Assignment 1            | 15%              | -
| Assignment 2            | 15%              | -
| Assignment 3            | 20%              | -
| Research Proposal       | -                | 10%
| Mid-Semester Checkpoint | -                | 15%
| Final Report            | -                | 25%
