import pybullet as p

class WORLD:

	def __init__(self):
		#p.loadSDF("world.sdf")
		self.objects = p.loadSDF("world.sdf")
		self.planeId = p.loadURDF("plane.urdf")
		
	def Get_Pos_And_Orientation(self):
		posAndOrientation = p.getBasePositionAndOrientation(self.objects[5])
		position = posAndOrientation[0]
		xPosition = position[0]
		yPosition = position[1]
		height = position[2]
		print(xPosition)
		



				