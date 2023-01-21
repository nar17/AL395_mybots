import pyrosim.pyrosim as pyrosim
import random
import constants as c


def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[-3,+3,0.5] , size=[c.length,c.width,c.height])
	pyrosim.End()

def Create_Robot():
	pass

Create_World()
Create_Robot()


def Generate_Body():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="torso", pos=[1.5,0,1.5] , size=[c.length,c.width,c.height])
	pyrosim.Send_Joint( name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [1,0,1])
	pyrosim.Send_Cube(name="frontleg", pos=[-0.5,0,-0.5] , size=[c.length,c.width,c.height])
	pyrosim.Send_Joint( name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [2,0,1])
	pyrosim.Send_Cube(name="backleg", pos=[0.5,0,-0.5] , size=[c.length,c.width,c.height])
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backleg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "frontleg")
	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "torso_backleg")
	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "torso_frontleg")

	for i in range(0,3):
		for j in range(3,5):
			pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = random.uniform(-1,1) ) #weight = random.random() #weight = random.uniform(-1,1)



	#pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
	#pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1.0 )
	#pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1.0 )
	#pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )
	#pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
	#pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )

	
	pyrosim.End()

Generate_Body()
Generate_Brain()