import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
		self.myID = nextAvailableID
		
	def Evaluate(self, directOrGUI):
		#self.Create_World()
		#self.Create_Body()
		#self.Create_Brain()
		#self.directOrGUI = directOrGUI
		#os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		#while not os.path.exists("fitness" + str(self.myID) + ".txt"):
		#	time.sleep(0.01)
		#fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		#self.fitness = float(fitnessFile.read())
		#print(self.fitness)
		#fitnessFile.close()
		pass
		

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		self.directOrGUI = directOrGUI
		os.system("start /B py simulate.py " + str(self.directOrGUI) + " " + str(self.myID))
		

	def Wait_For_Simulation_To_End(self, directOrGUI):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		#self.overallFitness = fitnessFile.readlines()
		self.xfitness = float(fitnessFile.read())
		#self.xfitness = float(self.overallFitness[0])
		#self.yfitness = float(self.overallFitness[1])
		#self.height = float(self.overallFitness[2])
		fitnessFile.close()
		#print(self.fitness)
		os.system("del fitness" + str(self.myID) + ".txt")
		

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
			#miniputt platform
		pyrosim.Send_Cube(name="largeGreen", pos=[0,0,0.5] , size=[16,10,1], mass=1000)
		pyrosim.Send_Cube(name="preHoleGreen", pos=[-9,0,0.5] , size=[2,6,1], mass=1000)
		pyrosim.Send_Cube(name="+yBox", pos=[-11.5,2,0.5] , size=[3,2,1], mass=1000)
		pyrosim.Send_Cube(name="-yBox", pos=[-11.5,-2,0.5] , size=[3,2,1], mass=1000)
		pyrosim.Send_Cube(name="backstopBox", pos=[-12.5,0,0.5] , size=[1,2,1], mass=1000)
		pyrosim.Send_Sphere(name="GolfBall" , pos=[-0.5,0.3,1.5] , size=[0.5], mass = 10)
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		
			#Quadruped
		#pyrosim.Send_Cube(name="torso", pos=[0,0,1] , size=[c.length,c.width,c.height])
		#pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2])
		#pyrosim.Send_Joint( name = "frontleg_frontlowerleg" , parent= "frontleg" , child = "frontlowerleg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="frontlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])				
		#pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
		#pyrosim.Send_Cube(name="backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
		#pyrosim.Send_Joint( name = "backleg_backlowerleg" , parent= "backleg" , child = "backlowerleg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="backlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		#pyrosim.Send_Joint( name = "torso_leftleg" , parent= "torso" , child = "leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
		#pyrosim.Send_Joint( name = "leftleg_leftlowerleg" , parent= "leftleg" , child = "leftlowerleg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="leftlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		#pyrosim.Send_Joint( name = "torso_rightleg" , parent= "torso" , child = "rightleg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2])
		#pyrosim.Send_Joint( name = "rightleg_rightlowerleg" , parent= "rightleg" , child = "rightlowerleg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
		#pyrosim.Send_Cube(name="rightlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])	
		
			#golfer
		pyrosim.Send_Cube(name="torso", pos=[0,-3,3] , size=[1,1,3], mass=1000.0, materialName="Red", colorString="1 0 0 1")

		pyrosim.Send_Joint( name = "torso_arm" , parent= "torso" , child = "arm" , type = "revolute", position = [0,-2.5,4], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="arm", pos=[0,1.25,-1/6] , size=[1/3,2.5,1/3], materialName="Tan", colorString="1.3 0.94 0.92 1")
		pyrosim.Send_Joint( name = "arm_club" , parent= "arm" , child = "club" , type = "fixed", position = [0,2.5,0], jointAxis = "1 0 0")		
		pyrosim.Send_Cube(name="club", pos=[0,1/6,-1.5] , size=[1/3,1/3,2.8], materialName="Gray", colorString="1 1 1 1")
		pyrosim.Send_Joint( name = "torso_hip" , parent= "torso" , child = "hip" , type = "revolute", position = [0,-3,1.75], jointAxis = "0 0 1")		
		pyrosim.Send_Cube(name="hip", pos=[0,0,-0.5] , size=[1, 1, 0.5], mass=10000.0, materialName="Brown", colorString="0.7 0.6 0.5 1")
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		
			#quadruped all sensors 
		#pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
		#pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backleg")
		#pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "backlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "frontleg")
		#pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "frontlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "leftleg")
		#pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "leftlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "rightleg")
		#pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "rightlowerleg")	
		#pyrosim.Send_Motor_Neuron( name = 9 , jointName = "torso_backleg")
		#pyrosim.Send_Motor_Neuron( name = 10 , jointName = "backleg_backlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 11 , jointName = "torso_frontleg")
		#pyrosim.Send_Motor_Neuron( name = 12 , jointName = "frontleg_frontlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 13 , jointName = "torso_leftleg")
		#pyrosim.Send_Motor_Neuron( name = 14 , jointName = "leftleg_leftlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 15 , jointName = "torso_rightleg")
		#pyrosim.Send_Motor_Neuron( name = 16 , jointName = "rightleg_rightlowerleg")
			#quadruped sensors only on lower legs
		#pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "backlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "frontlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "leftlowerleg")	
		#pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "rightlowerleg")	
		#pyrosim.Send_Motor_Neuron( name = 4 , jointName = "torso_backleg")
		#pyrosim.Send_Motor_Neuron( name = 5 , jointName = "backleg_backlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 6 , jointName = "torso_frontleg")
		#pyrosim.Send_Motor_Neuron( name = 7 , jointName = "frontleg_frontlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 8 , jointName = "torso_leftleg")
		#pyrosim.Send_Motor_Neuron( name = 9 , jointName = "leftleg_leftlowerleg")
		#pyrosim.Send_Motor_Neuron( name = 10 , jointName = "torso_rightleg")
		#pyrosim.Send_Motor_Neuron( name = 11 , jointName = "rightleg_rightlowerleg")

			#golfer
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "club")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "hip")
		pyrosim.Send_Motor_Neuron(name=2, jointName = "torso_arm")
		pyrosim.Send_Motor_Neuron(name=3, jointName = "torso_hip")
	
		for currentRow in range(0,c.numSensorNeurons):
			for currentColumn in range(0,c.numMotorNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] ) #weight = random.random() #weight = random.uniform(-1,1)
		pyrosim.End()
		#exit()
		
	

	def Mutate(self):
		randomRow = random.randint(0,c.numSensorNeurons-1)
		randomColumn = random.randint(0,c.numMotorNeurons-1)
		self.weights[randomRow,randomColumn] = random.random() * 2 - 1
		#exit()

	def Set_ID(self, ID):
		self.myID = ID


	