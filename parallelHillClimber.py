import constants as c
import copy
import os
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		self.parents = {}
		self.nextAvailableID = 0
		for i in range(0, c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID+1
		os.system("del brain" + str(self.nextAvailableID) + ".nndf") #not correct yet
		os.system("del fitness" + str(self.nextAvailableID) + ".txt") #not correct yet 
		

	def Evolve(self):
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
		for i in self.parents.keys():
		#mini putt
			#print("Parent fitness: "+str(abs(self.parents[i].xfitness+11)+abs(self.parents[i].yfitness))+", Children fitness: "+str(abs(self.children[i].xfitness+11)+abs(self.children[i].yfitness)))
			print("Parent fitness: "+str(self.parents[i].xfitness+self.parents[i].yfitness)+", Children fitness: "+str(self.children[i].xfitness+self.children[i].yfitness))		
		#furthest drive
			#print("Parent fitness: "+str(self.parents[i].xfitness+abs(self.parents[i].yfitness))+", Children fitness: "+str(self.children[i].xfitness+abs(self.children[i].yfitness)))
		print(" ")
		print(" ")
		

	def Select(self):
		for i in self.parents.keys():
		#mini putt
			if abs(self.parents[i].xfitness+11) > abs(self.children[i].xfitness+11) and abs(self.parents[i].yfitness) > abs(self.children[i].yfitness):
				self.parents[i] = self.children[i]
		#furthest drive
			#if self.parents[i].xfitness > self.children[i].xfitness and abs(self.parents[i].yfitness) > abs(self.children[i].yfitness):
			#	self.parents[i] = self.children[i]

	def Show_First(self):
		self.parents[0].Start_Simulation('GUI')
		self.parents[0].Wait_For_Simulation_To_End('GUI')

	def Show_Best(self):
		parent_fitnesses = []
		for i in self.parents:
			#mini putt
			parent_fitnesses.append(abs(self.parents[i].xfitness+11)+abs(self.parents[i].yfitness))
			#furthest drive
			#parent_fitnesses.append(self.parents[i].xfitness+abs(self.parents[i].yfitness))
		bestFitness = parent_fitnesses.index(min(parent_fitnesses))
		self.parents[bestFitness].Start_Simulation('GUI')
		
