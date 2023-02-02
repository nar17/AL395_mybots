import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR:
	def __init__(self, linkName):
		self.linkName = linkName
		self.values = numpy.zeros(c.numSteps)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		#print(self.values[t==999])

	def Save_Values(self):
		numpy.save(os.path.join('data', 'ptHSensorValuesData'), self.values)
		