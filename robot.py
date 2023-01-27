import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

	def __init__(self, solutionID):
		self.motors = {}
		self.sensors = {}
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		os.system("del brain" + str(solutionID) + ".nndf")
	
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
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].Set_Value(desiredAngle, self.robotId)
				#print(neuronName, jointName, desiredAngle)

	def Think(self):
		self.nn.Update()
		#self.nn.Print()

	def Get_Fitness(self):
		stateOfLinkZero = p.getLinkState(self.robotId,0)
		positionOfLinkZero = stateOfLinkZero[0]  #not sure if this is printing the right position of the link zero (0.5000, 0.000236, 0.4999848)
		xCoordinateOfLinkZero = str(positionOfLinkZero[0])
		#print(xCoordinateOfLinkZero)
		fitnessFile = open("fitness.txt", "w")
		fitnessFile.write(xCoordinateOfLinkZero)




