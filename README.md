# Final Project:
### Task:
Optimize morphology and behavior for a task of your choice.

###	Running Instructions:
To run the evolution, open `search.py`. To specify which simulation to run (control or experiment), follow the directions located in the comments in `search.py`.
To generate the fitness curves, open and start `finalProjectFitnessPlots.py`.

### Preview:
The goal of this project is to determine the effect of hidden neuron layers on the performance and evolution of a randomized robot.

![Final_Project_GIF](https://user-images.githubusercontent.com/122194228/223633219-db4ea32a-dbff-46a5-bbe8-7eb89d12c35f.gif)



# Environment:
- OS: Windows
- IDE: Sublime Text
- Language: Python 3
- Physics Engine: `pybullet`
- Simulator: `pyrosim.pyrosim`



# Robot Basics:
###	Genotype:
The genotype of the robot dictates that the rootlink grows two recursive legs in three-dimensional space. 

The following picture shows the genotype graph:

![Assignment_Seven_Robot_Genotype_Graph](https://user-images.githubusercontent.com/122194228/219932836-4f015801-6408-4898-9aba-c6cb0faf3902.JPG)

### 	Ontology:
In solution.py, the robot is generated from a rootlink of fixed size and position, where two legs grow from the rootlink origin. Each leg consists of randomly-sized links connected by center-placed, revolute joints with randomized axis. The legs are symmetrical across the X-Z plane, and they grow in the positive-Z, negative-X, and positive- or negative-Y directions. Each link is randomly assigned either a green color, indicating the presence of a sensor neuron, or a blue color, indicated no neurons. 

The following images shows a diagram of the robot's ontology and an example of a randomized robot:

![Assignment_Seven_Robot_Ontology](https://user-images.githubusercontent.com/122194228/219932846-be060de1-5ed7-4147-8ea5-e90f0a39a56c.JPG)

![Assignment_Seven_Robot_Example](https://user-images.githubusercontent.com/122194228/219933332-d1d2acd7-bc41-434b-92b1-8a95ca796876.JPG)

###	Neural Network:
The neural network is constructed with one layer of touch sensor neurons (one sensor neuron per green link) and one layer of motor neurons (one motor neuron per joint). The control group has no hidden neuron layers, and the experimental group has three hidden neuron layers (see below 'TEST' Section for diagrams). Every neural network generated is fully-integrated. 

###	Evolutionary Algorithm:
The evolutionary algorithm utilized is the ['parallel hillclimber'](https://en.wikipedia.org/wiki/Hill_climbing) as taught in Josh Bongard's [reddit-based 'Ludobots' MOOC](https://www.reddit.com/r/ludobots/). For this project, 25 different parents will be tested against 25 children mutated from their respective parents. If a child performs better than its parent, it will replace the parent in the next generation. The algorithm will perform over 200 generations. 

### Mutation Function: 
The randomized robots mutate by random choice of the following choices:
- 25% : Adjust sensor placement and mutate synapse weights
- 25% : Add a link to the end of each arm and mutate synapse weights
- 25% : Change the joint axis for one joint on each arm and mutate synapse weights
- 25% : Mutate synapse weights

### Fitness Definition:
Locomotion in the -x direction. If a child moves further in the -x direction, it will replace its parent. 



# Test:
### Question:
Will a randomized robot with hidden neuron layers perform locomotion in a specified direction (-x) better than a randomized robot with no hidden neuron layers? How does the presence of hidden neuron layers affect the evolution of a randomized robot? 

### Hypothesis:
The randomized robot with hidden neuron layers will move further in a specified direction (-x) than a randomized robot with no hidden neuron layers. The evolved randomized robots will differ in structure based upon the presence or absence of hidden neuron layers.

### Control:
The control group for this project is a randomized robot with no hidden neuron layers. The following diagram shows the control group's fully-integrated neural network. 

![Assignment_Eight_Neural_Network](https://user-images.githubusercontent.com/122194228/221723846-f64d6eda-c2ab-4d65-8238-eea1ad40fc5e.JPG)

### Experimental:
The experimental group for this project is a randomized robot with three hidden neuron layers. The number of hidden neurons per hidden neuron layer was set to equal the number of sensor neurons [1]. The following diagram shows the experimental group's fully-integrated neural network.

![FP_Exp_Neural_Network](https://user-images.githubusercontent.com/122194228/222880017-e9119ed7-b6d3-49a0-bbda-d0fdb9b9a6be.JPG)

### Testing Parameters:
- Population Size = 25
- Number of Generations = 200
- Number of Robots per Generation = 5000
- Number of Timesteps = 1500
- Number of Seeds/Tests = 5
- Total Simulations = 50,000



# Results:
## Fitness Curves:
For each generation, the randomized robot with the best fitness was plotted on the fitness curve for each seed. Total before and after fitness values can be found in the folders `finalProjectFiles_CONTROL` and `finalProjectFiles_EXPERI`. The following plot shows the fitness curves.

![FP_Fitness_Plot](https://user-images.githubusercontent.com/122194228/223331198-8da7723e-5ae1-4976-9ea3-1b02700aa2b2.png)

### Findings & Discussion:
The final fitnesses did not show any significant difference between the performance of the control and experimental groups. The robots did mutate in different manners as hypothesized and seen by a comparison between the final parents. Qualitatively, the experimental groups showed more control in their motor functions compared to the control group. Additionally, the experimental group's best robots showed more symmetrical movements of their two arms compared to a more oscillating arm behavior by the control group. Given that the time steps were set relatively low at 1500 steps, I hypothesize that the deep neural network made up of the three hidden layers did not have adequate time to adequately learn abstract concepts related to locomotion. Further experiments could explore this by running the same test at time steps near 20,000 or higher. 

### Results Video:
This [2-minute video](https://www.youtube.com/watch?v=etbkn_yEEDE) shows the animated results of the test. *MAKE THE VIDEO A URL*

### B-Roll:
This [1.5-minute video](https://www.youtube.com/watch?v=QLehORyXbzY) shows further animated results from the test. *MAKE THE VIDEO A URL*

### Going Forward:
- Increase number of generations
- Increase time steps
- Expand possible mutations
- Investigate the timing of mutations (for example, mutate the body during early generations and the brain in later generations)
- Explore symmetric synapses to match symmetric body



# Acknowledgements:
- This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University in the Winter 2023 quarter. 
- It is based off of Josh Bongard's reddit-based MOOC called 'Ludobots'. 
- Special thanks to Sunyang Xu and the rest of the students on Campuswire for their help throughout the course.
- The biggest thanks goes to Donna Hooshmand who always expressed enthusiasm and interest in every idea, question, and bug we presented throughout the quarter. TA of the year!!!

### Sources:
[1] https://www.r-bloggers.com/2015/09/selecting-the-number-of-neurons-in-the-hidden-layer-of-a-neural-network/#:~:text=The%20most%20common%20rule%20of,number%20is%20greater%20than%201).

