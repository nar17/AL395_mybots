import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.myID = nextAvailableID
		self.New_A7_Lists()

		self.countSensors = self.LmatList.count("Green")*2-1
		self.countHidden = self.countSensors
		self.countMotors = self.numJoints_A7*2

		#Control
		#self.weights = numpy.random.rand(self.countSensors,self.countMotors) * 2 - 1

		#Experi (with hidden layer)
		self.weights_Sensors2HiddenOne = numpy.random.rand(self.countSensors,self.countHidden) * 2 - 1
		self.weights_HiddenOne2HiddenTwo = numpy.random.rand(self.countHidden,self.countHidden) * 2 - 1
		self.weights_HiddenTwo2Motor = numpy.random.rand(self.countHidden,self.countMotors) * 2 - 1
		

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		#self.Create_Brain_Control()
		self.Create_Brain_Experi()
		self.directOrGUI = directOrGUI
		os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		

	def Wait_For_Simulation_To_End(self, directOrGUI):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.03)
			
			#quadruped fitness
		fitnessFile=open("fitness"+str(self.myID)+".txt","r")
		self.fitness = float(fitnessFile.read())
		
		fitnessFile.close()
		os.system("del fitness" + str(self.myID) + ".txt")
		#os.system("del body" + str(self.myID) + ".urdf")
		#os.system("del brain" + str(self.myID) + ".nndf")
		

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
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
		self.numLinks_A7=random.randint(3,4)+1
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
		for i in range(1,len(self.LnameListNPP)):
			pyrosim.Send_Cube(name=self.LnameListNPP[i], pos=self.LPosListNPP[i-1], size=[self.X[i-1],self.Y[i-1],self.Z[i-1]], mass=1, materialName=self.LmatList[i], colorString=self.LcolorStringList[i], rpy="0 0 0")
			if self.LmatList[i] == "Green":
				self.sensorList.append(self.LnameListNPP[i])
		#NNPlinks
		for i in range(1,len(self.LnameListNNP)):
			pyrosim.Send_Cube(name=self.LnameListNNP[i], pos=self.LPosListNNP[i-1], size=[self.X[i-1],self.Y[i-1],self.Z[i-1]], mass=1, materialName=self.LmatList[i], colorString=self.LcolorStringList[i], rpy="0 0 0")
			if self.LmatList[i] == "Green":
				self.sensorList.append(self.LnameListNNP[i])
		#NPPjoints
		for i in range(1,len(self.JnameListNPP)):
			pyrosim.Send_Joint(name=self.JnameListNPP[i], parent=self.JparentListNPP[i], child=self.JchildListNPP[i], type="revolute", position=self.JPosListNPP[i], jointAxis=self.JaxisList[i]) #[0,self.JposList[i-1],0]
			self.motorList.append(self.JnameListNPP[i])
		#NNPjoints
		for i in range(1,len(self.JnameListNNP)):
			pyrosim.Send_Joint(name=self.JnameListNNP[i], parent=self.JparentListNNP[i], child=self.JchildListNNP[i], type="revolute", position=self.JPosListNNP[i], jointAxis=self.JaxisList[i]) #[0,self.JposList[i-1],0]
			self.motorList.append(self.JnameListNNP[i])


	def Create_Body(self):
		pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
		#if self.listID==0:
		#	self.New_A7_Lists()
		self.New_A7_Generator()
		pyrosim.End()


	def Create_Brain_Control(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")	

		for i in range(len(self.sensorList)):
			pyrosim.Send_Sensor_Neuron(name = self.neuronId, linkName = self.sensorList[i])
			self.neuronId +=1
		for i in range(len(self.motorList)):
			pyrosim.Send_Motor_Neuron(name = self.neuronId, jointName = self.motorList[i])
			self.neuronId +=1

			#synapse with no hidden neurons
		for currentRow in range(len(self.sensorList)):
			for currentColumn in range(len(self.motorList)):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.sensorList) , weight = self.weights[currentRow][currentColumn])

		self.neuronId = 0
		pyrosim.End()


	def Create_Brain_Experi(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")	

		self.numHiddenNeurons = len(self.sensorList)

		for i in range(len(self.sensorList)):
			pyrosim.Send_Sensor_Neuron(name = self.neuronId, linkName = self.sensorList[i])
			self.neuronId +=1
		for i in range(len(self.motorList)):
			pyrosim.Send_Motor_Neuron(name = self.neuronId, jointName = self.motorList[i])
			self.neuronId +=1
		#hiddenOne
		for i in range(self.numHiddenNeurons):
			pyrosim.Send_Hidden_Neuron(name = self.neuronId)
			self.neuronId +=1
		#hiddenTwo
		for i in range(self.numHiddenNeurons):
			pyrosim.Send_Hidden_Neuron(name = self.neuronId)
			self.neuronId +=1

		#synapses with hidden neurons
			#sensor to hiddenOne
		for currentRow in range(len(self.sensorList)):
			for currentColumn in range(self.numHiddenNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+len(self.sensorList)+len(self.motorList) , weight = self.weights_Sensors2HiddenOne[currentRow][currentColumn] )

			#hiddenOne to hiddenTwo
		for currentRow in range(self.numHiddenNeurons):
			for currentColumn in range(self.numHiddenNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow+len(self.sensorList)+len(self.motorList) , targetNeuronName = currentColumn+len(self.sensorList)+len(self.motorList)+self.numHiddenNeurons , weight = self.weights_HiddenOne2HiddenTwo[currentRow][currentColumn] ) 

			#hiddenTwo to Motor
		for currentRow in range(self.numHiddenNeurons):
			for currentColumn in range(len(self.motorList)):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow+len(self.sensorList)+len(self.motorList)+self.numHiddenNeurons , targetNeuronName = currentColumn+len(self.sensorList) , weight = self.weights_HiddenTwo2Motor[currentRow][currentColumn] ) 


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
		
		#self.Mutate_Synapses_Control()
		self.Mutate_Synapses_Experi()


	def Mutate_Synapses_Control(self):

		self.countSensors = self.LmatList.count("Green")*2-1
		self.countMotors = self.numJoints_A7*2
		self.weights = numpy.random.rand(self.countSensors,self.countMotors) * 2 - 1
		

	def Mutate_Synapses_Experi(self):
		
		self.countSensors = self.LmatList.count("Green")*2-1
		self.countHidden = self.countSensors
		self.countMotors = self.numJoints_A7*2
		self.weights_Sensors2HiddenOne = numpy.random.rand(self.countSensors,self.countHidden) * 2 - 1
		self.weights_HiddenOne2HiddenTwo = numpy.random.rand(self.countHidden,self.countHidden) * 2 - 1
		self.weights_HiddenTwo2Motor = numpy.random.rand(self.countHidden,self.countMotors) * 2 - 1

	
	def Mutate_Joint_Axis(self):
		self.linkListIndex = random.randint(0,self.numLinks_A7-2) #having error here.. just subtracted another 1 ?
		self.JaxisList[self.linkListIndex]=random.choice(["1 0 0", "0 1 0", "0 0 1"])


	def Mutate_Sensor_Placement(self):
		self.linkListIndex = random.randint(1,self.numLinks_A7-1)

		if self.LmatList[self.linkListIndex] == "Green":
			self.LmatList[self.linkListIndex] = "Blue"
			self.LcolorStringList[self.linkListIndex] = "0 0 1 1"
			self.sensorList.remove(self.sensorList[0])
		else:
			self.LmatList[self.linkListIndex] = "Green"
			self.LcolorStringList[self.linkListIndex] = "0 1 0 1"
			self.sensorList.append("Green")


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

	
	def Set_ID(self, ID):
		self.myID = ID
