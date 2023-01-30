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
			time.sleep(0.01)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(fitnessFile.read())
		fitnessFile.close()
		#print(self.fitness)
		os.system("del fitness" + str(self.myID) + ".txt")
		

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[-3,+3,0.5] , size=[c.length,c.width,c.height])
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="torso", pos=[0,0,1] , size=[c.length,c.width,c.height])
		pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [1,0,1])
		pyrosim.Send_Cube(name="frontleg", pos=[-0.5,0,-0.5] , size=[c.length,c.width,c.height])
		pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [2,0,1])
		pyrosim.Send_Cube(name="backleg", pos=[0.5,0,-0.5] , size=[c.length,c.width,c.height])
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backleg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "frontleg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "torso_backleg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "torso_frontleg")
		for currentRow in range(0,c.numSensorNeurons):
			for currentColumn in range(0,c.numMotorNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)
		pyrosim.End()

	def Mutate(self):
		randomRow = random.randint(0,c.numSensorNeurons-1)
		randomColumn = random.randint(0,c.numMotorNeurons-1)
		self.weights[randomRow,randomColumn] = random.random() * 2 - 1
		#exit()

	def Set_ID(self, ID):
		self.myID = ID


	