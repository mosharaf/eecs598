# EECS598 Assignment: PyTorch

### *Gain a hands-on understanding of PyTorch on CloudLab*
##

### Due: Mar 7, 2021, 11:59 PM

## Overview
[PyTorch](https://pytorch.org/) is an open source machine learning library. It provides an imperative and Pythonic programming style that supports code as a model,
makes debugging easy and is consistent with other popular scientific computing libraries, while remaining efficient and supporting 
hardware accelerators such as GPUs \[[1](#bibliography)\]. It helps define a neural network computation as a data-flow graph, including 
the ability to place the operations across machines and across multiple computational within a machine.

Use the `pytorch-cluster` profile under `Michigan-BigData` project to start your experiment,
and follow the CloudLab usage policies mentioned in [Starting with Cloudlab](Starting\ with\ Cloudlab/README.md).

In this assignment, you will be given a machine learning workload written in PyTorch.
You will setup a 3-node cluster. After filling in the necessary code in the starter file, run workloads on a single machine first. 
You will be asked to do some profiling to get familiar with the execution profile of PyTorch. The next task is to modify the code so that it can be launched in a distributed way. 
We will provide you with detailed instructions on how to do it, but do keep in mind that PyTorch has a steep learning curve, 
and there are many low-level APIs that you may want to get familiar with when doing this assignment. 
The information provided in this spec is limited, so you should find more tutorials online (for example, in the official documentation) whenever you feel it is needed.

## Learning Outcomes
After completing this programming assignment, students should be able to:

* Describe how PyTorch operates at a high level and how its frequently used APIs work.
* Deploy a small PyTorch cluster to run machine learning training in a distributed way.
* Distribute a single-machine PyTorch workload into the cluster you deploy.

## Overall Architecture

In this section, we give a brief introduction of the overall architecure of the workload at a high level. You are encouraged to read more elsewhere (official documentation, papers, etc.) to consolidate your understanding of PyTorch.
To define the PyTorch workload, the evaluation of the neural network is described in an imperative fashion using PyTorch operators, while building the computation graph by encapsulating resulting tensors with metadata. This metadata
is used in the backward pass to generate the differential for every parameter, thus defining the computation for the updates. In a single-machine scenario, neither the training data nor the parameters are communicated externally.

There are multiple ways to conduct distributed training in PyTorch. In a parameter server architecture, multiple nodes communicate with a centralized node to send updates and receive updated parameters.

![parameterserver-architecture](./cluster.png)

In the distributed setting followed in this assignment, all nodes retain copies of the entire dataset but iterate on disjoint subsets. The updates to parameters are broadcasted to all nodes, applying all
of the updates to maintain a consistent set of parameters.

![allreduce-architecture](./all_reduce.png)

**Question 1.** When would you want to use a parameter-server based centralized architecture over the above described decentralized architure?

## Environment Setup

Once the machines according to the `pytorch-cluster` profile are setup, follow the steps to install PyTorch and setup the environment.

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh # You could use other shells too
./anaconda3/bin/conda init bash # Or your favorite shell
./anaconda3/bin/conda create -n pytorch_env pytorch torchvision torchaudio -c pytorch
./anaconda3/bin/conda activate pytorch_env
./anaconda3/bin/conda install -c conda-forge tensorboard
```

Restart the shell (`bash` in this case) to use `conda` instead of `./anaconda3/bin/conda`.

### Task 1: PyTorch in A Single Node

In this task, you will be completing the definition of the training loop to run a 6-layer neural network on a single machine.
The starter python file is available at `/proj/michigan-bigdata-PG0/assignments/p0.py`.
Once you have completed the code headlined by the comment "Task 1", start the workload using,
```
python p0.py
```

Using the default command line hyper-parameters, answer the following questions:

**Question 2.** What is the completion time of the training task? Record the CPU usage and memory usage with time when the program is running.
Use your favorite software tool to generate one plot for CPU usage and one plot for memory usage. Explain the resource usage pattern(s). 

**Question 3.** Repeat the training process in Question 2, with checkpointing enabled. Record the completion time. Explain the effect of checkpointing on the run-time. You only need the checkpointing setting in this question throughout the entire assignment.

**Question 4.** Benchmark the training process from Question 2 at batch sizes 32 and 256. Explain the results you observe (Hint: cpu usage). For this question, also generate the CPU and memory plots. (Optional) Explain the effect on network convergence.

**Question 5.** [TensorBoard](https://www.tensorflow.org/get_started/graph_viz) is a suite of visulization tools to created to help visualize the training process.
Originally designed for TensorFlow, it has been [ported to PyTorch](https://pytorch.org/docs/stable/tensorboard.html). Use TensorBoard to visualize the graph created in the training process you just ran.
The necessary logging has already been included in the code we provide you, so you simply [launch TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard) to view the graph.
Keep a screenshot of the graph for submission.

### Task 2: Distributed PyTorch

As mentioned earlier, your main goal in this task is to figure out a way to train the model in a distributed fashion.
To be specific, you will complete the tasks headlined with the comment "Task 2" in the starter code and follow the instructions.
To start the i-th worker on the i-th node in a 3 node cluster,

```bash
user@nodei: $ python p0.py -n 3 -np 1 -nr i
```

Answer the following questions after you finish implementing the distributed version.

**Question 6.** Run the distributed model with 1, 2 and 3 worker nodes. 
Record the completion time of the task on the master node and compare with the result you get in Question 2. Consider what batch size you should set for a fair comparison.
Also plot CPU and memory usage for your master server node. Keep a screenshot of the graphs visulized by TensorBoard for submission.

**Question 7.** Repeat Question 2 using 2 processes per worker. Explain the performance difference between the case with 1 and 2 worker processes. You will need to submit the CPU and memory plots.

**Question 8. (Optional)** Did you find any difference between the convergence rates in the distributed and single machine case?
If so, can you explain the difference in the rates with respect to the system architecture?

**Question 9. (Optional)** How many hours have you spent in this assignment?

## Submission Instructions
Email a tar.gz file to `eecs598-bigdata-staff@umich.edu` with the following,

1. Modified started code used in this assignment.
2. PDF with answers, ascreenshots and plots.

## Competetion (Bonus)

### Due Apr 25, 2021, 11:59 PM

Students can participate in a competetion for bonus points, by optimizing the application according to the below objective while following a set of constraints. The fastest code will receive 5 extra points.

**Objective**: Minimize run-time to a acheive 90 % validation accuracy.

**Constraints**:

1. The model can be trained for a maximum of 40 epochs.
2. You must use only CPUs to train.
3. You can use a maximum of 3 nodes to train.

**Submission**: Send screenshots of the run-time and accuracy posted on all nodes and your code zipped into a tar.gz file to `eecs598-bigdata-staff@umich.edu`. We will update the scoreboard on a weekly basis. 

## Acknowledgements

This assignment was adapted from Yiwen Zhang's work for a previous offering of the course.

## Bibiliography

1. [PyTorch: An Imperative Style, High-Performance Deep Learning Library](https://arxiv.org/abs/1912.01703)
