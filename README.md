# EECS 598: Systems for AI (W'21)

## Administrivia
* Catalog Number: 29495
* Lectures/Discussion: Live Online, MW: 1:30 PM – 3:00 PM
* Projects/Makeup: Live Online, F 2:00 PM – 3:00 PM
* Counts as: Software Breadth and Depth (PhD); Technical Elective and 500-Level (MS/E)

### Team

| Member (uniqname) | Role | Office Hours |
| :---------------- | :--- | :----------- |
| [Mosharaf Chowdhury](http://www.mosharaf.com/) (mosharaf) | Faculty | 4820 BBB. **By appointments only.**
| Sanjay Singapuram (singam) | GSI | 11 AM - 12 PM every Thu

### Piazza
**ALL** communication regarding this course must be via [Piazza](https://piazza.com/umich/winter2021/eecs598009w21/).
This includes questions, discussions, announcements, as well as private messages.

Presentation slides and paper summaries should be emailed to [eecs598-bigdata-staff@umich.edu](mailto:eecs598-bigdata-staff@umich.edu).

## Course Description
This class will introduce you to the key concepts and the state-of-the-art in practical, scalable, and fault-tolerant software systems for AI and encourage you to think about either building new tools or how to apply an existing one in your own research. 

Since datacenters and cloud computing form the backbone of modern computing, we will start with an overview of the two. 
We will then take a deep dive into systems for big data and AI landscapes, focusing on different types of problems. 
Our topics will include: 
backgrounds on datacenters and edge; 
systems for deep learning, machine learning, and reinforcement learning; runtime execution and compilers for AI; 
distributed and federated learning systems; 
serving systems and inference;
scheduling and resource management in AI clusters;
etc.
We will cover topics from top conferences in systems, networking, and databases venues.

Note that this course is **NOT focused on AI methods**. 
Instead, we will *focus on how one can build practical software systems* so that existing AI methods can be used in practice. 

### Prerequisites
Students are expected to have good programming skills and must have taken *at least one* undergraduate-level systems-related course (from operating systems/EECS482, databases/EECS484, distributed systems/EECS491, and networking/EECS489).

### Textbook
This course has no textbooks.
We will read recent papers from top venues to understand trends in big data systems and their applications.

## Tentative Schedule and Reading List

| Date    | Readings                       | Presenter | Summary
| --------| -------------------------------| --------- | -------
|         | **Introduction** |
| Jan 20  | [Analysis of Large-Scale Multi-Tenant GPU Clusters for DNN Training Workloads](http://web.eecs.umich.edu/~mosharaf/Readings/Fiddle-Philly.pdf) | [Mosharaf](Slides/012021-MChowdhury.pptx)
|         | [TFX: A TensorFlow-Based Production-Scale Machine Learning Platform](http://web.eecs.umich.edu/~mosharaf/Readings/TFX.pdf)
|         | [Applied Machine Learning at Facebook: A Datacenter Infrastructure Perspective](http://web.eecs.umich.edu/~mosharaf/Readings/FB-ML.pdf)
|         | [Machine Learning at Facebook: Understanding Inference at the Edge](http://web.eecs.umich.edu/~mosharaf/Readings/FB-ML-Edge.pdf)
|         | **Background**
| Jan 25  | [The Datacenter as a Computer](http://web.eecs.umich.edu/~mosharaf/Readings/DC-Computer.pdf) (Chapters 1 and 2) | [Mosharaf](Slides/012521-MC-DCComputer-DCN.pptx) | [Tianyi-Lingyun-Haojie](Summaries/012521-DCaaC-Jupiter.pdf)
|         | [Jupiter Rising: A Decade of Clos Topologies and Centralized Control in Google's Datacenter Network](http://web.eecs.umich.edu/~mosharaf/Readings/Jupiter.pdf)
| Feb  1  | [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing](http://web.eecs.umich.edu/~mosharaf/Readings/Spark.pdf) | [Mosharaf](Slides/020121-MC-Spark-FDS.pptx)
|         | [Flat Datacenter Storage](http://web.eecs.umich.edu/~mosharaf/Readings/FDS.pdf)
|         | **Frameworks**
| Feb  3  | [TensorFlow: A System for Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TensorFlow.pdf) | [Abzaliev-Saisamrit](Slides/020321-TF-DCFLML.pdf)
|         | [Dynamic Control Flow in Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/DynamicControlFlow-TF.pdf)
| Feb  8  | [Ray: A Distributed Framework for Emerging AI Applications](http://web.eecs.umich.edu/~mosharaf/Readings/Ray.pdf) | [Joshua-Shucheng-Han](Slides/020821-Ray-Stash.pdf) | [Yiran-Jonah-WeiChung](Summaries/020821-Ray-Stash.pdf)
|         | [Lineage Stash: Fault Tolerance Off the Critical Path](http://web.eecs.umich.edu/~mosharaf/Readings/LineageStash.pdf)
|         | **Distributed and Federated Learning**
| Feb 10  | [Scaling Distributed Machine Learning with the Parameter Server](http://web.eecs.umich.edu/~mosharaf/Readings/ParameterServer.pdf) | [Christopher-Joe-Roland](Slides/021021-ParamServ-Adam.pdf) | [Jie-Yin-Jinyang](Summaries/021021-ParamServer-Adam.pdf)
|         | [Project Adam: Building an Efficient and Scalable Deep Learning Training System](http://web.eecs.umich.edu/~mosharaf/Readings/Project-Adam.pdf) 
| Feb 15  | [PipeDream: Generalized Pipeline Parallelism for DNN Training](http://web.eecs.umich.edu/~mosharaf/Readings/PipeDream.pdf) | [Yabin-Haofeng-Hanchi](Slides/021521-Pipedream-BytePS.pdf) | [Abzaliev-Saisamrit](Summaries/021521-Pipedream-BytePS.pdf)
|         | [A Unified Architecture for Accelerating Distributed DNN Training in Heterogeneous GPU/CPU Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/BytePS.pdf)
| Feb 17  | [Gaia: Geo-Distributed Machine Learning Approaching LAN Speeds](http://web.eecs.umich.edu/~mosharaf/Readings/Gaia.pdf) | [Jie-Yin-Jinyang](Slides/021721-Gaia-TFF.pdf) | [Christopher-Joe-Roland](Summaries/021721-Gaia-TFF.pdf)
|         | [Towards Federated Learning at Scale: System Design](http://web.eecs.umich.edu/~mosharaf/Readings/TFF.pdf)
|         | **Runtime and Compiler Optimizations**
| Feb 22  | [Ansor: Generating High-Performance Tensor Programs for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Ansor.pdf) | [Tianyi-Lingyun-Haojie](Slides/022221-TASO-ANSOR.pdf) | [Yabin-Haofeng-Hanchi](Summaries/022221-TASO-ANSOR.pdf)
|         | [TASO: Optimizing Deep Learning Computation with Automated Generation of Graph Substitutions](http://web.eecs.umich.edu/~mosharaf/Readings/TASO.pdf)
| Mar  1  | [Rammer: Enabling Holistic Deep Learning Compiler Optimizations with rTasks](http://web.eecs.umich.edu/~mosharaf/Readings/Rammer.pdf) | [Qiyue-Tianrong](Slides/030121-Rammer-Hummingbird.pdf) | [Anshul-Drake](Summaries/030121-Rammer-Hummingbird.pdf)
|         | [A Tensor Compiler for Unified Machine Learning Prediction Serving](http://web.eecs.umich.edu/~mosharaf/Readings/Hummingbird.pdf)
| Mar  8  | **Mid-Semester Presentations**
| Mar 10  | **Mid-Semester Presentations**
|         | **Serving Systems and Inference**
| Mar 12  | [Serving DNNs like Clockwork: Performance Predictability from the Bottom Up](http://web.eecs.umich.edu/~mosharaf/Readings/Clockwork.pdf) | [Anshul-Drake](Slides/031221-Clipper-Clockwork.pdf) | Wenyuan-Ruiyang-Shuowei
|         | [Clipper: A Low-Latency Online Prediction Serving System](http://web.eecs.umich.edu/~mosharaf/Readings/Clipper.pdf)
| Mar 17  | [Focus: Querying Large Video Datasets with Low Latency and Low Cost](http://web.eecs.umich.edu/~mosharaf/Readings/Focus.pdf) | Yiran-Jonah-WeiChung | Wenqi-Jianbin-Shi
|         | [Nexus: A GPU Cluster Engine for Accelerating DNN-Based Video Analysis](http://web.eecs.umich.edu/~mosharaf/Readings/Nexus.pdf)
|         | **Hyperparameter Tuning**
| Mar 22  | [A System for Massively Parallel Hyperparameter Tuning](http://web.eecs.umich.edu/~mosharaf/Readings/ASHA.pdf) | Muhammed | Jiachen-Qinye-Yibo
|         | [BOHB: Robust and Efficient Hyperparameter Optimization at Scale](http://web.eecs.umich.edu/~mosharaf/Readings/BOHB.pdf)
| Mar 24  | [Retiarii: A Deep Learning Exploratory-Training Framework](http://web.eecs.umich.edu/~mosharaf/Readings/Retiarii.pdf) | Jiachen-Qinye-Yibo | Tianyi-Lingyun-Haojie
|         | [FluidExec: A Generic Resource-Aware Hyperparameter Tuning Execution Engine](http://web.eecs.umich.edu/~mosharaf/Readings/FluidExec.pdf)
|         | **Scheduling and Resource Management**
| Mar 29  | [Tiresias: A GPU Cluster Manager for Distributed Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Tiresias.pdf) | Wenyuan-Ruiyang-Shuowei | Joshua-Shucheng-Han
|         | [HiveD: Sharing a GPU Cluster for Deep Learning with Guarantees](http://web.eecs.umich.edu/~mosharaf/Readings/HiveD.pdf)
| Mar 31  | [AntMan: Dynamic Scaling on GPU Clusters for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/AntMan.pdf) | Wenqi-Jianbin-Shi | Muhammed
|         | [PipeSwitch: Fast Pipelined Context Switching for Deep Learning Applications](http://web.eecs.umich.edu/~mosharaf/Readings/PipeSwitch.pdf)
|         | **Emerging Hardware**
| Apr  5  | [In-Datacenter Performance Analysis of a Tensor Processing Unit](http://web.eecs.umich.edu/~mosharaf/Readings/TPU.pdf) |  | Qiyue-Tianrong
|         | [Serving DNNs in Real Time at Datacenter Scale with Project Brainwave](http://web.eecs.umich.edu/~mosharaf/Readings/Brainwave.pdf)
| Apr  7  | **Wrap Up** | 
| Apr 19  | **Final Presentations** | 
| Apr 21  | **Final Presentations** | 

## Policies

### Honor Code
[The Engineering Honor Code](http://honorcode.engin.umich.edu/) applies to all activities related to this course.

### Lecture Recordings
Course lectures will be audio/video recorded and made available to other students in this course. 
As part of your participation in this course, you may be recorded. 

Students may not record or distribute any class activity without written permission from the instructor, except as necessary as part of approved accommodations for students with disabilities. 
Any approved recordings may only be used for the student's own private use.

### Groups
All activities of this course will be performed in **groups of 2-3 students**.

[Declare your group's membership and paper preferences](https://forms.gle/aTPa6DQKWb2mtpA47) by February 1, 2021. 
After this date, we will form groups from the remaining students.

### Paper Presentation
The course will be conducted as a seminar. 
Only one group will synchronously present in each class.
Each group will be assigned to present a paper at least once throughout the semester. 
Presentations should last **at most 40 minutes** without interruption.
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
You are expected to attend **all** lectures (you may skip up to 4 lectures due to legitimate reasons), and more importantly, participate in class discussions.
Although the lectures will be recorded, given the discussion-based nature of this course, participation is required both for your own understanding and to improve the overall quality of the course.

A key part of participation will be in the form of discussion in piazza.
The group in charge of the summary should initiate the discussion and the rest should participate.
Not everyone must have add something every day, but it is expected that everyone has something to say over the semester.

### Project
You will have to complete substantive work an instructor-approved problem and have original contribution.
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work.
You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Form a group of 2-3 members by **February 1**.
* Turn in a 2-page draft proposal (including references) by **February 10**. Remember to include the names and Michigan email addresses of the group members. Schedule a 15-minute meeting to pitch your idea and to get early feedback.
* Keep revising your initial idea and incorporate instructor feedback. However, your project proposal must be finalized and approved on or before **February 17**.
* Each group must present mid-semester progress during class hours on **March 8 and March 10**.
* Each group must turn in an 8-page final report and your code via email **on or before 11:59PM EST on April 27.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.

## Tentative Grading
|                         | Weight | 
| ------------------------| ------:| 
| Paper Summary           | 20%    | 
| Paper Presentation      | 20%    | 
| Participation           | 10%    | 
| Assignment              | 10%    | 
| Project                 | 40%    | 

