import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import os

#backleg
amplitude_BL = numpy.pi/3
frequency_BL = 10
phaseOffset_BL = numpy.pi/4

#frontleg
amplitude_FL = numpy.pi/4
frequency_FL = 10
phaseOffset_FL = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
targetAngles_BL = (numpy.sin(numpy.linspace(phaseOffset_BL, 2*numpy.pi*frequency_BL+phaseOffset_BL, 1000)))*(amplitude_BL)
targetAngles_FL = (numpy.sin(numpy.linspace(phaseOffset_FL, 2*numpy.pi*frequency_FL+phaseOffset_FL, 1000)))*(amplitude_FL)

for i in range (1000):
	p.stepSimulation()
	time.sleep(1/60)
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_backleg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_BL[i], maxForce = 50)
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'torso_frontleg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_FL[i], maxForce = 50)

#numpy.save(os.path.join('data', 'backLegSensorValuesData'), backLegSensorValues)
#numpy.save(os.path.join('data', 'frontLegSensorValuesData'), frontLegSensorValues)
#numpy.save(os.path.join('data', 'targetAnglesData'), targetAngles)
#numpy.save(os.path.join('data', 'targetAnglesData_BL'), targetAngles_BL)
#numpy.save(os.path.join('data', 'targetAnglesData_FL'), targetAngles_FL)

p.disconnect()


#print(backLegSensorValues)
#print(frontLegSensorValues)