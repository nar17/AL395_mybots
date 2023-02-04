# AL395_mybots
#
# Run in search.py
#
# For Assingment 5, I set out to create a mini-putt robot. 
# The robot is contructed of four links, the torso, the hip, the arm, and the club. It has three joints, two revolute joints, torso_arm and torso_hip, and one fixed joint between the arm and the club. 
# I added the state of the world, mass patch, and sphere patch. 
# For the world, I created a mini putt course with a hole at the end (x = -11.5) and a sphere set right in front of robot's club.
# The fitness function reads the x position and y position of the sphere, and it's goal is to land closest to the hole's x-coordinate(-11.5) while minimizing the distance from the y=0.
#
# Takeaways:
#	- I'm damn proud I was able to achieve this assignment with its minimal instructions and this being my first ever coding class, and I'm thankful for those who helped me through it.
#	- I set the motor max force very high, which simulates a golfer because when they are putting, and as such, they have to use much less swing force than their capability.
#	- Since the robot is looking for a fixed desired angle for the joints, it acts more like a hockey player shooting the puck with a wrist shot than a golfer winding back and swinging. 
#			- To make this better, I would try to incorporate an oscillating sinusoidal movement for the club that only has a frequency of 1 and an offset that makes sure it winds back and then swings
#			   forward to hit the golf ball.
#	- I've learned something about fitness. There is a difference between a finite fitness and a continuous fitness. The golf hole is definitely a finite fitness which means that there are abundant
#	  configurations to get the ball in the hole. So, by increasing the evolutions and populations, you aren't necessarily getting to a most optimum golfer. On the contra, when you have a continuous 
#	  fitness, each additional evolution produces a greater chance at reaching a single optimal robot. Perhaps, for future assignments or exploration, it is more interesting (or at least you can get more 
#	  insight), by looking at a continous fitness. An example of a continuous goal for a golfing robot would be how far the robot could drive the ball in a straight line. I added this function; it is 
#	  currently commented out in parallelHillClimber.py as #furthestdrive. 
#
# Ways to make it better:
#	- sinusoidal motion of club
#	- add friction to golf ball and mini-putt course
#	- things to randomize: max force of motor, motor joint range, mass of sphere, numSteps
#	- add a time factor to the movement of the joints, such that the hip joint will move first followed by the arm joint