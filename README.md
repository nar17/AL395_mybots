# Assignment 7:
Expand the morphospace from assignment 6 and create randomly generated robots in multiple dimensions.

# 	Running Instructions:
Open search.py and run program.

# 	Essential Code:
In solution.py's Create_Body method, the number of links is randomized such that the robot will be between 5-11 links long. The robot is built along the positive x-axis, with each joint placed in the center of the previous link. Each link has a randomized size in each direction and randomized mass, and each joint is revolute with movement along the x-z plane. The color of each link is decided by a 50/50 coin toss, and if the link is green, it will be stored in a sensor dictionary; every joint receives a motor neuron. These two dictionaries are then called in Create_Brain, and the respective neurons are added. Synapses are added between each sensor and motor neuron. 

The following image shows an example of a randomized snake robot:

![Random_Snake_Screenshot](https://user-images.githubusercontent.com/122194228/217650570-47537373-2a6f-4da9-b711-91a382f188aa.JPG)

# 	Result:
The resulting robots show small movements with a "wiggle"-like disposition.

The following Youtube link shows various generations of the randomized robots: 



The following Github link shows the full code repository: 
https://github.com/nar17/AL395_mybots/tree/assignmentSEVEN

# 	Acknowledgements:
This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University in the Winter 2022 quarter. It is based off of Josh Bongard's reddit-based MOOC called 'Ludobots'. Special thanks to Donna Hooshmand and the rest of the students for their help in office hours and on Campuswire. 
