import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
		self.myID = nextAvailableID
		
		
		
	def Evaluate(self, directOrGUI):
		#self.Create_World()
		#self.Create_Body()
		#self.Create_Brain()
		#self.directOrGUI = directOrGUI
		#os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		#while not os.path.exists("fitness" + str(self.myID) + ".txt"):
		#	time.sleep(0.01)
		#fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		#self.fitness = float(fitnessFile.read())
		#print(self.fitness)
		#fitnessFile.close()
		pass
		

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		self.directOrGUI = directOrGUI
		os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		

	def Wait_For_Simulation_To_End(self, directOrGUI):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.02)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		self.overallFitness = fitnessFile.readlines()
		self.xfitness = float(self.overallFitness[0])
		self.yfitness = float(self.overallFitness[1])
		fitnessFile.close()
		os.system("del fitness" + str(self.myID) + ".txt")
		

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")

			#miniputt platform
		#pyrosim.Send_Cube(name="largeGreen", pos=[0,0,0.5] , size=[16,10,1], mass=1000)
		#pyrosim.Send_Cube(name="preHoleGreen", pos=[-9,0,0.5] , size=[2,6,1], mass=1000)
		#pyrosim.Send_Cube(name="+yBox", pos=[-11.5,2,0.5] , size=[3,2,1], mass=1000)
		#pyrosim.Send_Cube(name="-yBox", pos=[-11.5,-2,0.5] , size=[3,2,1], mass=1000)
		#pyrosim.Send_Cube(name="backstopBox", pos=[-12.5,0,0.5] , size=[1,2,1], mass=1000)
		#pyrosim.Send_Sphere(name="GolfBall" , pos=[-0.5,0.3,1.5] , size=[0.5], mass = 1)

		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		
			#randomSnake
		#self.numLinks is in the constructor
		self.numLinks = random.randint(5,10)
		print(' ')
		print('the number of links is: ' +str(self.numLinks-1))
		print(' ')

		self.snakeLinks={}
		self.snakeJoints={}

		#pyrosim.Send_Cube(name="rootLink", pos=[0,0,6] , size=[1,1,1], mass=1.0, materialName="Blue", colorString="0 0 1 1", rpy="0 0 0")
		#pyrosim.Send_Joint( name = "rootLink_link1" , parent= "rootLink" , child = "link1" , type = "revolute", position = [0.5,0,6], jointAxis = "0 1 0")
		
		for i in range(1,self.numLinks):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.randSizeX = random.uniform(0.5,2.5)
			self.randSizeY = random.uniform(0.5,2.5)
			self.randSizeZ = random.uniform(0.5,2.5)
			self.randLinkPosX = self.randSizeX/2
			self.randJointPosX = self.randSizeX
			self.randMass = random.uniform(0,5)
			#self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])

			if i == 1:
				pyrosim.Send_Cube(name='link1', pos=[self.randLinkPosX,0,self.randSizeZ] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint( name = 'link1_link'+str(i+1) , parent='link1', child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,self.randSizeZ], jointAxis = "0 1 0")
			if i != 1 and i != self.numLinks:
				pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
			if i != 1 and i != self.numLinks-1:
				pyrosim.Send_Joint( name = 'link'+str(i)+'_link'+str(i+1) , parent='link'+str(i), child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,0], jointAxis = "0 1 0")
			if i == self.numLinks:
				pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
			
			self.linkName = {}
			self.linkName['link'+str(i)] = self.randMatName
			if self.linkName['link'+str(i)] == 'Green':
				print('link'+str(i)+' is green')
			else:
				print('link'+str(i)+' is blue')
			print(self.linkName)
			
			#self.snakeLinks.update(name = 'link'+str(i+1), materialName=self.randMatName)
			#self.snakeJoints.update(name = 'link'+str(i+1)+'_link'+str(i+2) , parent='link'+str(1), child ='link'+str(i+2), type = "revolute", position = [self.randJointPosX,0,0], jointAxis = "0 1 0")
		
		#pyrosim.Send_Cube(name='link'+str(self.numLinks), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,random.uniform(0.5,2.5),random.uniform(0.5,2.5)], mass=random.uniform(0,5), materialName="Blue", colorString="0 0 1 1", rpy="0 0 0")
		#the only issue with this last link outside the for loop is that it has to be the same width as the second to last link in order that there isn't a gap between the two.
		
		# what if we define two dictionaries in the constructor: snakeLinks={} and snakeJoints={}; then after we Send_Cube we add to snakeLinks and after we Send_Joint we add to snakeJoints.
		# then when we go down to Create_Brain, we pull from the dictionary, query the color, then apply sensorneurons as needed, and we apply motorneurons to all joints. 
		# then we get into the randomized weights of the sensors
		# having trouble with this ^^ .. could we have a nested dictionary, where the keys are 'link'+str(i):self.randMatName ??? seems a little overly complicated....
		
		#print(self.snakeLinks)
		#print(self.snakeLinks.keys())
		#print(self.snakeJoints.keys())

		pyrosim.End()
	

	def Create_Brain(self):
		#pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

		#for i in range(1,self.numLinks):
		#	if self.snakeLinks['materialName'] == "Blue":
		#		pyrosim.Send_Sensor_Neuron(name = i-1, linkName = self.snakeLinks)
		#for i in (1,self.numLinks):
			#pyrosim.Send_Motor_Neuron(name=)
	
		#for currentRow in range(0,c.numSensorNeurons):
		#	for currentColumn in range(0,c.numMotorNeurons):
		#		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)

		#pyrosim.End()
		pass
		
	

	def Mutate(self):
		randomRow = random.randint(0,c.numSensorNeurons-1)
		randomColumn = random.randint(0,c.numMotorNeurons-1)
		self.weights[randomRow,randomColumn] = random.random() * 2 - 1

	def Set_ID(self, ID):
		self.myID = ID


	



	#This goes in CREATE Body
		#Quadruped
		#pyrosim.Send_Cube(name="torso", pos=[0,0,1] , size=[c.length,c.width,c.height])
		#pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2])
		#pyrosim.Send_Joint( name = "frontleg_frontlowerleg" , parent= "frontleg" , child = "frontlowerleg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="frontlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])				
		#pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
		#pyrosim.Send_Joint( name = "backleg_backlowerleg" , parent= "backleg" , child = "backlowerleg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="backlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		#pyrosim.Send_Joint( name = "torso_leftleg" , parent= "torso" , child = "leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
		#pyrosim.Send_Joint( name = "leftleg_leftlowerleg" , parent= "leftleg" , child = "leftlowerleg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="leftlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		#pyrosim.Send_Joint( name = "torso_rightleg" , parent= "torso" , child = "rightleg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2])
		#pyrosim.Send_Joint( name = "rightleg_rightlowerleg" , parent= "rightleg" , child = "rightlowerleg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="rightlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		
			#golfer
		#pyrosim.Send_Cube(name="torso", pos=[0,-3,3] , size=[1,1,3], mass=1000.0, materialName="Red", colorString="1 0 0 1", rpy="0 0 0")
		#pyrosim.Send_Joint( name = "torso_arm" , parent= "torso" , child = "arm" , type = "revolute", position = [0,-2.5,4], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="arm", pos=[0,1.25,-1/6] , size=[1/3,2.5,1/3], materialName="Tan", colorString="1.3 0.94 0.92 1")
		#pyrosim.Send_Joint( name = "arm_club" , parent= "arm" , child = "club" , type = "fixed", position = [0,2.5,0], jointAxis = "1 0 0")		
		#pyrosim.Send_Cube(name="club", pos=[0,1/6,-1.5] , size=[1/3,1/3,2.8], materialName="Gray", colorString="1 1 1 1")
		#pyrosim.Send_Joint( name = "torso_hip" , parent= "torso" , child = "hip" , type = "revolute", position = [0,-3,1.75], jointAxis = "0 0 1")		
		#pyrosim.Send_Cube(name="hip", pos=[0,0,-0.5] , size=[1, 1, 0.5], mass=10000.0, materialName="Brown", colorString="0.7 0.6 0.5 1")


	#This goes in CREATE Brain
			#quadruped all sensors 
		#pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
		#pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backleg")
		#pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "backlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "frontleg")
		#pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "frontlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "leftleg")
		#pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "leftlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "rightleg")
		#pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "rightlowerleg")	
		#pyrosim.Send_Motor_Neuron( name = 9 , jointName = "torso_backleg")
		#pyrosim.Send_Motor_Neuron( name = 10 , jointName = "backleg_backlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 11 , jointName = "torso_frontleg")
		#pyrosim.Send_Motor_Neuron( name = 12 , jointName = "frontleg_frontlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 13 , jointName = "torso_leftleg")
		#pyrosim.Send_Motor_Neuron( name = 14 , jointName = "leftleg_leftlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 15 , jointName = "torso_rightleg")
		#pyrosim.Send_Motor_Neuron( name = 16 , jointName = "rightleg_rightlowerleg")
			#quadruped sensors only on lower legs
		#pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "backlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "frontlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "leftlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "rightlowerleg")	
		#pyrosim.Send_Motor_Neuron( name = 4 , jointName = "torso_backleg")
		#pyrosim.Send_Motor_Neuron( name = 5 , jointName = "backleg_backlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 6 , jointName = "torso_frontleg")
		#pyrosim.Send_Motor_Neuron( name = 7 , jointName = "frontleg_frontlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 8 , jointName = "torso_leftleg")
		#pyrosim.Send_Motor_Neuron( name = 9 , jointName = "leftleg_leftlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 10 , jointName = "torso_rightleg")
		#pyrosim.Send_Motor_Neuron( name = 11 , jointName = "rightleg_rightlowerleg")
			#golfer
		#pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "club")
		#pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "hip")
		#pyrosim.Send_Motor_Neuron(name=2, jointName = "torso_arm")
		#pyrosim.Send_Motor_Neuron(name=3, jointName = "torso_hip")