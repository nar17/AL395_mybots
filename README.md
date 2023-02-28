# Assignment 8:
Utilize the parallel hillclimber algorithm to design morphology and behavior for locomotion.


# 	Running Instructions:
To run the evolution, open and start search.py.
To generate the fitness curves, open and start EightFitnessPlots.py.


#	Genotype:
The genotype of the robot dictates that the rootlink grows two recursive legs in three-dimensional space. 

The following picture shows the genotype graph:

![Assignment_Seven_Robot_Genotype_Graph](https://user-images.githubusercontent.com/122194228/219932836-4f015801-6408-4898-9aba-c6cb0faf3902.JPG)


# 	Ontology:
In solution.py, the robot is generated from a rootlink of fixed size and position, where two legs grow from the rootlink origin. Each leg consists of randomly-sized links connected by center-placed, revolute joints with randomized axis. The legs are symmetrical across the X-Z plane, and they grow in the positive-Z, negative-X, and positive- or negative-Y directions. Each link is randomly assigned either a green color, indicating the presence of a sensor neuron, or a blue color, indicated no neurons. 

The following images shows a diagram of the robot's ontology and an example of a randomized robot:

![Assignment_Seven_Robot_Ontology](https://user-images.githubusercontent.com/122194228/219932846-be060de1-5ed7-4147-8ea5-e90f0a39a56c.JPG)

![Assignment_Seven_Robot_Example](https://user-images.githubusercontent.com/122194228/219933332-d1d2acd7-bc41-434b-92b1-8a95ca796876.JPG)


#	Neural Network:
The neural network is constructed with one layer of sensor neurons and one layer of motor neurons. The sensor neurons detect touch and are located in green links (one sensor neuron per green link). The motor neurons are located on every joint (one motor neuron per joint). 

The fully-integrated neural network is shown in the figure below: 

![Assignment_Eight_Neural_Network](https://user-images.githubusercontent.com/122194228/221723846-f64d6eda-c2ab-4d65-8238-eea1ad40fc5e.JPG)


#	Evolutionary Algorithm:
The evolutionary algorithm utilized is the 'parallel hillclimber' as taught in Josh Bongard's 'Ludobots' MOOC. Each parent's brain was mutated by assigning random weights to each synapse in the fully-integrated neural network. The body was mutated by a random choice between changing one sensor neuron location, changing one joint's axis, or adding an extra link of random size to each leg. If the child performs better in terms of -x movement fitness it will replace its parent. This algorithm was run with a population size of 10 over 50 generations. 


#	Fitness Curves:
The fitness definition was movement in the -x direction. The best fitness out of the population for each generation was plotted on the fitness curve, and the simulation was run with five different seeds.

The fitness curve plot is shown in the figure below: 

![Assignment_Eight_Robot_Evolution_Fitness_Curves](https://user-images.githubusercontent.com/122194228/221723812-ada48555-33b5-4785-a45c-00be3602b9bc.jpg)


# 	Results:
The resulting robots loosely resemble a boxer with muscular arms and no legs; their movements are varied based upon the randomized placement of the sensor neurons.

The following Youtube link shows one example of the evolution of one random robot: 

The following Github link shows the full code repository: https://github.com/nar17/AL395_mybots/tree/assignmentEIGHT


# 	Acknowledgements:
This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University in the Winter 2023 quarter. It is based off of Josh Bongard's reddit-based MOOC called 'Ludobots'. Special thanks to Donna Hooshmand and the rest of the students for their help in office hours and on Campuswire. 

