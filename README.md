# Assignment 7:
Expand the morphospace from assignment 6 and create randomly generated robots in multiple dimensions.


# 	Running Instructions:
Open search.py and run program.


#	Genotype:
The genotype of the robot dictates that the rootlink grows two recursive legs in three-dimensional space. 

The following picture shows the genotype graph:

![Assignment_Seven_Robot_Genotype_Graph](https://user-images.githubusercontent.com/122194228/219932836-4f015801-6408-4898-9aba-c6cb0faf3902.JPG)


# 	Ontology:
In solution.py, the robot is generated from a rootlink of fixed size and position. From the rootlink, two legs grow from the rootlink origin. Each leg consists of randomly-sized links connected by center-placed, revolute joints with randomized axis. The legs are symmetrical across the X-Z plane, and they grow in the positive-Z, negative-X, and positive- or negative-Y directions. Each link is randomly assigned either a green color, indicating the presence of a sensor neuron, or a blue color, indicated no neurons. 

The following images shows a diagram of the robot's ontology and an example of a randomized robot:

![Assignment_Seven_Robot_Ontology](https://user-images.githubusercontent.com/122194228/219932846-be060de1-5ed7-4147-8ea5-e90f0a39a56c.JPG)


#	Neural Network:
The neural network is constructed with one layer of sensor neurons, one layer of hidden neurons, and one layer of motor neurons. The sensor neurons detect touch and are located in green links (one sensor neuron per green link). The motor neurons are located on every joint (one motor neuron per joint). Based upon Sandhya Krishnan's Medium post from September 2021 [1], the number of hidden neurons is a randomly selected integer between the number of sensor neurons and the number motor neurons.

The fully-integrated neural network is shown in the figure below: 

![Assignment_Seven_Neural_Network](https://user-images.githubusercontent.com/122194228/219932849-807318e8-3719-4c93-b9ce-182ba16bedb1.JPG)


# 	Result:
The resulting robots loosely resemble a boxer with muscular arms and no legs; their movements are varied based upon the randomized placement of the sensor neurons. 

The following Youtube link shows various generations of the randomized robots: 
https://github.com/nar17/AL395_mybots/tree/assignmentSEVEN

The following Github link shows the full code repository: 
https://github.com/nar17/AL395_mybots/tree/assignmentSEVEN


# 	Acknowledgements:
This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University in the Winter 2022 quarter. It is based off of Josh Bongard's reddit-based MOOC called 'Ludobots'. Special thanks to Donna Hooshmand and the rest of the students for their help in office hours and on Campuswire. 


#	Sources:
[1] https://medium.com/geekculture/introduction-to-neural-network-2f8b8221fbd3
