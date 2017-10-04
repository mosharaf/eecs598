# EECS 598: Big Data Systems and Applications

## Administrivia
* Catalog Number: 31878
* Lectures/Discussion: 2166 DOW, MW: 12:00 PM – 1:30 PM
* Projects/Makeup: 1690 BEYSTER, F 12:00 PM – 1:00 PM

### Team

| Member (uniqname) | Role | Office Hours |
| :---------------- | :--- | :----------- |
| [Mosharaf Chowdhury](http://www.mosharaf.com/) (mosharaf) | Faculty | 4820 BBB. **By appointments only.**
| Yiwen Zhang (yiwenzhg) | GSI | BBB Learning Center, F 2:00 PM - 4:00 PM |

### Piazza
**ALL** communication regarding this course must be via [Piazza](https://piazza.com/umich/fall2017/eecs598001f17/). 
This includes questions, discussions, announcements, as well as private messages.

Presentation slides and paper summaries should be emailed to [eecs598-bigdata-staff@umich.edu](mailto:eecs598-bigdata-staff@umich.edu).

## Course Description
This class will introduce you to the key concepts and the state-of-the-art in big data systems and encourage you to think about either building new tools or how to apply an existing one in your own research. 

Since datacenters and cloud computing form the backbone of modern big data systems, we will start with high-level overviews of the two and discuss emerging trends in both software and hardware. 
We will then take a deep dive into the big data systems landscape, focusing on different types of problems. 
Our journey will cover topics from top conferences such as SOSP, OSDI, NSDI, SIGCOMM, SIGMOD, and EuroSys on SQL queries, log analysis, machine learning activities, graph processing, approximation queries, stream processing, interactive analysis, and deep learning.

### Prerequisites
Students are expected to have good programming skills and must have taken *at least one* undergraduate-level systems-related course (from operating systems, databases, distributed systems, and networking). 

Undergraduates must receive explicit permission from the instructor to enroll, if space permits.


### Textbook
This course has no textbooks. 
We will read recent papers from top venues to understand trends in big data systems and their applications. 

## Tentative Schedule and Reading List
* **Mandatory**: Unless otherwise specified.
* **Optional**: Can skip, but should skim.
* **Companion**: Mandatory for presenters and critics. Optional for the rest.

| Date    | Readings                       | Presenter| Critic |
| --------| -------------------------------| ---------| ------ |
| Sep 6   | Introduction                   | [Mosharaf](Slides/090617-MChowdhury.pptx) | |
|         | **Background**
| Sep 11  | [The Datacenter as a Computer (Chapters 1 and 2)](http://web.eecs.umich.edu/~mosharaf/Readings/DC-Computer.pdf) | [Mosharaf](Slides/091117-MC-DCComputer-DCN.pptx)
|         | [VL2: A Scalable and Flexible Data Center Network](http://web.eecs.umich.edu/~mosharaf/Readings/VL2.pdf) (Optional)
| Sep 13  | [The Google File System](http://web.eecs.umich.edu/~mosharaf/Readings/GFS.pdf) | [Mosharaf](Slides/091317-MC-GFS-MapReduce.pptx)
|         | [MapReduce: Simplified Data Processing on Large Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/MapReduce.pdf)
|         | [GFS: Evolution on Fast-Forward](http://web.eecs.umich.edu/~mosharaf/Readings/GFS-ACMQueue-2012.pdf) (Optional)
|         | **Resource Management**
| Sep 18  | [YARN: Yet Another Resource Negotiator](http://web.eecs.umich.edu/~mosharaf/Readings/YARN.pdf) | [Matthew-Ayush-HyunJong](Slides/091817-YARN.pptx) | [ChunJung-TingWei-Vandit*](Summaries/091817-YARN.pdf)
|         | [Borg, Omega, and Kubernetes](http://queue.acm.org/detail.cfm?id=2898444) (Companion)
|         | [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](http://web.eecs.umich.edu/~mosharaf/Readings/Mesos.pdf) (Optional)
| Sep 20  | [Dominant Resource Fairness: Fair Allocation of Multiple Resource Types](http://web.eecs.umich.edu/~mosharaf/Readings/DRF.pdf) | [Fan-Hasan-Henry](Slides/092017-DRF.pptx) | [Andrew-William-Zhao*](Summaries/092017-DRF.pdf)
|         | [Altruistic Scheduling in Multi-Resource Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Carbyne.pdf) (Companion)
|         | **Dataflow Programming Frameworks and Execution Engines**
| Sep 27  | [Resilient Distributed Datasets: A Fault-tolerant Abstraction for In-memory Cluster Computing](http://web.eecs.umich.edu/~mosharaf/Readings/Spark.pdf) | [Dong-Jinxiaoyu-Huanyu](Slides/092717-RDD.pptx) | [Qiyang-Ruying](Summaries/092717-RDD.pdf)
|         | [Apache Tez: A Unifying Framework for Modeling and Building Data Processing Applications](http://web.eecs.umich.edu/~mosharaf/Readings/Tez.pdf) (Companion)
| Sep 29  | [Naiad: A Timely Dataflow System](http://web.eecs.umich.edu/~mosharaf/Readings/Naiad.pdf) | [Die-Chi-Shaowen](Slides/092917-Naiad.pptx) | [Matthew-Ayush-HyunJong](Summaries/092917-Naiad.pdf)
|         | **Batch Processing**
| Oct 2   | [Spark SQL: Relational Data Processing in Spark](http://web.eecs.umich.edu/~mosharaf/Readings/SparkSQL.pdf) | [Bor-ChungWen-Hongyu](Slides/100217-SparkSQL-Hive.pptx) | [Dong-Jinxiaoyu-Huanyu](Summaries/100217-SparkSQL-Hive.pdf)
|         | [Major Technical Advancements in Apache Hive](http://web.eecs.umich.edu/~mosharaf/Readings/Hive.pdf) (Companion)
| Oct 4   | [Global Analytics in the Face of Bandwidth and Regulatory Constraints](http://web.eecs.umich.edu/~mosharaf/Readings/Geode.pdf) | [Fan-Hasan-Henry*](Slides/100417-Geode.pptx) | Boyu-Rui-Haojun*
|         | [Clarinet: WAN-Aware Optimization for Analytics Queries](http://web.eecs.umich.edu/~mosharaf/Readings/Clarinet.pdf) (Companion)
|         | **Stream Processing**
| Oct 9   | [Discretized Streams: Fault-Tolerant Streaming Computation at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/Spark-Streaming.pdf) | ChunJung-TingWei-Vandit | TaiYing-PeiXuan-Changfeng
|         | [Storm @Twitter](http://web.eecs.umich.edu/~mosharaf/Readings/Storm-Twitter.pdf) (Companion)
| Oct 11  | [Realtime Data Processing at Facebook](http://web.eecs.umich.edu/~mosharaf/Readings/Facebook-Streaming.pdf) | TaiYing-PeiXuan-Changfeng | Wen-Eric-Kevin
|         | [Twitter Heron: Stream Processing at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/Heron.pdf) (Companion)
| Oct 18  | [StreamScope: Continuous Reliable Distributed Processing of Big Data Streams](http://web.eecs.umich.edu/~mosharaf/Readings/StreamScope.pdf) | Die-Chi-Shaowen* | Bor-ChungWen-Hongyu
|         | **Graph Processing**
| Oct 23  | [PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs](http://web.eecs.umich.edu/~mosharaf/Readings/PowerGraph.pdf) | Wen-Eric-Kevin* | Dong-Jinxiaoyu-Huanyu*
|         | [GraphX: Graph Processing in a Distributed Dataflow Framework](http://web.eecs.umich.edu/~mosharaf/Readings/GraphX.pdf) (Companion)
|         | **Machine Learning**
| Oct 25  | [Scaling Distributed Machine Learning with the Parameter Server](http://web.eecs.umich.edu/~mosharaf/Readings/Parameter-Server.pdf) | Qiyang-Ruying | Die-Chi-Shaowen
|         | [Project Adam: Building an Efficient and Scalable Deep Learning Training System](http://web.eecs.umich.edu/~mosharaf/Readings/Project-Adam.pdf) (Optional)
| Oct 30  | [TensorFlow: A System for Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TensorFlow.pdf) | Wen-Eric-Kevin | Boyu-Rui-Haojun
| Nov 1   | [TuX2: Distributed Graph Computation for Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TuX2.pdf) | Andrew-William-Zhao | Wenting-Peter
| Nov 10  | [Gaia: Geo-Distributed Machine Learning Approaching LAN Speeds](http://web.eecs.umich.edu/~mosharaf/Readings/Gaia.pdf) | Matthew-Ayush-HyunJong* | Fan-Hasan-Henry
| Nov 13  | **Mid-Semester Presentations** | | |
|         | **Approximate Query Processing**
| Nov 15  | [BlinkDB: Queries with Bounded Errors and Bounded Response Times on Very Large Data](http://web.eecs.umich.edu/~mosharaf/Readings/BlinkDB.pdf) | Boyu-Rui-Haojun | Wenting-Peter*
| Nov 22  | [Quickr: Lazily Approximating Complex AdHoc Queries in BigData Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Quickr.pdf) | Andrew-William-Zhao | Bor-ChungWen-Hongyu*
|         | **RDMA-Enabled Systems**
| Nov 29  | [FaRM: Fast Remote Memory](http://web.eecs.umich.edu/~mosharaf/Readings/FaRM-NSDI.pdf) | Qiyang-Ruying* | TaiYing-PeiXuan-Changfeng*
|         | [No Compromises: Distributed Transactions with Consistency, Availability, and Performance](http://web.eecs.umich.edu/~mosharaf/Readings/FaRM-SOSP.pdf) (Companion)
| Dec 4   | [Efficient Memory Disaggregation with Infiniswap](http://web.eecs.umich.edu/~mosharaf/Readings/Infiniswap.pdf) | Wenting-Peter | ChunJung-TingWei-Vandit
| Dec 6   | **Wrap Up** | | |
| Dec 11  | **Final Presentation** | | |

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


## Policies

### Honor Code
[The Engineering Honor Code](http://honorcode.engin.umich.edu/) applies to all activities related to this course.

### Groups
All activities of this course will be performed in **groups of 3 students** for the Assignment track.
Exceptions may be made for the Research track. 

[Declare your group's membership and paper preferences](https://goo.gl/qzMjq4) by September 11, 2017. 
After this date, we will form groups from the remaining students.

### Paper Presentation
The course will be conducted as a seminar. 
Only one group will present in each class.
Each group will be assigned to present a paper at least once throughout the semester. 
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

### Paper Summaries
Each group will also be assigned to write one or more paper summaries. 
The paper summary assigned to a group may not be the same paper they have presented.

A paper summary must address the following four questions in sufficient details (2-3 pages):

* What is the problem addressed by the paper, and why is this problem important?
* What is the hypothesis of the work?
* What is the proposed solution, and what key insight guides their solution?
* What is one (or more) drawback or limitation of the proposal, and how will you improve it?

*The paper summary of a paper must be emailed to the instructor team within 24 hours after its presentation.* 
**Late reviews will not be counted.** 
You should use [this template](Summaries/Template.md) for writing your summary.
Allocate enough time for your reading, discuss as a group, write the summary carefully, and finally, include key observations from the class discussion.

Because you do not have to write summaries/reviews for each paper, you cannot avoid reading a paper. 
Everyone is expected to have read all the papers. 
Being able to critically judge others' work is crucial for your understanding. 

### Participation
You are expected to attend all lectures (you may skip up to 2 lectures due to legitimate reasons), and more importantly, participate in class discussions.

### Assignment Track
If your group chooses the assignment track, you will have to complete two assignments on popular big data frameworks Apache Spark and TensorFlow.
The third assignment will likely be different for each group with specific goals, and this will resemble a small research exploration project.
Details of the assignments will be available over time.
Tentative deadlines for the assignments are October 11, November 13, and December 11.

### Research Track
If your group chooses the research track, you will have to complete substantive work an instructor-approved problem and have original contribution. 
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work. 
You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Turn in a 2-page draft proposal (including references) by September 27. Remember to include the names and Michigan email addresses of the group members. 
* Keep revising your initial idea and incorporate instructor feedback. However, your team and project proposal must be finalized and approved on or before October 11.
* Each group must submit a 4-page mid-semester progress report and present mid-semester progress during class hours on the week of November 13.
* Each group must present their final results during a presentation or poster session on December 11.
* **Each group must turn in an 8-page final report and your code via email on or before 11:59PM EST on December 15.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.
