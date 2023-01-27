import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import os
import constants as c
import sys

from world import WORLD
from robot import ROBOT

class SIMULATION:

	def __init__(self, directOrGUI, solutionID):
		self.directOrGUI = directOrGUI
		if directOrGUI == 'DIRECT':
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)

		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		
		self.world = WORLD()		
		self.robot = ROBOT(solutionID)
		
	def Run(self):
		for t in range (1000):
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Think()
			self.robot.Act(t)
			if self.directOrGUI != 'DIRECT':
				time.sleep(1/100)

	def Get_Fitness(self):
		self.robot.Get_Fitness()

	def __del__(self):
		p.disconnect()
		


	
		
		
