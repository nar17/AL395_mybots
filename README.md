# Assignment 7:
Expand the morphospace from assignment 6 and create randomly generated robots in multiple dimensions.


# 	Running Instructions:
Open search.py and run program.


#	Genotype:
The genotype of the robot is represented by the following graph. The rootlink has the potential to grow up to four legs, and each leg can be 2-3 links long. 

The following picture shows the genotype graph:

![Random_Snake_Screenshot](https://user-images.githubusercontent.com/122194228/217650570-47537373-2a6f-4da9-b711-91a382f188aa.JPG)


# 	Ontology:
In solution.py, the robot is generated from a rootlink of fixed size and position. There is a 50% probability of the robot growing a "leg" in any of the +y, -y, -x, and +z direction. Each of these legs will consist of 2-3 links of random size. Each link is connected to the previous link at its center with a revolute joint that has a randomized axis. Every link has a 50% probability of being green or blue. Green links have a touch sensor neuron, blue links have no neuron, and every joint has a motor neuron. 

The following images shows a diagram of the robot's ontology and an example of a randomized robot:

![Random_Snake_Screenshot](https://user-images.githubusercontent.com/122194228/217650570-47537373-2a6f-4da9-b711-91a382f188aa.JPG)	![Random_Snake_Screenshot](https://user-images.githubusercontent.com/122194228/217650570-47537373-2a6f-4da9-b711-91a382f188aa.JPG)


#	Neural Network:
The neural network is constructed with one layer of sensor neurons, one layer of hidden neurons, and one layer of motor neurons. The sensor neurons detect touch and are located in green links (one sensor neuron per green link). The motor neurons are located on every joint (one motor neuron per joint). Based upon Sandhya Krishnan's Medium post from September 2021 [1], the number of hidden neurons is a randomly selected integer between the number of sensors neurons and the number motor neurons.

The fully integrated neural network is shown in the figure below: 


# 	Result:
The resulting robots show small movements with a "wiggle"-like disposition.

The following Youtube link shows various generations of the randomized robots: 
https://github.com/nar17/AL395_mybots/tree/assignmentSEVEN

The following Github link shows the full code repository: 
https://github.com/nar17/AL395_mybots/tree/assignmentSEVEN


# 	Acknowledgements:
This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University in the Winter 2022 quarter. It is based off of Josh Bongard's reddit-based MOOC called 'Ludobots'. Special thanks to Donna Hooshmand and the rest of the students for their help in office hours and on Campuswire. 


#	Sources:
[1] https://medium.com/geekculture/introduction-to-neural-network-2f8b8221fbd3
