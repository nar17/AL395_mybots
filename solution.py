import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.myID = nextAvailableID
		self.listID = 0
	
		random.seed(c.randomSeed)
		numpy.random.seed(c.numpyRandomSeed)
		#self.weights = numpy.random.rand(len(self.sensorList),len(self.motorList)) * 2 - 1
		

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		self.directOrGUI = directOrGUI
		os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		#self.Clear_Lists()
		

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
		#os.system("del fitness" + str(self.myID) + ".txt")
		

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

	def Pick_Pos(self, i):
		if self.pickPos[i-1]=='Z':
			self.pickPos.append(random.choice(['Y','X']))
			if self.pickPos[i]=='Y':#
				self.LPosListNPP.append([0,self.Y[i]/2,0])
				self.JPosListNPP.append([0,self.Y[i-1]/2,self.Z[i-1]/2])
				self.LPosListNNP.append([0,-self.Y[i]/2,0])
				self.JPosListNNP.append([0,-self.Y[i-1]/2,self.Z[i-1]/2])
			elif self.pickPos[i]=='X':
				self.LPosListNPP.append([-self.X[i]/2,0,0])
				self.JPosListNPP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
				self.LPosListNNP.append([-self.X[i]/2,0,0])
				self.JPosListNNP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])

		elif self.pickPos[i-1]=='Y':
			self.pickPos.append(random.choice(['Z','X']))
			if self.pickPos[i]=='Z':
				self.LPosListNPP.append([0,0,self.Z[i]/2])
				self.JPosListNPP.append([0,self.Y[i-1]/2,self.Z[i-1]/2])
				self.LPosListNNP.append([0,0,self.Z[i]/2])
				self.JPosListNNP.append([0,-self.Y[i-1]/2,self.Z[i-1]/2])
			elif self.pickPos[i]=='X':
				self.LPosListNPP.append([-self.X[i]/2,0,0])
				self.JPosListNPP.append([-self.X[i-1]/2,self.Y[i-1]/2,0])
				self.LPosListNNP.append([-self.X[i]/2,0,0])
				self.JPosListNNP.append([-self.X[i-1]/2,-self.Y[i-1]/2,0])

		elif self.pickPos[i-1]=='X':
			self.pickPos.append(random.choice(['Z','Y']))
			if self.pickPos[i]=='Z':
				self.LPosListNPP.append([0,0,self.Z[i]/2])
				self.JPosListNPP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
				self.LPosListNNP.append([0,0,self.Z[i]/2])
				self.JPosListNNP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
			elif self.pickPos[i]=='Y':
				self.LPosListNPP.append([0,self.Y[i]/2,0])
				self.JPosListNPP.append([-self.X[i-1]/2,self.Y[i-1]/2,0])
				self.LPosListNNP.append([0,-self.Y[i]/2,0])
				self.JPosListNNP.append([-self.X[i-1]/2,-self.Y[i-1]/2,0])
		
	def New_A7_Lists(self):
		self.numLinks_A7=random.randint(2,3)+1
		self.numJoints_A7=self.numLinks_A7-1

		self.X=[]
		self.Y=[]
		self.Z=[]

		self.pickPos=[]

			#link lists
		self.LnameListNPP=[] 
		self.LnameListNNP=[] 
		self.LPosListNPP=[]
		self.LPosListNNP=[]  
		self.LmatList=[]
		self.LcolorStringList=[]
			#joint lists
		self.JnameListNPP=[]
		self.JnameListNNP=[]
		self.JparentListNPP=[]
		self.JparentListNNP=[]
		self.JchildListNPP=[] 
		self.JchildListNNP=[] 
		self.JPosListNPP=[]
		self.JPosListNNP=[]
		self.JaxisList=[]

		#rootlink appends
		self.rootSize=1
		self.rootPos=1
		self.X.append(0)
		self.Y.append(0)
		self.Z.append(self.rootPos)
		self.pickPos.append('Z')
		self.LnameListNPP.append('rootLink')
		self.LnameListNNP.append('rootLink')
		self.LmatList.append("Green")
		self.LcolorStringList.append("0 1 0 1")
		self.LPosListNPP.append([0,self.rootPos,self.rootPos])
		self.LPosListNNP.append([0,self.rootPos,self.rootPos])
		self.JnameListNPP.append('rootLink_link1NPP')
		self.JnameListNNP.append('rootLink_link1NNP')
		self.JparentListNPP.append('rootLink')
		self.JparentListNNP.append('rootLink')
		self.JchildListNPP.append('link1NPP')
		self.JchildListNNP.append('link1NNP')
		self.JPosListNPP.append([0,self.rootPos,self.rootPos])
		self.JPosListNNP.append([0,self.rootPos,self.rootPos])
		self.JaxisList.append("0 1 0")
		
		#link lists appends
		for i in range(1,self.numLinks_A7):
			self.X.append(random.uniform(0.2,1))
			self.Y.append(random.uniform(0.2,0.6))
			self.Z.append(random.uniform(0.2,1))
				#link appends
			self.LnameListNPP.append('link'+str(i)+'NPP')
			self.LnameListNNP.append('link'+str(i)+'NNP')
			self.LmatList.append(random.choice(["Blue","Green"]))
			if self.LmatList[i]=="Blue":
				self.LcolorStringList.append("0 0 1 1")
			else:
				self.LmatList[i]=="Green"
				self.LcolorStringList.append("0 1 0 1")

		#joint list appends
		for i in range(1,self.numJoints_A7):
				#joint appends
			self.JnameListNPP.append('link'+str(i)+'NPP'+'_link'+str(i+1)+'NPP')
			self.JnameListNNP.append('link'+str(i)+'NNP'+'_link'+str(i+1)+'NNP')
			self.JparentListNPP.append('link'+str(i)+'NPP')
			self.JparentListNNP.append('link'+str(i)+'NNP')
			self.JchildListNPP.append('link'+str(i+1)+'NPP')
			self.JchildListNNP.append('link'+str(i+1)+'NNP')
			if i == 1:
				self.JaxisList.append("0 1 0")
			else:
				self.JaxisList.append(random.choice(["1 0 0", "0 1 0", "0 0 1"]))

		for i in range(1,self.numLinks_A7):
			self.Pick_Pos(i)
			
		self.listID+=1
		

	def New_A7_Generator(self):
		self.sensorList = []
		self.motorList = []
		self.neuronId = 0

		#rootlink
		self.rootSize=1
		self.rootPos=1
		pyrosim.Send_Cube(name='rootLink', pos=[0,0,self.rootPos], size=[self.rootSize,self.rootSize,self.rootSize], mass=10, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name='rootLink_link1NPP', parent='rootLink', child='link1NPP', type="revolute", position=[0,self.rootSize/2,self.rootPos/2], jointAxis="0 1 0")
		pyrosim.Send_Joint(name='rootLink_link1NNP', parent='rootLink', child='link1NNP', type="revolute", position=[0,-self.rootSize/2,self.rootPos/2], jointAxis="0 1 0")
		self.sensorList.append('rootLink')
		self.motorList.append('rootLink_link1NPP')
		self.motorList.append('rootLink_link1NNP')
		#NPPlinks
		for i in range(1,self.numLinks_A7):
			pyrosim.Send_Cube(name=self.LnameListNPP[i], pos=self.LPosListNPP[i-1], size=[self.X[i-1],self.Y[i-1],self.Z[i-1]], mass=1, materialName=self.LmatList[i], colorString=self.LcolorStringList[i], rpy="0 0 0")
			if self.LmatList[i] == "Green":
				self.sensorList.append(self.LnameListNPP[i])
		#NNPlinks
		for i in range(1,self.numLinks_A7):
			pyrosim.Send_Cube(name=self.LnameListNNP[i], pos=self.LPosListNNP[i-1], size=[self.X[i-1],self.Y[i-1],self.Z[i-1]], mass=1, materialName=self.LmatList[i], colorString=self.LcolorStringList[i], rpy="0 0 0")
			if self.LmatList[i] == "Green":
				self.sensorList.append(self.LnameListNNP[i])
		#NPPjoints
		for i in range(1,self.numJoints_A7):
			pyrosim.Send_Joint(name=self.JnameListNPP[i], parent=self.JparentListNPP[i], child=self.JchildListNPP[i], type="revolute", position=self.JPosListNPP[i], jointAxis=self.JaxisList[i]) #[0,self.JposList[i-1],0]
			self.motorList.append(self.JnameListNPP[i])
		#NNPjoints
		for i in range(1,self.numJoints_A7):
			pyrosim.Send_Joint(name=self.JnameListNNP[i], parent=self.JparentListNNP[i], child=self.JchildListNNP[i], type="revolute", position=self.JPosListNNP[i], jointAxis=self.JaxisList[i]) #[0,self.JposList[i-1],0]
			self.motorList.append(self.JnameListNNP[i])


	def Create_Body(self):
		pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
		if self.listID==0:
			self.New_A7_Lists()
		self.New_A7_Generator()
		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")	

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

			#New_A7
		self.numHiddenNeurons = 3 #random.randint(len(self.sensorList),len(self.motorList)-1)

		for i in range(len(self.sensorList)):
			pyrosim.Send_Sensor_Neuron(name = self.neuronId, linkName = self.sensorList[i])
			self.neuronId +=1
		for i in range(len(self.motorList)):
			pyrosim.Send_Motor_Neuron(name = self.neuronId, jointName = self.motorList[i])
			self.neuronId +=1
		#for i in range(self.numHiddenNeurons):
		#	pyrosim.Send_Hidden_Neuron(name = self.neuronId)
		#	self.neuronId +=1

			#synapse with no hidden neurons
		self.weights = numpy.random.rand(len(self.sensorList),len(self.motorList)) * 2 - 1
		for currentRow in range(len(self.sensorList)):
			for currentColumn in range(len(self.motorList)):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.sensorList) , weight = self.weights[currentRow][currentColumn]) #weight = random.random() #weight = random.uniform(-1,1)

		#synapse with hidden neurons
			#sensor to hidden
		#self.weights = numpy.random.rand(len(self.sensorList),self.numHiddenNeurons) * 2 - 1
		#for currentRow in range(0,len(self.sensorList)):
		#	for currentColumn in range(0,self.numHiddenNeurons):
		#		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.sensorList)+len(self.motorList) , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)

			#hidden to motor
		#self.weights = numpy.random.rand(self.numHiddenNeurons,len(self.motorList)) * 2 - 1
		#for currentRow in range(0,self.numHiddenNeurons):
		#	for currentColumn in range(0,len(self.motorList)):
		#		pyrosim.Send_Synapse( sourceNeuronName = currentRow+len(self.sensorList)+len(self.motorList) , targetNeuronName = currentColumn+len(self.sensorList) , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)

		#print('the number of sensor neurons is '+str(len(self.sensorList)))
		#print('the number of hidden neurons is '+str(self.numHiddenNeurons))
		#print('the number of motor neurons is '+str(len(self.motorList)))

		self.neuronId = 0
		pyrosim.End()
		

	def Mutate(self):
		self.randMut = random.random()
		
		if self.randMut<0.33:
			self.Mutate_Add_Link()
		elif 0.33<self.randMut<0.66:
			self.Mutate_Joint_Axis()
		else:
			self.Mutate_Sensor_Placement()
		
		self.Mutate_Synapses()

	
	def Mutate_Joint_Axis(self):
		self.linkListIndex = random.randint(0,self.numLinks_A7-2) #having error here.. just subtracted another 1 ?
		self.JaxisList[self.linkListIndex]=random.choice(["1 0 0", "0 1 0", "0 0 1"])

	def Mutate_Sensor_Placement(self):
		self.linkListIndex = random.randint(0,self.numLinks_A7-1)

		if self.LmatList[self.linkListIndex] == "Green":
			self.LmatList[self.linkListIndex] = "Blue"
			self.LcolorStringList[self.linkListIndex] = "0 0 1 1"
		else:
			self.LmatList[self.linkListIndex] = "Green"
			self.LcolorStringList[self.linkListIndex] = "0 1 0 1"

	def Mutate_Add_Link(self):
		self.new = self.numLinks_A7
		i = self.numLinks_A7

		self.X.append(random.uniform(0.2,1))
		self.Y.append(random.uniform(0.2,0.6))
		self.Z.append(random.uniform(0.2,1))
			#link appends
		self.LnameListNPP.append('link'+str(self.new)+'NPP')
		self.LnameListNNP.append('link'+str(self.new)+'NNP')
		self.LmatList.append(random.choice(["Blue","Green"]))
		if self.LmatList[self.new]=="Blue":
			self.LcolorStringList.append("0 0 1 1")
		else:
			self.LmatList[self.new]=="Green"
			self.LcolorStringList.append("0 1 0 1")
		self.JnameListNPP.append('link'+str(self.new-1)+'NPP'+'_link'+str(self.new)+'NPP')
		self.JnameListNNP.append('link'+str(self.new-1)+'NNP'+'_link'+str(self.new)+'NNP')
		self.JparentListNPP.append('link'+str(self.new-1)+'NPP')
		self.JparentListNNP.append('link'+str(self.new-1)+'NNP')
		self.JchildListNPP.append('link'+str(self.new)+'NPP')
		self.JchildListNNP.append('link'+str(self.new)+'NNP')
		self.JaxisList.append(random.choice(["1 0 0", "0 1 0", "0 0 1"]))

		if self.pickPos[i-1]=='Z':
			self.pickPos.append(random.choice(['Y','X']))
			if self.pickPos[i]=='Y':#
				self.LPosListNPP.append([0,self.Y[i]/2,0])
				self.JPosListNPP.append([0,self.Y[i-1]/2,self.Z[i-1]/2])
				self.LPosListNNP.append([0,-self.Y[i]/2,0])
				self.JPosListNNP.append([0,-self.Y[i-1]/2,self.Z[i-1]/2])
			elif self.pickPos[i]=='X':
				self.LPosListNPP.append([-self.X[i]/2,0,0])
				self.JPosListNPP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
				self.LPosListNNP.append([-self.X[i]/2,0,0])
				self.JPosListNNP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])

		elif self.pickPos[i-1]=='Y':
			self.pickPos.append(random.choice(['Z','X']))
			if self.pickPos[i]=='Z':
				self.LPosListNPP.append([0,0,self.Z[i]/2])
				self.JPosListNPP.append([0,self.Y[i-1]/2,self.Z[i-1]/2])
				self.LPosListNNP.append([0,0,self.Z[i]/2])
				self.JPosListNNP.append([0,-self.Y[i-1]/2,self.Z[i-1]/2])
			elif self.pickPos[i]=='X':
				self.LPosListNPP.append([-self.X[i]/2,0,0])
				self.JPosListNPP.append([-self.X[i-1]/2,self.Y[i-1]/2,0])
				self.LPosListNNP.append([-self.X[i]/2,0,0])
				self.JPosListNNP.append([-self.X[i-1]/2,-self.Y[i-1]/2,0])

		elif self.pickPos[i-1]=='X':
			self.pickPos.append(random.choice(['Z','Y']))
			if self.pickPos[i]=='Z':
				self.LPosListNPP.append([0,0,self.Z[i]/2])
				self.JPosListNPP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
				self.LPosListNNP.append([0,0,self.Z[i]/2])
				self.JPosListNNP.append([-self.X[i-1]/2,0,self.Z[i-1]/2])
			elif self.pickPos[i]=='Y':
				self.LPosListNPP.append([0,self.Y[i]/2,0])
				self.JPosListNPP.append([-self.X[i-1]/2,self.Y[i-1]/2,0])
				self.LPosListNNP.append([0,-self.Y[i]/2,0])
				self.JPosListNNP.append([-self.X[i-1]/2,-self.Y[i-1]/2,0])

		self.numLinks_A7 = self.numLinks_A7+1
		self.numJoints_A7 = self.numJoints_A7+1

	def Mutate_Synapses(self):
			#newA7 synapses no hidden
		randomRow = random.randint(0,len(self.sensorList)-1)
		randomColumn = random.randint(0,len(self.motorList)-1)
		self.weights[randomRow,randomColumn] = random.random() * 2 - 1

			#newA7 synapses with hidden
		#randomRowStH = random.randint(0,len(self.sensorList)-1)
		#randomColumnStH = random.randint(0,self.numHiddenNeurons-1)
		#self.weights[randomRowStH,randomColumnStH] = random.random() * 2 - 1

		#randomRowHtM = random.randint(0,self.numHiddenNeurons-1)
		#randomColumnHtM = random.randint(0,len(self.motorList)-1)
		#self.weights[randomRowHtM,randomColumnHtM] = random.random() * 2 - 1
		
			#quadruped/golfer
		#randomRow = random.randint(0,c.numSensorNeurons-1)
		#randomColumn = random.randint(0,c.numMotorNeurons-1)
		#self.weights[randomRow,randomColumn] = random.random() * 2 - 1


	def Set_ID(self, ID):
		self.myID = ID


















#############################################################################IGNORE################################################################################################
	def Clear_Lists(self):
		self.sensorList.clear()
		self.motorList.clear()
		
		self.X.clear()
		self.Y.clear()
		self.Z.clear()

		self.pickPos.clear()

			#link lists
		self.LnameListNPP.clear()
		self.LnameListNNP.clear()
		self.LPosListNPP.clear()
		self.LPosListNNP.clear()
		self.LmatList.clear()
		self.LcolorStringList.clear()
			#joint lists
		self.JnameListNPP.clear()
		self.JnameListNNP.clear()
		self.JparentListNPP.clear()
		self.JparentListNNP.clear()
		self.JchildListNPP.clear()
		self.JchildListNNP.clear()
		self.JPosListNPP.clear()
		self.JPosListNNP.clear()
		self.JaxisList.clear()


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


	def Crawler(self):
		self.numLinks_Crawler = random.randint(2,4)

			
		pyrosim.Send_Cube(name='rootLink', pos=[0,0,1] , size=[2,2,2], mass=100, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name = 'rootLink_link0_plusY' , parent='rootLink', child ='link0_plusY' , type = "revolute", position = [0,1,2], jointAxis = "0 0 1")
		pyrosim.Send_Joint(name = 'rootLink_link0_negY' , parent='rootLink', child ='link0_negY' , type = "revolute", position = [0,-1,2], jointAxis = "0 0 1")
		
		pyrosim.Send_Cube(name='link0_plusY', pos=[0,0,0.5] , size=[0.5,0.5,1], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name = 'link0_plusY_link1_plusY' , parent='link0_plusY', child ='link1_plusY' , type = "revolute", position = [0,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name='link1_plusY', pos=[0,1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name = 'link1_plusY_link2_plusY' , parent='link1_plusY', child ='link2_plusY' , type = "revolute", position = [0,2,0], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name='link2_plusY', pos=[0,0,-1.5] , size=[0.5,0.5,3], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")

		pyrosim.Send_Cube(name='link0_negY', pos=[0,0,0.5] , size=[0.5,0.5,1], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name = 'link0_negY_link1_negY' , parent='link0_negY', child ='link1_negY' , type = "revolute", position = [0,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name='link1_negY', pos=[0,-1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name = 'link1_negY_link2_negY' , parent='link1_negY', child ='link2_negY' , type = "revolute", position = [0,-2,0], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name='link2_negY', pos=[0,0,-1.5] , size=[0.5,0.5,3], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")


	def Simple_Bot(self):
		self.size = random.uniform(0.5,2.5)
		self.jointPosX = random.uniform(-self.size,self.size)/2
		self.jointPosY = self.size/2
		self.jointPosZ = random.uniform(0,self.size)/2
		self.axis = random.choice(["1 0 0", "0 1 0", "0 0 1"])
		self.X = random.uniform(0.2,1)
		self.Y = random.uniform(0.2,1)
		self.Z = random.uniform(0.2,1)
		#self.armPos = random.uniform(-)

		pyrosim.Send_Cube(name='rootLink', pos=[0,0,self.size/2] , size=[self.size,self.size,self.size], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Joint(name='rootLink_link0_plusY', parent='rootLink', child='link0_plusY', type='revolute', position=[self.jointPosX,self.jointPosY,self.jointPosZ], jointAxis=self.axis)
		pyrosim.Send_Joint(name='rootLink_link0_negY', parent='rootLink', child='link0_negY', type='revolute', position=[self.jointPosX,-self.jointPosY,self.jointPosZ], jointAxis=self.axis)
		pyrosim.Send_Cube(name='link0_plusY', pos=[0,self.Y/2,0] , size=[self.X,self.Y,self.Z], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		pyrosim.Send_Cube(name='link0_negY', pos=[0,-self.Y/2,0] , size=[self.X,self.Y,self.Z], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")


	def Four_Leg_Body(self):
		self.rootLinkPosZ = 1
		pyrosim.Send_Cube(name='rootLink', pos=[0,0,self.rootLinkPosZ] , size=[2,2,2], mass=5, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
		self.sensorList['rootLink']= 'rootLink'

		if random.random()<1:
			pyrosim.Send_Joint(name = 'rootLink_link0plusY' , parent='rootLink', child ='link0plusY' , type = "revolute", position = [0,1,self.rootLinkPosZ], jointAxis = random.choice(["1 0 0", "0 1 0", "0 0 1"]))
			self.motorList['rootLink_jointplusY']='rootLink_link0plusY'
			self.Links_PlusY()
			print('the number of links in the plus-Y direction is '+ str(self.numLinks_plusY))

		#if random.random()<1:
		#	pyrosim.Send_Joint(name = 'rootLink_link0negY' , parent='rootLink', child ='link0negY' , type = "revolute", position = [0,-1,self.rootLinkPosZ], jointAxis = random.choice(["1 0 0", "0 1 0", "0 0 1"]))
		#	self.motorList['rootLink_jointnegY']='rootLink_link0negY'
		#	self.Links_NegY()
		#	print('the number of links in the neg-Y direction is '+ str(self.numLinks_negY))

		#if random.random()<0.5:
		#	pyrosim.Send_Joint(name = 'rootLink_link0negX' , parent='rootLink', child ='link0negX' , type = "revolute", position = [-1,0,self.rootLinkPosZ], jointAxis = random.choice(["1 0 0", "0 1 0", "0 0 1"]))
		#	self.motorList['rootLink_jointnegX']='rootLink_link0negX'
		#	self.Links_NegX()
		#	print('the number of links in the neg-X direction is '+ str(self.numLinks_negX))

		#if random.random()<0.5:
		#	pyrosim.Send_Joint(name = 'rootLink_link0plusZ' , parent='rootLink', child ='link0plusZ' , type = "revolute", position = [0,0,self.rootLinkPosZ+1], jointAxis = random.choice(["1 0 0", "0 1 0", "0 0 1"]))
		#	self.motorList['rootLink_jointplusZ']='rootLink_link0plusZ'
		#	self.Links_PlusZ()
		#	print('the number of links in the plus-Z direction is '+ str(self.numLinks_plusZ))

			

			
	def Links_PlusY(self):		#editted to try to figure it out.. if want to go back to original change back sizes and positions
		self.numLinks_plusY = 3#random.randint(2,3)
		
		for i in range(0,self.numLinks_plusY):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_plusY = random.uniform(0.5,1.5)
			self.sizeY_plusY = random.uniform(0.5,2.5)
			self.sizeZ_plusY = random.uniform(0.5,1.5)
			self.size_plusY = 1
			self.LinkPosY_plusY = 1/2
			self.JointPosY_plusY = 1
			self.randMass = 1 #random.uniform(0,5)
			self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
			self.axis = random.choice(["1 0 0", "0 1 0", "0 0 1"])
			#self.linkPos = random.choice([[self.size_plusY/2,0,0],[0,self.size_plusY/2,0],[0,0,self.size_plusY/2]])
			#self.jointPos = random.choice([[self.size_plusY,0,0],[0,self.size_plusY,0],[0,0,self.size_plusY]])
			self.jointlinkchoice = random.choice([1,2,3])
			if self.jointlinkchoice == 1: #plusY 
				self.linkPos = [self.size_plusY/2,self.size_plusY/2,0]
				self.jointPos = [self.size_plusY,self.size_plusY,0]
			if self.jointlinkchoice == 2:
				self.linkPos = [0,self.size_plusY/2,self.size_plusY/2]
				self.jointPos = [0,self.size_plusY,self.size_plusY]
			if self.jointlinkchoice == 3:
				self.linkPos = [self.size_plusY/2,0,self.size_plusY/2]
				self.jointPos = [self.size_plusY,0,self.size_plusY]
			
			if i==0:
				pyrosim.Send_Cube(name='link0plusY', pos=[0,1/2,0] , size=[self.size_plusY,self.size_plusY,self.size_plusY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0plusY_'+'link1plusY', parent='link0plusY', child ='link1plusY', type = "revolute", position = [0,1,0], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusY']= 'link0plusY'
				self.motorList['joint'+str(i)+'plusY']='link0plusY_link1plusY'
			if i!=0 and i!=self.numLinks_plusY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'plusY', pos=self.linkPos , size=[self.size_plusY,self.size_plusY,self.size_plusY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'plusY_'+'link'+str(i+1)+'plusY', parent='link'+str(i)+'plusY', child ='link'+str(i+1)+'plusY', type = "revolute", position = self.jointPos, jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusY']= 'link'+str(i)+'plusY'
				self.motorList['joint'+str(i)+'plusY']='link'+str(i)+'plusY_'+'link'+str(i+1)+'plusY'
			if i==self.numLinks_plusY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'plusY', pos=self.linkPos, size=[self.size_plusY,self.size_plusY,self.size_plusY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusY']= 'link'+str(i)+'plusY'

	def Links_NegY(self):
		self.numLinks_negY = random.randint(2,3)

		for i in range(0,self.numLinks_negY):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_negY = random.uniform(0.5,1.5)
			self.sizeY_negY = random.uniform(0.5,2.5)
			self.sizeZ_negY = random.uniform(0.5,1.5)
			self.LinkPosY_negY = -self.sizeY_negY/2
			self.JointPosY_negY = -self.sizeY_negY
			self.randMass = 1 #random.uniform(0,5)
			self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
			self.axis = random.choice(["1 0 0", "0 1 0", "0 0 1"])
			
			if i==0:
				pyrosim.Send_Cube(name='link0negY', pos=[0,self.LinkPosY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0negY_'+'link1negY', parent='link0negY', child ='link1negY', type = "revolute", position = [0,self.JointPosY_negY,0], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negY']= 'link0negY'
				self.motorList['joint'+str(i)+'negY']='link0negY_link1negY'
			if i!=0 and i!=self.numLinks_negY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'negY', pos=[0,self.LinkPosY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'negY_'+'link'+str(i+1)+'negY', parent='link'+str(i)+'negY', child ='link'+str(i+1)+'negY', type = "revolute", position = [0,self.JointPosY_negY,0], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negY']= 'link'+str(i)+'negY'
				self.motorList['joint'+str(i)+'negY']='link'+str(i)+'negY_'+'link'+str(i+1)+'negY'
			if i==self.numLinks_negY-1:
				pyrosim.Send_Cube(name='link'+str(i)+'negY', pos=[0,self.LinkPosY_negY,0] , size=[self.sizeX_negY,self.sizeY_negY,self.sizeZ_negY], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negY']= 'link'+str(i)+'negY'

	def Links_NegX(self):
		self.numLinks_negX = random.randint(2,3)

		for i in range(0,self.numLinks_negX):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_negX = random.uniform(0.5,2.5)
			self.sizeY_negX = random.uniform(0.5,1.5)
			self.sizeZ_negX = random.uniform(0.5,1.5)
			self.LinkPosX_negX = -self.sizeX_negX/2
			self.JointPosX_negX = -self.sizeX_negX
			self.randMass = 1 #random.uniform(0,5)
			self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
			self.axis = random.choice(["1 0 0", "0 1 0", "0 0 1"])
			
			if i==0:
				pyrosim.Send_Cube(name='link0negX', pos=[self.LinkPosX_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0negX_link1negX', parent='link0negX', child ='link1negX', type = "revolute", position = [self.JointPosX_negX,0,0], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negX']= 'link0negX'
				self.motorList['joint'+str(i)+'negX']='link0negX_link1negX'
			if i!=0 and i!=self.numLinks_negX-1:
				pyrosim.Send_Cube(name='link'+str(i)+'negX', pos=[self.LinkPosX_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'negX_'+'link'+str(i+1)+'negX', parent='link'+str(i)+'negX', child ='link'+str(i+1)+'negX', type = "revolute", position = [self.JointPosX_negX,0,0], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negX']= 'link'+str(i)+'negX'
				self.motorList['joint'+str(i)+'negX']='link'+str(i)+'negX_'+'link'+str(i+1)+'negX'
			if i==self.numLinks_negX-1:
				pyrosim.Send_Cube(name='link'+str(i)+'negX', pos=[self.LinkPosX_negX,0,0] , size=[self.sizeX_negX,self.sizeY_negX,self.sizeZ_negX], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				if self.randMatName == "Green":
					self.sensorList[str(i)+'negX']= 'link'+str(i)+'negX'

	def Links_PlusZ(self):
		self.numLinks_plusZ = random.randint(2,3)

		for i in range(0,self.numLinks_plusZ):
			if random.random()<0.5:
				self.randMatName = "Blue"
				self.randColStr = "0 0 1 1"
			else:
				self.randMatName = "Green"
				self.randColStr = "0 1 0 1"
			self.sizeX_plusZ = random.uniform(0.5,1.5)
			self.sizeY_plusZ = random.uniform(0.5,1.5)
			self.sizeZ_plusZ = random.uniform(0.5,2.5)
			self.LinkPosZ_plusZ = self.sizeZ_plusZ/2
			self.JointPosZ_plusZ = self.sizeZ_plusZ
			self.randMass = 1 #random.uniform(0,5)
			self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
			self.axis = random.choice(["1 0 0", "0 1 0", "0 0 1"])
			
			if i==0:
				pyrosim.Send_Cube(name='link0plusZ', pos=[0,0,self.LinkPosZ_plusZ] , size=[self.sizeX_plusZ,self.sizeY_plusZ,self.sizeZ_plusZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link0plusZ_link1plusZ', parent='link0plusZ', child ='link1plusZ', type = "revolute", position = [0,0,self.JointPosZ_plusZ], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusZ']= 'link0plusZ'
				self.motorList['joint'+str(i)+'plusZ']='link0plusZ_link1plusZ'
			if i!=0 and i!=self.numLinks_plusZ-1:
				pyrosim.Send_Cube(name='link'+str(i)+'plusZ', pos=[0,0,self.LinkPosZ_plusZ] , size=[self.sizeX_plusZ,self.sizeY_plusZ,self.sizeZ_plusZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				pyrosim.Send_Joint(name = 'link'+str(i)+'plusZ_'+'link'+str(i+1)+'plusZ', parent='link'+str(i)+'plusZ', child ='link'+str(i+1)+'plusZ', type = "revolute", position = [0,0,self.JointPosZ_plusZ], jointAxis = self.axis)
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusZ']= 'link'+str(i)+'plusZ'
				self.motorList['joint'+str(i)+'plusZ']='link'+str(i)+'plusZ_'+'link'+str(i+1)+'plusZ'
			if i==self.numLinks_plusZ-1:
				pyrosim.Send_Cube(name='link'+str(i)+'plusZ', pos=[0,0,self.LinkPosZ_plusZ] , size=[self.sizeX_plusZ,self.sizeY_plusZ,self.sizeZ_plusZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
				if self.randMatName == "Green":
					self.sensorList[str(i)+'plusZ']= 'link'+str(i)+'plusZ'


					#randomSnake
		#self.numLinks = 3 #random.randint(2,3)
		#print(' ')
		#print('the number of links is: ' +str(self.numLinks-1))
		#print(' ')
		
		#for i in range(1,self.numLinks):
			#if random.random()<0.5:
			#	self.randMatName = "Blue"
			#	self.randColStr = "0 0 1 1"
			#else:
			#	self.randMatName = "Green"
			#	self.randColStr = "0 1 0 1"
			#self.randSizeX = random.uniform(0.5,2.5)
			#self.randSizeY = random.uniform(0.5,2.5)
			#self.randSizeZ = random.uniform(0.5,2.5)
			#self.randLinkPosX = self.randSizeX/2
			#self.randLinkPosY = self.randSizeY
			#self.randLinkPosZ = self.randSizeZ
			#self.randJointPosX = self.randSizeX
			#self.randJointPosY = self.randSizeY/2
			#self.randJointPosZ = self.randSizeZ
			#self.randMass = 1 #random.uniform(0,5)
			#self.randJointType = random.choice(["revolute","prismatic","spherical","fixed"])
		
			#if i == 1:
			#	pyrosim.Send_Cube(name='link1', pos=[self.randLinkPosX,0,self.randSizeZ] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
			#	pyrosim.Send_Joint( name = 'link1_link'+str(i+1) , parent='link1', child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,self.randSizeZ], jointAxis = "0 1 0")
			#	
			#	pyrosim.Send_Joint(name = 'link1_arm1_plusY' , parent='link1', child ='arm1_plusY' , type = "revolute", position = [self.randJointPosX/2,self.randJointPosY,self.randJointPosZ], jointAxis = "0 0 1")
			#	pyrosim.Send_Cube(name='arm1_plusY', pos=[0,1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")

			#	pyrosim.Send_Joint(name = 'link1_arm1_negY' , parent='link1', child ='arm1_negY' , type = "revolute", position = [self.randJointPosX/2,-self.randJointPosY,self.randJointPosZ], jointAxis = "0 0 1")
			#	pyrosim.Send_Cube(name='arm1_negY', pos=[0,-1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")

			#	#if self.randMatName == "Green":
			#	#	self.sensorList[i] = 'link'+str(i)
			#	#self.motorList['joint'+str(i)] = 'link1_link'+str(i+1)
			#if i != 1 and i != self.numLinks:
			#	pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
			#	pyrosim.Send_Cube(name='arm'+str(i)+'_plusY', pos=[0,1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
			#	pyrosim.Send_Cube(name='arm'+str(i)+'_negY', pos=[0,-1,0] , size=[0.5,2,0.5], mass=1, materialName="Green", colorString="0 1 0 1", rpy="0 0 0")
			#	#if self.randMatName == "Green":
			#	#	self.sensorList[i] = 'link'+str(i)
			#if i != 1 and i != self.numLinks-1:
			#	pyrosim.Send_Joint( name = 'link'+str(i)+'_link'+str(i+1) , parent='link'+str(i), child ='link'+str(i+1), type = "revolute", position = [self.randJointPosX,0,0], jointAxis = "0 1 0")
			#	pyrosim.Send_Joint(name = 'link'+str(i)+'_arm'+str(i)+'_plusY' , parent='link'+str(i), child ='arm'+str(i)+'_plusY' , type = "revolute", position = [self.randJointPosX/2,self.randJointPosY,self.randJointPosZ], jointAxis = "0 0 1")
			#	pyrosim.Send_Joint(name = 'link'+str(i)+'_arm'+str(i)+'_negY' , parent='link'+str(i), child ='arm'+str(i)+'_negY' , type = "revolute", position = [self.randJointPosX/2,-self.randJointPosY,self.randJointPosZ], jointAxis = "0 0 1")
			#	#self.motorList['joint'+str(i)] = 'link'+str(i)+'_link'+str(i+1)
			#if i == self.numLinks:
			#	pyrosim.Send_Cube(name='link'+str(i), pos=[self.randLinkPosX,0,0] , size=[self.randSizeX,self.randSizeY,self.randSizeZ], mass=self.randMass, materialName=self.randMatName, colorString=self.randColStr, rpy="0 0 0")
			#	#if self.randMatName == "Green":
			#	#	self.sensorList[i] = 'link'+str(i)



