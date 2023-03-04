import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body123.urdf")
nn = NEURAL_NETWORK("brain123.nndf")
p.loadSDF("world.sdf")

for i in range (1000):
	p.stepSimulation()
	time.sleep(1/60)