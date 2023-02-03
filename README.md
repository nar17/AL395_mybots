# AL395_mybots
# For Assingment 5, I set out to create a mini-putt robot. 
# The robot is contructed of three links, the torso, the arm, and the club. It has two joints, one revolute joint between the torso and the arm and one fixed joint between the arm and the club. 
# I added the state of the world, mass patch, and sphere patch. 
# For the world, I created a mini putt course with a hole at the end and a sphere set right in front of robot's club.
# The fitness function reads the x position of the sphere, and it's goal is to land closest to the hole's x-coordinate.
#
# Takeaways:
#	- I'm damn proud I was able to achieve this assignment with its minimal instructions, and I'm thankful for those who helped me through it.
#	- I set the motor max force very high, which simulates a golfer because when they are putting, they have to use much less swing force than their capability.
#	- Since the robot is looking for a fixed desired angle for the joint, it acts more like a hockey player shooting the puck than a golfer winding back and swinging. 
#			- To fix this, I would try to incorporate an oscillating sinusoidal movement for the club that only has a frequency of 1 and an offset that makes sure it winds back and then swings forward to hit the golf ball.
#
# Ways to make it better:
#	- add a joint on the torso which would simulate the hips of a real golfer.
#	- sinusoidal motion of club
#	- add friction to golf ball and mini-putt course
#	- things to randomize: max force of motor, motor joint range, mass of sphere, numSteps