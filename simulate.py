import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import os

pi = 3.14159265359

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for i in range (1000):
	p.stepSimulation()
	time.sleep(1/60)
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_backleg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-pi/2, pi/2), maxForce = 50)
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_frontleg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-pi/2, pi/2), maxForce = 50)

numpy.save(os.path.join('data', 'backLegSensorValuesData'), backLegSensorValues)
numpy.save(os.path.join('data', 'frontLegSensorValuesData'), frontLegSensorValues)

p.disconnect()

#print(backLegSensorValues)
#print(frontLegSensorValues)