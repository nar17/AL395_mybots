import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import constants as c

from sensor import SENSOR
from motor import MOTOR
from world import WORLD
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

	def __init__(self, solutionID):
		self.motors = {}
		self.sensors = {}
		self.solutionID = solutionID
		#self.robotId = p.loadURDF("body"+str(solutionID)+".urdf")
		self.robotId = p.loadURDF("body4803.urdf") #this is for simulating specific bodies
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		#self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		self.nn = NEURAL_NETWORK("brain4803.nndf")  #this is for simulating specific bodies

	
	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)


	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)


	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)


	def Act(self, jointName):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = (self.nn.Get_Value_Of(neuronName))*c.motorJointRange
				self.motors[jointName].Set_Value(desiredAngle, self.robotId)


	def Think(self):
		self.nn.Update()


	def Get_Fitness(self):
			#fitness = furthest -x position
		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
		basePosition = basePositionAndOrientation[0]
		xPosition = str(basePosition[0])
		fitnessFile = open("tmp" + str(self.solutionID) + ".txt", "w")
		fitnessFile.write(xPosition)
		fitnessFile.close()
		os.system("rename tmp"+str(self.solutionID)+".txt " + "fitness"+str(self.solutionID)+".txt")

