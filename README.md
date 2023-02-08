# Assignment 6:
	Create a snake-like robot with a randomized body in one dimension and with color-coded, randomized sensor placement.

# Running Instructions:
	Open search.py and run program.

# Essential Code:
	In solution.py's Create_Body method, the number of links is randomized such that the robot will be between 5-11 links long. The robot 
	is built along the positive x-axis, with each joint placed in the center of the previous link. Each link has a randomized size in each 
	direction, and each joint is revolute with movement along the x-z plane. The color of each link is decided by a 50/50 coin toss, and 
	if the link is green, it will be stored in a sensor dictionary; every joint receives a motor neuron. These two dictionaries are then 
	called in Create_Brain, and the respective neurons are added. Synapses are added between each sensor and motor neuron. 

# Result:
	The resulting robots show small movements with a "wiggle"-like disposition.

	The following link shows various generations of the randomized snake-bodied robots: 

# Acknowledgements:
	This assignment was performed for Sam Kriegman's Artificial Life class at Northwestern University. It is based off of Josh Bongard's 
	reddit-based MOOC called 'Ludobots'. Special thanks go out to Donna Hooshmand and the rest of the students in the class for 
	their help in office hours and on Campuswire. 