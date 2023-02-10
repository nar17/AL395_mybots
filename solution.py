import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.myID = nextAvailableID
		self.sensorList = {}
		self.motorList = {}
		self.neuronId = 0
		#self.weights = numpy.random.rand(len(self.sensorList),len(self.motorList)) * 2 - 1

		

		
		
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
			
			#quadruped fitness
		fitnessFile=open("fitness"+str(self.myID)+".txt","r")
		self.fitness = float(fitnessFile.read())

			#golf fitness
		#fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		#self.overallFitness = fitnessFile.readlines()
		#self.xfitness = float(self.overallFitness[0])
		#self.yfitness = float(self.overallFitness[1])
		
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

	def Random_Robot_Multiple_Dimensions(self):
		if random.random()<0.5:
			self.randMatName = "Blue"
			self.randColStr = "0 0 1 1"
		else:
			self.randMatName = "Green"
			self.randColStr = "0 1 0 1"
		#self.randSizeX = random.uniform(0.5,2.5)
		#self.randSizeY = random.uniform(0.5,2.5)
		#self.randSizeZ = random.uniform(0.5,2.5)
		#self.randLinkPosX = self.randSizeX/2
		#self.randLinkPosY = self.randSizeY/2
		#self.randJointPosX = self.randSizeX
		#self.randJointPosY = self.randSizeY
		self.randMass = 1 #random.uniform(0,5)
		#self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])

		pyrosim.Send_Cube(name='link1', pos=[0,0,1] , size=[2,2,2], mass=100, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")

	def Links_Off_Rootlink(self):
		pyrosim.Send_Joint( name = 'link1_link2_xy' , parent='link1', child ='link2' , type = "revolute", position = [0,1,1], jointAxis = "0 0 1")
		#pyrosim.Send_Joint( name = 'link1_link2_xz' , parent='link1', child ='link2' , type = "revolute", position = [0,1,1], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name='link2', pos=[0,1.5,0] , size=[1,1.5,1], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
		
	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		
		self.Random_Robot_Multiple_Dimensions()
		self.Links_Off_Rootlink()
		
			#randomSnake
		#self.numLinks is in the constructor
		#self.numLinks = random.randint(5,10)
		#print(' ')
		#print('the number of links is: ' +str(self.numLinks-1))
		#print(' ')
		
		#for i in range(1,self.numLinks):
		#	if random.random()<0.5:
		#		self.randMatName = "Blue"
		#		self.randColStr = "0 0 1 1"
		#	else:
		#		self.randMatName = "Green"
		#		self.randColStr = "0 1 0 1"
		#	self.randSizeX = random.uniform(0.5,2.5)
		#	self.randSizeY = random.uniform(0.5,2.5)
		#	self.randSizeZ = random.uniform(0.5,2.5)
		#	self.randLinkPosX = self.randSizeX/2
		#	self.randJointPosX = self.randSizeX
		#	self.randMass = 1 #random.uniform(0,5)
		#	#self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
		#
		#	if i == 1:
		#		pyrosim.Send_Cube(name='link1', pos=[self.randLinkPosX,0,self.randSizeZ] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
		#		pyrosim.Send_Joint( name = 'link1_link'+str(i+1) , parent='link1', child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,self.randSizeZ], jointAxis = "0 1 0")
		#		if self.randMatName == "Green":
		#			self.sensorList[i] = 'link'+str(i)
		#		self.motorList['joint'+str(i)] = 'link1_link'+str(i+1)
		#	if i != 1 and i != self.numLinks:
		#		pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
		#		if self.randMatName == "Green":
		#			self.sensorList[i] = 'link'+str(i)
		#	if i != 1 and i != self.numLinks-1:
		#		pyrosim.Send_Joint( name = 'link'+str(i)+'_link'+str(i+1) , parent='link'+str(i), child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,0], jointAxis = "0 1 0")
		#		self.motorList['joint'+str(i)] = 'link'+str(i)+'_link'+str(i+1)
		#	if i == self.numLinks:
		#		pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
		#		if self.randMatName == "Green":
		#			self.sensorList[i] = 'link'+str(i)


		pyrosim.End()
	

	def Create_Brain(self):
		
		#pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")	

			#quadruped/golfer
		#for currentRow in range(0,c.numSensorNeurons):
		#	for currentColumn in range(0,c.numMotorNeurons):
		#		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)

			#randomSnake
		#for i in self.sensorList:
		#	pyrosim.Send_Sensor_Neuron(name = self.neuronId, linkName = str(self.sensorList[i]))
		#	self.neuronId +=1
		#for i in self.motorList:
		#	pyrosim.Send_Motor_Neuron(name = self.neuronId, jointName = str(self.motorList[i]))
		#	self.neuronId +=1
		#self.weights = numpy.random.rand(len(self.sensorList),len(self.motorList)) * 2 - 1
		#for currentRow in range(0,len(self.sensorList)):
		#	for currentColumn in range(0,len(self.motorList)):
		#		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.sensorList) , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)

		#pyrosim.End()
		pass

	def Mutate(self):
			#randomSnake
		randomRow = random.randint(0,len(self.sensorList)-1)
		randomColumn = random.randint(0,len(self.sensorMotor)-1)
		self.weights[randomRow,randomColumn] = random.random() * 2 - 1
		
			#quadruped/golfer
		#randomRow = random.randint(0,c.numSensorNeurons-1)
		#randomColumn = random.randint(0,c.numMotorNeurons-1)
		#self.weights[randomRow,randomColumn] = random.random() * 2 - 1

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