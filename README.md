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

| Date    | Readings                       | Presenter | Summary
| --------| -------------------------------| --------- | -------
| Jan 10  | **Introduction** | [Mosharaf](Slides/011020-MChowdhury.pptx)
|         | **Background**
| Jan 13  | [The Datacenter as a Computer](http://web.eecs.umich.edu/~mosharaf/Readings/DC-Computer.pdf) (Chapters 1 and 2) | [Mosharaf](Slides/011320-MC-DCComputer-DCN.pptx)
|         | [VL2: A Scalable and Flexible Data Center Network](http://web.eecs.umich.edu/~mosharaf/Readings/VL2.pdf)
| Jan 15  | [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing](http://web.eecs.umich.edu/~mosharaf/Readings/Spark.pdf) | [Mosharaf](Slides/011520-MC-Spark-FDS.pptx)
|         | [Flat Datacenter Storage](http://web.eecs.umich.edu/~mosharaf/Readings/FDS.pdf) |  | [Xiangfeng](Summaries/011520-FDS.pdf)
|         | **Frameworks**
| Jan 22  | [TensorFlow: A System for Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TensorFlow.pdf) | [Hengjia-Jiaqing-Yide](Slides/012220-TensorFlow-Pytorch.pptx) | [Jiho-Matthew-Zineb](Summaries/012220-TensorFlow-Pytorch.pdf)
|         | [PyTorch: An Imperative Style, High-Performance Deep Learning Library](http://web.eecs.umich.edu/~mosharaf/Readings/PyTorch.pdf)
| Jan 27  | [Ray: A Distributed Framework for Emerging AI Applications](http://web.eecs.umich.edu/~mosharaf/Readings/Ray.pdf) | [Hengjia-Jiaqing-Yide](Slides/012720-Ray-DCF.pptx) | [Diego](Summaries/012720-Ray-DCF.pdf)
|         | [Dynamic Control Flow in Large-Scale Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/DynamicControlFlow-TF.pdf)
|         | **Distributed and Federated Learning**
| Jan 29  | [Scaling Distributed Machine Learning with the Parameter Server](http://web.eecs.umich.edu/~mosharaf/Readings/ParameterServer.pdf) | [Jiho-Matthew-Zineb](Slides/012920-ParameterServer-STRADS.pptx) | [Runyu-Shangquan](Summaries/012920-ParameterServer-STRADS.pdf)
|         | [STRADS: A Distributed Framework for Scheduled Model Parallel Machine Learning](http://web.eecs.umich.edu/~mosharaf/Readings/STRADS.pdf)
| Feb 3   | [PipeDream: Generalized Pipeline Parallelism for DNN Training](http://web.eecs.umich.edu/~mosharaf/Readings/PipeDream.pdf) | [Alexandra-Wenyi](Slides/020320-PipeDream-Tofu.pptx) | [Adam-Mihir](Summaries/020320-PipeDream-Tofu.pdf)
|         | [Supporting Very Large Models using Automatic Dataflow Graph Partitioning](http://web.eecs.umich.edu/~mosharaf/Readings/Tofu.pdf)
| Feb 10  | [Towards Federated Learning at Scale: System Design](http://web.eecs.umich.edu/~mosharaf/Readings/TFF.pdf) | [Chris-Jiachen-Xiangfeng](Slides/021020-TFF-FilterForward.pptx) | [Chris-Jiachen-Xiangfeng](Summaries/021020-TFF-FilterForward.pdf)	
|         | [Scaling Video Analytics on Constrained Edge Nodes](http://web.eecs.umich.edu/~mosharaf/Readings/FilterForward.pdf)
|         | **Runtime and Compiler Optimizations**
| Feb 12  | [JANUS: Fast and Flexible Deep Learning via Symbolic Graph Execution of Imperative Programs](http://web.eecs.umich.edu/~mosharaf/Readings/Janus.pdf) | [Runyu-Shangquan](Slides/021220-Janus-TASO.pptx) | [Runyu-Shangquan](Summaries/021220-Janus-TASO.pdf)
|         | [TASO: Optimizing Deep Learning Computation with Automated Generation of Graph Substitutions](http://web.eecs.umich.edu/~mosharaf/Readings/TASO.pdf)
| Feb 17  | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/TVM.pdf) | [Jingyuan-Yuze](Slides/021720-TVM-Lara.pptx) | Hengjia-Jiaqing
|         | [An Intermediate Representation for Optimizing Machine Learning Pipelines](http://web.eecs.umich.edu/~mosharaf/Readings/IR-Pipeline.pdf)
|         | **Serving Systems and Inference**
| Feb 19  | [Pretzel: Opening the Black Box of Machine Learning Prediction Serving Systems](http://web.eecs.umich.edu/~mosharaf/Readings/Pretzel.pdf) | Chris-Jiachen-Xiangfeng | Alexandra-Wenyi
|         | [Parity Models: Erasure-Coded Resilience for Prediction Serving Systems](http://web.eecs.umich.edu/~mosharaf/Readings/ParM.pdf)
| Feb 24  | [GRNN: Low-Latency and Scalable RNN Inference on GPUs](http://web.eecs.umich.edu/~mosharaf/Readings/GRNN.pdf) | Adam-Mihir | Jiho-Matthew-Zineb
|         | [Nexus: A GPU Cluster Engine for Accelerating DNN-Based Video Analysis](http://web.eecs.umich.edu/~mosharaf/Readings/Nexus.pdf)
| Mar 9   | **Mid-Semester Presentations**
| Mar 11  | **Mid-Semester Presentations**
|         | **Hyperparameter Tuning**
| Mar 16  | [Google Vizier: A Service for Black-Box Optimization](http://web.eecs.umich.edu/~mosharaf/Readings/Vizier.pdf) | Jiho-Matthew-Zineb | Adam-Mihir
|         | [Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization](http://web.eecs.umich.edu/~mosharaf/Readings/HyperBand.pdf)
|         | **Testing and Verification**
| Mar 18  | [DeepXplore: Automated Whitebox Testing of Deep Learning Systems](http://web.eecs.umich.edu/~mosharaf/Readings/DeepXplore.pdf) | Jingyuan-Yuze | Chris-Jiachen-Xiangfeng
|         | [DeepBase: Deep Inspection of Neural Networks](http://web.eecs.umich.edu/~mosharaf/Readings/DeepBase.pdf)
|         | **ML Systems in Practice**
| Mar 23  | [Analysis of Large-Scale Multi-Tenant GPU Clusters for DNN Training Workloads](http://web.eecs.umich.edu/~mosharaf/Readings/Fiddle-Philly.pdf) | Alexandra-Wenyi | Alexandra-Wenyi
|         | [TFX: A TensorFlow-Based Production-Scale Machine Learning Platform](http://web.eecs.umich.edu/~mosharaf/Readings/TFX.pdf)
| Mar 25  | [Applied Machine Learning at Facebook: A Datacenter Infrastructure Perspective](http://web.eecs.umich.edu/~mosharaf/Readings/FB-ML.pdf) | Runyu-Shangquan | Hengjia-Jiaqing
|         | [Machine Learning at Facebook: Understanding Inference at the Edge](http://web.eecs.umich.edu/~mosharaf/Readings/FB-ML-Edge.pdf)
|         | **Scheduling and Resource Management**
| Mar 30  | [Tiresias: A GPU Cluster Manager for Distributed Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Tiresias.pdf) | Juncheng (Guest Lecture) | Chris-Jiachen-Xiangfeng
|         | [Gandiva: Introspective Cluster Scheduling for Deep Learning](http://web.eecs.umich.edu/~mosharaf/Readings/Gandiva.pdf)
| Apr 1   | [Salus: Fine-Grained GPU Sharing Primitives for Deep Learning Applications](http://web.eecs.umich.edu/~mosharaf/Readings/Salus.pdf) | Peifeng (Guest Lecture) | Jingyuan-Yuze
|         | [SuperNeurons: Dynamic GPU Memory Management for Training Deep Neural Networks](http://web.eecs.umich.edu/~mosharaf/Readings/SuperNeurons.pdf)
|         | **Emerging Hardware**
| Apr 6   | [In-Datacenter Performance Analysis of a Tensor Processing Unit](http://web.eecs.umich.edu/~mosharaf/Readings/TPU.pdf) | Adam-Mihir | Runyu-Shangquan
|         | [Serving DNNs in Real Time at Datacenter Scale with Project Brainwave](http://web.eecs.umich.edu/~mosharaf/Readings/Brainwave.pdf)
|         | **ML for Systems**
| Apr 8   | [Neural Packet Classification](http://web.eecs.umich.edu/~mosharaf/Readings/NeuroCuts.pdf) | Xiangfeng | Jingyuan-Yuze
|         | [Learning Scheduling Algorithms for Data Processing Clusters](http://web.eecs.umich.edu/~mosharaf/Readings/Decima.pdfwenb)
| Apr 13  | **Wrap Up** | Mosharaf
| Apr 15  | **Final Presentations <br \>3-5 PM @ Tishman Hall** |

## Policies

### Honor Code
[The Engineering Honor Code](http://honorcode.engin.umich.edu/) applies to all activities related to this course.

### Groups
All activities of this course will be performed in **groups of 2-3 students**.

[Declare your group's membership and paper preferences](https://forms.gle/YrrMqnWsBRFfcr9s8) by January 20, 2020. 
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

A key part of participation will be in the form of discussion in piazza.
The group in charge of the summary should initiate the discussion and the rest should participate.
Not everyone must have add something every day, but it is expected that everyone has something to say over the semester.

### Project
You will have to complete substantive work an instructor-approved problem and have original contribution.
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work.
You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Form a group of 2-3 members by **January 20**.
* Turn in a 2-page draft proposal (including references) by **January 31**. Remember to include the names and Michigan email addresses of the group members. Schedule a 15-minute meeting to pitch your idea and to get early feedback.
* Keep revising your initial idea and incorporate instructor feedback. However, your project proposal must be finalized and approved on or before **February 14**.
* Each group must present mid-semester progress during class hours on **March 9 and March 11**.
* Each group must present their final results during a presentation or poster session on **April 15**.
* Each group must turn in an 8-page final report and your code via email **on or before 11:59PM EST on April 21.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.

## Grading
|                         | Weight | 
| ------------------------| ------:| 
| Paper Summary           | 20%    | 
| Paper Presentation      | 20%    | 
| Participation           | 10%    | 
| Project                 | 50%    | 

