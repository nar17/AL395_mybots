import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import os
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:

	def __init__(self):
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		
		self.world = WORLD()		
		self.robot = ROBOT()
		
	def Run(self):
		for i in range (1000):
			p.stepSimulation()
			time.sleep(1/60)
			#backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
			#frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
			#pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_backleg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_BL[i], maxForce = 50)
			#pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_frontleg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_FL[i], maxForce = 50)
			print (i)
		


	
		
		
