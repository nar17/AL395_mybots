import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)

for i in range (1000):
	p.stepSimulation()
	time.sleep(1/60)
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")

numpy.save(os.path.join('data', 'backLegSensorValuesData'), backLegSensorValues)

p.disconnect()

print(backLegSensorValues)

