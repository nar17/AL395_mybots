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

	def Random_Variables(self):
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
		self.randLinkPosY = self.randSizeY/2
		self.randJointPosX = self.randSizeX
		self.randJointPosY = self.randSizeY
		self.randMass = 1 #random.uniform(0,5)
		self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])

	def Root_Link(self):
		pyrosim.Send_Cube(name='rootLink', pos=[0,0,1] , size=[2,2,2], mass=100, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")

		if random.random()<1:
			pyrosim.Send_Joint(name = 'rootLink_plusY_link0_plusY' , parent='rootLink', child ='link0_plusY' , type = "revolute", position = [0,1,1], jointAxis = "0 0 1")
			self.Links_PlusY()
			print(' ')
			print('the number of links in the plus-Y direction is '+ str(self.numLinks_plusY))
			print(' ')
		
		if random.random()<1:
			pyrosim.Send_Joint(name = 'rootLink_negY_link0_negY' , parent='rootLink', child ='link0_negY' , type = "revolute", position = [0,-1,1], jointAxis = "0 0 1")
			self.Links_NegY()
			print(' ')
			print('the number of links in the neg-Y direction is '+ str(self.numLinks_negY))
			print(' ')

		if random.random()<1:
			pyrosim.Send_Joint(name = 'rootLink_negX_link0_negX' , parent='rootLink', child ='link0_negX' , type = "revolute", position = [-1,0,1], jointAxis = "0 0 1")
			self.Links_NegX()
			print(' ')
			print('the number of links in the neg-X direction is '+ str(self.numLinks_negX))
			print(' ')


	def Links_PlusY(self):
		self.numLinks_plusY = random.randint(2,4)

		for i in range(0,self.numLinks_plusY):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_plusY = random.uniform(0.5,1)
			self.sizeY_plusY = random.uniform(0.5,2.5)
			self.sizeZ_plusY = random.uniform(0.5,1)
			self.LinkPosY_plusY = self.sizeY_plusY/2
			self.JointPosY_plusY = self.sizeY_plusY
			
			if i==0:
				pyrosim.Send_Cube(name='link0_plusY', pos=[0,self.LinkPosY_plusY,0] , size=[self.sizeX_plusY,self.sizeY_plusY,self.sizeZ_plusY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0_plusY_'+'link1_plusY', parent='link0_plusY', child ='link1_plusY', type = "revolute", position = [0,self.JointPosY_plusY,0], jointAxis = "0 0 1")
			if i!=0 and i!=self.numLinks_plusY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_plusY', pos=[0,self.LinkPosY_plusY*2/3,0] , size=[self.sizeX_plusY*2/3,self.sizeY_plusY*2/3,self.sizeZ_plusY*2/3], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'_plusY_'+'link'+str(i+1)+'_plusY', parent='link'+str(i)+'_plusY', child ='link'+str(i+1)+'_plusY', type = "revolute", position = [0,self.JointPosY_plusY*2/3,0], jointAxis = "0 0 1")
			if i==self.numLinks_plusY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_plusY', pos=[0,self.LinkPosY_plusY,0] , size=[self.sizeX_plusY,self.sizeY_plusY,self.sizeZ_plusY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")

	def Links_NegY(self):
		self.numLinks_negY = random.randint(2,4)

		for i in range(0,self.numLinks_negY):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_negY = random.uniform(0.5,1)
			self.sizeY_negY = random.uniform(0.5,2.5)
			self.sizeZ_negY = random.uniform(0.5,1)
			self.LinkNegY_negY = -self.sizeY_negY/2
			self.JointNegY_negY = -self.sizeY_negY
			
			if i==0:
				pyrosim.Send_Cube(name='link0_negY', pos=[0,self.LinkNegY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0_negY_'+'link1_negY', parent='link0_negY', child ='link1_negY', type = "revolute", position = [0,self.JointNegY_negY,0], jointAxis = "0 0 1")
			if i!=0 and i!=self.numLinks_negY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_negY', pos=[0,self.LinkNegY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'_negY_'+'link'+str(i+1)+'_negY', parent='link'+str(i)+'_negY', child ='link'+str(i+1)+'_negY', type = "revolute", position = [0,self.JointNegY_negY,0], jointAxis = "0 0 1")
			if i==self.numLinks_negY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_negY', pos=[0,self.LinkNegY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")

	def Links_NegX(self):
		self.numLinks_negX = random.randint(2,4)

		for i in range(0,self.numLinks_negX):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_negX = random.uniform(0.5,2.5)
			self.sizeY_negX = random.uniform(0.5,1)
			self.sizeZ_negX = random.uniform(0.5,1)
			self.LinkNegY_negX = -self.sizeX_negX/2
			self.JointNegY_negX = -self.sizeX_negX
			
			if i==0:
				pyrosim.Send_Cube(name='link0_negX', pos=[self.LinkNegY_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0_negX_'+'link1_negX', parent='link0_negX', child ='link1_negX', type = "revolute", position = [self.JointNegY_negX,0,0], jointAxis = "0 0 1")
			if i!=0 and i!=self.numLinks_negX-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_negX', pos=[self.LinkNegY_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'_negX_'+'link'+str(i+1)+'_negX', parent='link'+str(i)+'_negX', child ='link'+str(i+1)+'_negX', type = "revolute", position = [self.JointNegY_negX,0,0], jointAxis = "0 0 1")
			if i==self.numLinks_negX-1:
				pyrosim.Send_Cube(name='link'+str(i)+'_negX', pos=[self.LinkNegY_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")

		
	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		self.Random_Variables()
		self.Root_Link()
		
		self.movie = random.choice(["gangs of new york", "inside llewyn davis", "dont look up", "casino"])
		print(self.movie)

		
		
			#randomSnake
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