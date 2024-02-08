# EECS 598: Systems for Generative AI (W'24)

## Administrivia
* Catalog Number: 34478
* Lectures/Discussion: 133 CHRYS, TTh: 10:30 AM – 12:00 PM
* Projects/Makeup: 1610 IOE, F 1:30 PM – 2:30 PM
* Counts as: Software Depth (PhD); Technical Elective and 500-Level (MS/E)

### Team

| Member (uniqname) | Role | Office Hours |
| :---------------- | :--- | :----------- |
| [Mosharaf Chowdhury](http://www.mosharaf.com/) (mosharaf) | Faculty | 4820 BBB. **By appointments only.**
| [Jiachen Liu](https://websites.umich.edu/~amberljc/) (amberljc) | GSI | 4828 BBB. F 12:30 - 1:30 PM

### Piazza
**ALL** communication regarding this course must be via [Piazza](https://piazza.com/umich/winter2024/eecs598004w24/).
This includes questions, discussions, announcements, as well as private messages.

Presentation slides and paper summaries should be emailed to [eecs598-genai-staff@umich.edu](mailto:eecs598-genai-staff@umich.edu).

## Course Description
This class will introduce you to the key concepts and the state-of-the-art in practical, scalable, and fault-tolerant software systems for emerging Generative AI (GenAI) and encourage you to think about either building new tools or how to apply an existing one in your own research.

Since datacenters and cloud computing form the backbone of modern computing, we will start with an overview of the two. 
We will then take a deep dive into systems for the Generative AI landscape, focusing on different types of problems. 
Our topics will include: basics on generative models from a systems perspective; systems for GenAI lifecycle including pre-training, fine-tuning/alignment, grounding, and inference serving systems; etc. 
We will cover GenAI topics from top conferences that take a systems view to the relevant challenges.

Note that this course is **NOT focused on AI methods**. 
Instead, we will *focus on how one can build software systems* so that existing AI methods can be used in practice and new AI methods can emerge. 

### Prerequisites
Students are expected to have good programming skills and must have taken *at least one* undergraduate-level systems-related course (from operating systems/EECS482, databases/EECS484, distributed systems/EECS491, and networking/EECS489).
Having an undergraduate ML/AI course may be helpful, but not required or necessary. 

### Textbook
This course has no textbooks.
We will read recent papers from top venues to understand trends in GenAI systems and their applications.

## Tentative Schedule and Reading List
*This is an evolving list and subject to changes due to the breakneck pace of GenAI innovations.* 

| Date    | Readings                       | Presenter | Summary | Reviewer
| --------| -------------------------------| --------- | ------- | -------
| Jan 11  | **Introduction** | [Mosharaf](Slides/011124-MChowdhury.pdf)
|         | [How to Read a Paper](http://svr-sk818-web.cl.cam.ac.uk/keshav/papers/07/paper-reading.pdf) (Required)
|         | [How to Give a Bad Talk](http://www.cs.berkeley.edu/~pattrsn/talks/BadTalk.pdf) (Required)
|         | [Writing Reviews for Systems Conferences](http://people.inf.ethz.ch/troscoe/pubs/review-writing.pdf)
|         | [The Datacenter as a Computer](https://link.springer.com/book/10.1007/978-3-031-01761-2) (Chapters 1 and 2)
|         | **GenAI Basics**
| Jan 16  | [Challenges and Applications of Large Language Models](https://arxiv.org/abs/2307.10169) | [Jiachen](Slides/011624-LLMSys-JLiu.pdf) | - 
|         | [Attention Is All You Need](https://dl.acm.org/doi/10.5555/3295222.3295349)
|         | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (Required)
|         | [The Transformer Family Version 2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/)
| Jan 18  | [High-Resolution Image Synthesis With Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | [Jiachen](/Slides/011824-CLIP-Jiachen.pptx), [Yuxuan](/Slides/011824-Diffusion-Yuxuan.pptx) | [Ari, Jack, Vishwa](/Summaries/011824-Diffusion-CLIP.pdf)
|         | [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125)
|         | [Adding Conditional Control to Text-to-Image Diffusion Models](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html)
|         | [CLIP: Connecting Text and Images](https://openai.com/research/clip) (Required)
|         | [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) (Required)
| Jan 23  | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)  | [Shiqi, Aakash, Yong](/Slides/012324-LVLM.pptx) | [Yuxuan, Daniel, Oh Jun](/Summaries/012324-Multimodal.pdf)
|         | [DeepSpeed-VisualChat: Multi-Round Multi-Image Interleave Chat via Multi-Modal Causal Attention](https://arxiv.org/abs/2309.14327)
|         | [Flamingo: a Visual Language Model for Few-Shot Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html)
|         | [Multimodality and Large Multimodal Models (LMMs)](https://huyenchip.com/2023/10/10/multimodal.html) (Required)
| Jan 25  | [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://dl.acm.org/doi/abs/10.5555/3586589.3586709) | [Ari, Jack, Vishwa](/Slides/012324-MoE.pptx) | [Maya, Aidan, Christopher](/Summaries/012325-MoE.pdf)
|         | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://openreview.net/forum?id=B1ckMDqlg) (Required)
|         | [Scaling Vision-Language Models with Sparse Mixture of Experts](https://arxiv.org/abs/2303.07226)
|         | [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://arxiv.org/abs/2201.05596) (Required)
| Jan 30  | **No Lecture / Work on Project Proposal**
|         | [Worse is Better](https://en.wikipedia.org/wiki/Worse_is_better) (Required)
|         | [Hints and Principles for Computer System Design](https://arxiv.org/abs/2011.02455)
|         | **Pre-Training**
| Feb  1  | [Pathways: Asynchronous Distributed Dataflow for ML](https://proceedings.mlsys.org/paper_files/paper/2022/hash/37385144cac01dff38247ab11c119e3c-Abstract.html) (Required) | [Yuxuan, Finn, Marwa](/Slides/010224-Pathways%20&%20Megatron.pptx) | [Daniel, Norman, Zhixiang](/Summaries/020124-pathway-megatron.pdf) | Maya, Aidan, Christopher
|         | [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://dl.acm.org/doi/10.1145/3458817.3476209) (Required)
| Feb  6  | [Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning](https://www.usenix.org/conference/osdi22/presentation/zheng-lianmin) (Required) | [Insu Jang](/Slides/020624-alpa-oobleck-Insu.pptx) | - | Jiaheng, Jeremy, Zhenning 
|         | [Oobleck: Resilient Distributed Training of Large Models Using Pipeline Templates](https://dl.acm.org/doi/10.1145/3600006.3613152) (Required) |
|         | **Fine Tuning / Alignment**
| Feb  8  | [LoRA: Low-Rank Adaptation of Large Language Models](https://openreview.net/forum?id=nZeVKeeFYf9) (Required) | [Mehar, Parth, Zachary](/Slides/020824-Lora-RLHF.pdf) | Lingxiao, Shoma, Christopher | Leah, Zin, Rabia
|         | [Training Language Models to Follow Instructions with Human Feedback](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) (Required)
|         | [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/abs/2311.03285)
| Feb 13  | [Finetuned Language Models Are Zero-Shot Learners](https://openreview.net/forum?id=gEZrGCozdqR) (Required) | Yash, Aniket	| - | Filippos Bellos, Yayuan Li
|         | [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) (Required)
|         | [A Picture is Worth a Thousand Words: Principled Recaptioning Improves Image Generation](https://arxiv.org/abs/2310.16656)
|         | **Inference**
| Feb 15  | [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) | Daniel, Norman, Zhixiang	| Xueshen, Juechu | Yuxuan, Finn, Marwa
|         | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://dl.acm.org/doi/10.1145/3600006.3613165) (Required)
|         | [Approximate Caching for Efficiently Serving Diffusion Models](https://arxiv.org/abs/2312.04429) (Required)
| Feb 20  | [AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving](https://www.usenix.org/conference/osdi23/presentation/li-zhouhan) (Required) | Luke, Daniel, Oh Jun |	Jiaheng, Jeremy, Zhenning | Shiqi, Aakash, Yong
|         | [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) (Required)
|         | [SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills](https://arxiv.org/abs/2308.16369)
| Feb 22  | **Buffer**
|         | **Grounding**
| Mar  5  | [REALM: Retrieval-Augmented Language Model Pre-Training](https://proceedings.mlr.press/v119/guu20a.html) (Required) | Maya, Aidan, Christopher	| Mehar, Parth, Zachary | Ari, Jack, Vishwa
|         | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/)
|         | [Improving Language Models by Retrieving from Trillions of Tokens](https://proceedings.mlr.press/v162/borgeaud22a.html) (Required)
| Mar  7  | [Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs](https://ieeexplore.ieee.org/abstract/document/8594636) (Required) | Filippos, Yayuan | Yash, Aniket | 
|         | [Billion-Scale Similarity Search with GPUs](https://ieeexplore.ieee.org/document/8733051)
|         | [LightSeq: Sequence Level Parallelism for Distributed Training of Long Context Transformers](https://arxiv.org/abs/2310.03294)
|         | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (Required)
| Mar 12  | **Mid-Semester Presentations**
| Mar 14  | **Mid-Semester Presentations**
|         | **Systems Optimizations**
| Mar 19  | [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://papers.nips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) (Required) | Jiaheng, Jeremy, Zhenning | Leah, Zin, Rabia | Mehar, Parth, Zachary
|         | [Efficiently Scaling Transformer Inference](https://proceedings.mlsys.org/paper_files/paper/2023/hash/523f87e9d08e6071a3bbd150e6da40fb-Abstract-mlsys2023.html) (Required)
|         | [Full Stack Optimization of Transformer Inference: a Survey](https://arxiv.org/abs/2302.14017)
|         | [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)
| Mar 21  | [FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU](https://proceedings.mlr.press/v202/sheng23a.html) (Required) | Xueshen, Juechu | Shiqi, Aakash, Yong | Yash, Aniket
|         | [ZeRO-Infinity: Breaking the GPU Memory Wall for Extreme Scale Deep Learning](https://dl.acm.org/doi/10.1145/3458817.3476205) (Required)
| Mar 26  | [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://openreview.net/forum?id=tcbBPnfwxS) (Required) | Lingxiao, Shoma, Christopher | Yuxuan, Finn, Marwa | Daniel, Norman, Zhixiang
|         | [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://papers.nips.cc/paper_files/paper/2022/hash/c3ba4962c05c49636d4c6206a97e9c8a-Abstract-Conference.html)
|         | [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) (Required)
| Mar 28  | **Buffer**
|         | **Special Topics**
| Apr  2  | [Zeus: Understanding and Optimizing GPU Energy Consumption of DNN Training](https://www.usenix.org/conference/nsdi23/presentation/you) | Jae-Won Chung | - | Yuxuan, Daniel, Oh 
|         | [Perseus: Removing Energy Bloat from Large Model Training](https://arxiv.org/abs/2312.06902) (Required)
|         | [POLCA: Power Oversubscription in LLM Cloud Providers](https://arxiv.org/abs/2308.12908) (Required)
| Apr  4  | [Sociotechnical Safety Evaluation of Generative AI Systems](https://arxiv.org/abs/2310.11986) (Required) |  | Filippos, Yayuan | Lingxiao, Shoma, Christopher
|         | [On the Dangers of Stochastic Parrots: Can Language Models be too Big?🦜](https://dl.acm.org/doi/abs/10.1145/3442188.3445922) (Required)
|         | [Foundation Models and Fair Use](https://arxiv.org/abs/2303.15715)
| Apr  9  | **Buffer**
| Apr 11  | [Extracting Training Data from Large Language Models](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting) (Required) | Leah, Zin, Rabia | Luke | Xueshen, Juechu
|         | [Extracting Training Data from Diffusion Models](https://www.usenix.org/conference/usenixsecurity23/presentation/carlini) (Required)
|         | [Identifying and Mitigating the Security Risks of Generative AI](https://arxiv.org/abs/2308.14840)
| Apr 16  | **Wrap Up** | Mosharaf
|         | [How to Write a Great Research Paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) (Required)
| Apr 18  | **Final Presentations** | 


## Policies

### Honor Code
[The Engineering Honor Code](https://ecas.engin.umich.edu/honor-council/honor-code/) applies to all activities related to this course.

### Groups
All activities of this course will be performed in **groups of 2-3 students**.

### Required Reading
Each lecture will have **two required reading that everyone must read**.  
There will be *one or more optional related reading(s)* that only the presenter(s) should be familiar with.
They are optional for the rest of the class.

### Student Lectures
The course will be conducted as a seminar. 
Only one group will present in each class.
Each group will be assigned *at least one lecture* over the course of the semester. 
Presentations should last **at most 40 minutes** without interruption.
However, presenters should expect questions and interruptions throughout. 

In the presentation, you should:

* Provide necessary background and motivate the problem.
* Present the high level idea, approach, and/or insight (using examples, whenever appropriate) in the required reading as well as the additional reading. 
* Discuss technical details so that one can understand key details without carefully reading.
* Explain the differences between related works.
* Identify strengths and weaknesses of the required reading and propose directions of future research.

*The slides for a presentation must be emailed to the instructor team at least 24 hours prior to the corresponding class.* 
Use Google slides to enable in-line comments and suggestions.

### Lecture Summaries
Each group will also be assigned to **write summaries for at least one lectures**. 
The summary assigned to a group will not be the reading they gave the lecture on.

A paper summary must address the following four questions in sufficient details (2-3 pages):

* What is the problem addressed in the lecture, and why is this problem important?
* What is the state of related works in this topic?
* What is the proposed solution, and what key insight guides their solution?
* What is one (or more) drawback or limitation of the proposal?
* What are potential directions for future research?

*The paper summary of a paper must be emailed to the instructor team within 24 hours after its presentation.* 
**Late reviews will not be counted.** 
You should use [this format](Summaries/Template.md) for writing your summary.
Use Google doc to enable in-line comments and suggestions.

*Allocate enough time for your reading, discuss as a group, write the summary carefully, and finally, include key observations from the class discussion.*

### Post-Presentation Panel Discussion 
To foster a deeper understanding of the papers and encourage critical thinking, each lecture will be followed by a panel discussion. 
This discussion will involve three distinct roles played by different student groups, simulating an interactive and dynamic scholarly exchange.

#### Roles and Responsibilities

1. **The Authors**
- Group Assignment: The group that presents the paper and the group that writes the summary will play the role of the paper's authors.
- Responsibility: As authors, you are expected to defend your paper against critiques, answer questions, and discuss how you might improve or extend your research in the future, akin to writing a rebuttal during the peer-review process.


2. **The Reviewers**
- Group Assignment: Each group will be assigned to one slot to play the role of reviewers.
- Responsibility: Reviewers critically assess the paper, posing challenging questions and highlighting potential weaknesses or areas for further investigation. 
Your goal is to engage in a constructive critique of the paper, simulating a peer review scenario.

 
3. **Rest of the Class**
- Responsibility: 
  - You are required to [submit](https://forms.gle/Us8pr5o4R4TtzMzU7) **one insightful question** for each presented papers before each class. 
  - During the panel discussions, feel free to actively **ask questions** and engage in the dialogue. 
  - After each session, you'll have the opportunity to **[vote](https://forms.gle/7wmVdYmhXR63kFHB9) for your favorite group** based on their performance and contribution to the discussion.
  The group with the most votes will receive a _bonus_ point.

### Participation
Given the discussion-based nature of this course, participation is required both for your own understanding and to improve the overall quality of the course.
You are expected to attend **all** lectures (you may skip up to 2 lectures due to legitimate reasons), and more importantly, participate in class discussions.

A key part of participation will be in the form of discussion in Piazza.
The group in charge of the summary should initiate the discussion and the rest should participate.
Not everyone must have add something every day, but it is expected that everyone has something to say over the semester.

### Project
You will have to complete substantive work an instructor-approved problem and have original contribution.
Surveys are not permitted as projects; instead, each project must contain a survey of background and related work.

You must meet the following milestones (unless otherwise specified in future announcements) to ensure a high-quality project at the end of the semester:

* Form a group of 2-3 members and [declare your group's membership and paper preferences](https://forms.gle/t8n6V9ewJoDWTaSL9) by **January 23**. After this date, we will form groups from the remaining students.
* Turn in a 2-page draft proposal (including references) by **February 9**. Remember to include the names and Michigan email addresses of the group members. 
* Each group must present mid-semester progress during class hours on **March 12 and March 14**.
* Each group must turn in an 8-page final report and your code via email **on or before 6:00PM EST on May 1.** The report must be submitted as a PDF file, with formatting similar to that of the papers you've read in the class. The self-contained (i.e., include ALL dependencies) code must be submitted as a zip file. Each zip file containing the code must include a README file with a step-by-step guide on how to compile and run the provided code.
* You can find how to access GPU resources [here](./Resources/Starting%20with%20Cloudlab).

## Tentative Grading
|                         | Weight | 
| ------------------------| ------:| 
| Paper Presentation      | 15%    | 
| Paper Summary           | 15%    | 
| Participation           | 10%    | 
| Project Report          | 40%    | 
| Project Presentations   | 20%    | 
