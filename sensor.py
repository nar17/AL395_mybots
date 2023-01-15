import pyrosim.pyrosim as pyrosim
import numpy

class SENSOR:
	def __init__(self, linkName):
		self.linkName = linkName
		self.values = numpy.zeros(1000)

	def Get_Value(self):
		self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
	
