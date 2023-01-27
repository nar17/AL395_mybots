import constants as c
import copy
import os
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		self.parents = {}
		for i in (0, c.populationSize-1):
			self.parents[i] = SOLUTION()
		

	def Evolve(self):
		for i in self.parents:
			self.parents[i].Evaluate('GUI')
		#for currentGeneration in range(c.numberOfGenerations):
		#	self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.child.Evaluate('DIRECT')
		self.Select()
		self.Print()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		self.child.Mutate()

	def Select(self):
		if self.parent.fitness > self.child.fitness:
			self.parent = self.child

	def Print(self):
		print(self.parent.fitness, self.child.fitness)

	def Show_Best(self):
		#os.system("py simulate.py GUI")
		#self.Print()
		pass
		