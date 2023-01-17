import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

	def __init__(self):
		self.motors = {}
		self.sensors = {}
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain.nndf")
	
	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, t):
		for neuronName in self.nn.Get_Neuron_Names():
			print(self.neurons)
		#for i in self.motors:
		#	self.motors[i].Set_Value(t, self.robotId)

	def Think(self):
		self.nn.Update()
		self.nn.Print()



