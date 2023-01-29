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
		self.Print()
		self.Select()

	def Spawn(self):
		self.children = {}
		for parent_key in self.parents.keys():
			self.children[parent_key] = copy.deepcopy(self.parents[parent_key])
			self.children[parent_key].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID+1

	def Mutate(self):
		for child in self.children.keys():
			self.children[child].Mutate()

	def Evaluate(self, solutions):
		self.solutions = solutions
		for i in range(c.populationSize):
			solutions[i].Start_Simulation('DIRECT')
		for i in range(c.populationSize):
			solutions[i].Wait_For_Simulation_To_End('DIRECT')

	def Print(self):
		print(" ")
		print(" ")
		for i in self.parents.keys():	#potential
			print("Parent fitness: "+str(self.parents[i].fitness)+", Children fitness: "+str(self.children[i].fitness))
		print(" ")
		print(" ")

	def Select(self):
		for i in self.parents.keys():
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]

	def Show_Best(self):
		parent_fitnesses = []
		for i in self.parents:
			parent_fitnesses.append(self.parents[i].fitness)
		bestFitness = parent_fitnesses.index(min(parent_fitnesses))
		self.parents[bestFitness].Start_Simulation('GUI')

		#for i in self.parents:
		#	self.parents[i].fitness = apple
		#	self.parents[i].fitness = peach
		#	if apple < peach:
		#		yellow = apple
		#self.parents[yellow].Start_Simulation('GUI')
		
		#os.system("py simulate.py GUI")
		#self.Print()
