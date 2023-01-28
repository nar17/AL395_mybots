import constants as c
import copy
import os
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		os.system("del brain*.nndf")
		os.system("del fitness*.nndf")
		self.parents = {}
		self.nextAvailableID = 0
		for i in range(0, c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID+1
		

	def Evolve(self):
		#for i in self.parents:
		#	self.parents[i].Start_Simulation('DIRECT')
		#for i in self.parents:
		#	self.parents[i].Wait_For_Simulation_To_End('DIRECT')
		self.Evaluate(self.parents)
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		#self.Select()
		self.Print()
		exit()

	def Spawn(self):
		self.children = {}
		for parent_key in self.parents.keys():
			self.children[parent_key] = copy.deepcopy(self.parents[parent_key])
			self.children[parent_key].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID+1

	def Mutate(self):
		self.children.keys()		#potential

	def Evaluate(self, solutions):
		self.solutions = solutions	#potential
		for i in solutions:
			solutions[i].Start_Simulation('GUI')
		for i in solutions:
			solutions[i].Wait_For_Simulation_To_End('GUI')

	def Select(self):
		if self.parent.fitness > self.child.fitness:
			self.parent = self.child

	def Print(self):
		for i in self.parents.keys():
			print("Parent fitness:"+str(self.parents[i].fitness)+", Children fitness:"+str(self.children[i].fitness))

	def Show_Best(self):
		#os.system("py simulate.py GUI")
		#self.Print()
		pass
