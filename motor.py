import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName
	#	self.Prepare_To_Act()

	#CAN DELETE  def Prepare_To_Act(self):
	#	self.amplitude = c.amplitude
	#	self.frequency = c.frequency
	#	self.phaseOffset = c.phaseOffset
	#	if self.jointName == b'torso_frontleg':
	#		self.frequency = c.frequency / 2
	#	self.motorValues = (numpy.sin(numpy.linspace(self.phaseOffset, 2 * numpy.pi * self.frequency + self.phaseOffset, 1000)))*(self.amplitude)
		

	def Set_Value(self, desiredAngle, robotId):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 1000)

	#CAN DELETE def Save_Values(self):
	#	numpy.save(os.path.join('data', 'ptHMotorValuesData'), self.motorValues)
		