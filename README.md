# EECS 598: Systems for AI (W'20)

## Administrivia
* Catalog Number: 30123
* Lectures/Discussion: 3150 DOW, MW: 12:00 PM – 1:30 PM
* Projects/Makeup: 1200 EECS, F 12:00 PM – 1:00 PM

### Team

| Member (uniqname) | Role | Office Hours |
| :---------------- | :--- | :----------- |
| [Mosharaf Chowdhury](http://www.mosharaf.com/) (mosharaf) | Faculty | 4820 BBB. **By appointments only.**

### Piazza
**ALL** communication regarding this course must be via [Piazza](https://piazza.com/umich/winter2020/eecs598009w20/).
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

| Date    | Readings                       | Presenter
| --------| -------------------------------| ---------
| Jan 10  | **Introduction** | Mosharaf
|         | **Background**
| Jan 13  | The Datacenter as a Computer (Chapters 1 and 2) | Mosharaf
|         | VL2: A Scalable and Flexible Data Center Network
| Jan 15  | Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing 
|         | Flat Datacenter Storage
|         | **Frameworks**
| Jan 22  | TensorFlow: A System for Large-Scale Machine Learning
|         | PyTorch: An Imperative Style, High-Performance Deep Learning Library
| Jan 27  | Ray: A Distributed Framework for Emerging AI Applications
|         | Dynamic Control Flow in Large-Scale Machine Learning
|         | **Distributed and Federated Learning**
| Jan 29  | Scaling Distributed Machine Learning with the Parameter Server
|         | STRADS: A Distributed Framework for Scheduled Model Parallel Machine Learning
| Feb 3   | PipeDream: Generalized Pipeline Parallelism for DNN Training
|         | Supporting Very Large Models using Automatic Dataflow Graph Partitioning
| Feb 10  | Towards Federated Learning at Scale: System Design
|         | Scaling Video Analytics on Constrained Edge Nodes
|         | **Runtime and Compiler Optimizations**
| Feb 12  | JANUS: Fast and Flexible Deep Learning via Symbolic Graph Execution of Imperative Programs
|         | TASO: Optimizing Deep Learning Computation with Automated Generation of Graph Substitutions
| Feb 17  | TVM: An Automated End-to-End Optimizing Compiler for Deep Learning
|         | An Intermediate Representation for Optimizing Machine Learning Pipelines
|         | **Serving Systems and Inference**
| Feb 19  | Pretzel: Opening the Black Box of Machine Learning Prediction Serving Systems
|         | Parity Models: Erasure-Coded Resilience for Prediction Serving Systems
| Feb 24  | GRNN: Low-Latency and Scalable RNN Inference on GPUs
|         | Nexus: A GPU Cluster Engine for Accelerating DNN-Based Video Analysis
|         | **Hyperparameter Tuning**
| Feb 26  | Google Vizier: A Service for Black-Box Optimization
|         | Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization
|         | **Testing, Verification, Security, and Privacy**
| Mar 9   | DeepXplore: Automated Whitebox Testing of Deep Learning Systems
|         | DeepBase: Deep Inspection of Neural Networks
| Mar 11  | Privacy Accounting and Quality Control in the Sage Differentially Private ML Platform
|         | SecureML: A System for Scalable Privacy-Preserving Machine Learning
| Mar 16  | **Mid-Semester Presentations**
| Mar 18  | **Mid-Semester Presentations**
|         | **ML Systems in Practice**
| Mar 23  | Analysis of Large-Scale Multi-Tenant GPU Clusters for DNN Training Workloads
|         | TFX: A TensorFlow-Based Production-Scale Machine Learning Platform
| Mar 25  | Applied Machine Learning at Facebook: A Datacenter Infrastructure Perspective
|         | Machine Learning at Facebook: Understanding Inference at the Edge
|         | **Scheduling and Resource Management**
| Mar 30  | Tiresias: A GPU Cluster Manager for Distributed Deep Learning
|         | Gandiva: Introspective Cluster Scheduling for Deep Learning
| Apr 1   | Salus: Fine-Grained GPU Sharing Primitives for Deep Learning Applications
|         | SuperNeurons: Dynamic GPU Memory Management for Training Deep Neural Networks
|         | **Emerging Hardware**
| Apr 6   | In-Datacenter Performance Analysis of a Tensor Processing Unit
|         | Serving DNNs in Real Time at Datacenter Scale with Project Brainwave
|         | **ML for Systems**
| Apr 8   | Neural Packet Classification
|         | Learning Scheduling Algorithms for Data Processing Clusters
| Apr 13  | **Wrap Up** | Mosharaf
| Apr 15  | **Final Presentations** |

## Policies

### Honor Code
[The Engineering Honor Code](http://honorcode.engin.umich.edu/) applies to all activities related to this course.

### Paper Reviews
Read all the papers of each day carefully and **write your own paper review**. Being able to critically judge others’ work is crucial for your understanding. 
For papers that require summaries, you must address a number of questions including:

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

Submit reviews via [HotCRP](https://bigdata1.eecs.umich.edu/).

### Paper Presentation
The course will be conducted as a seminar.
Depending on the final class size, presentations will be done in groups or individually.
Each student, indiviudally or in group, will be assigned to present two papers (mandatory and companion) on the same day at least once throughout the semester.
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

### Participation
You are expected to attend all lectures (you may skip up to 2 lectures due to legitimate reasons), and more importantly, participate in class discussions.

### Project
You will have to complete substantive work an instructor-approved problem and have original contribution.
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work.
You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Form a group of 2-3 members by **January 20**.
* Turn in a 2-page draft proposal (including references) by **January 31**. Remember to include the names and Michigan email addresses of the group members. Schedule a 15-minute meeting to pitch your idea and to get early feedback.
* Keep revising your initial idea and incorporate instructor feedback. However, your project proposal must be finalized and approved on or before **February 14**.
* Each group must present mid-semester progress during class hours on **March 16 and March 18**.
* Each group must present their final results during a presentation or poster session on **April 15**.
* Each group must turn in an 8-page final report and your code via email **on or before 11:59PM EST on April 21.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.

## Grading
|                         | Weight | Description | 
| ------------------------| ------:| ----------- |
| Paper Summary           | 20%    | Written summaries of 2 papers per week.
| Paper Presentation      | 20%    | At least one paper presentation.
| Participation           | 10%    | Preparation and participation in classroom discussions.
| Project                 | 50%    | Substantial research project with a final paper and poster presentation.

