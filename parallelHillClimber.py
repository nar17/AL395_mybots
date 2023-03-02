import constants as c
import copy
import os
import numpy
import matplotlib.pyplot
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		os.system("del body*.urdf")
		os.system("del brain*.nndf")
		os.system("del fitness*.txt")
		
		self.parents = {}
		self.nextAvailableID = 0
		for i in range(0, c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID+1

		self.bestGenFitnessList = []

		
		

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
		
			#quadruped
		for i in self.parents.keys():
			print("parent fitness: "+str(self.parents[i].fitness)+", Children fitness: "+str(self.children[i].fitness))
		
		#golfer
		#for i in self.parents.keys():
		#mini putt
			#print("Parent fitness: "+str(abs(self.parents[i].xfitness+11)+abs(self.parents[i].yfitness))+", Children fitness: "+str(abs(self.children[i].xfitness+11)+abs(self.children[i].yfitness)))
		#furthest drive
			#print("Parent fitness: "+str(self.parents[i].xfitness+abs(self.parents[i].yfitness))+", Children fitness: "+str(self.children[i].xfitness+abs(self.children[i].yfitness)))
		
		print(" ")
		print(" ")
		

	def Select(self):
		self.parentsFitnessesList = []
		for i in self.parents.keys():
		
		#quadruped
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]
			self.parentsFitnessesList.append(self.parents[i].fitness)
			self.bestGenFitness = min(self.parentsFitnessesList)
		self.bestGenFitnessList.append(self.bestGenFitness)
		

		#mini putt
			#if abs(self.parents[i].xfitness+11)+abs(self.parents[i].yfitness) > abs(self.children[i].xfitness+11)+abs(self.children[i].yfitness):
			#	self.parents[i] = self.children[i]
		#furthest drive
			#if self.parents[i].xfitness > self.children[i].xfitness and abs(self.parents[i].yfitness) > abs(self.children[i].yfitness):
			#	self.parents[i] = self.children[i]

	def Save_Fitness_Data(self):
		if c.randomSeed == 0:
			self.fitness_Zero_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData','fitness_Zero_Seed'), self.fitness_Zero_Seed)
		elif c.randomSeed == 1:
			self.fitness_First_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData','fitness_First_Seed'), self.fitness_First_Seed)
		elif c.randomSeed == 2:
			self.fitness_Second_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData','fitness_Second_Seed'), self.fitness_Second_Seed)
		elif c.randomSeed == 3:
			self.fitness_Third_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData','fitness_Third_Seed'), self.fitness_Third_Seed)
		else:
			self.fitness_Fourth_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData','fitness_Fourth_Seed'), self.fitness_Fourth_Seed)

		


	def Show_First(self):
		self.parents[0].Start_Simulation('GUI')
		self.parents[0].Wait_For_Simulation_To_End('GUI')

	def Show_Best(self):
		#print(self.parents)
		#print(self.bestGenFitnessList)
		#self.bestParentGen = self.bestGenFitnessList.index(min(self.bestGenFitnessList))
		#self.parents[self.bestParentGen].Start_Simulation('GUI')

		parent_fitnesses = []
		
			#quadruped fitness
		for i in self.parents:
			parent_fitnesses.append(self.parents[i].fitness)
		bestFitness = parent_fitnesses.index(min(parent_fitnesses))
		self.parents[bestFitness].Start_Simulation('GUI')
		print(bestFitness)

			#golf fitness
		#for i in self.parents:
			#mini putt
			#parent_fitnesses.append(abs(self.parents[i].xfitness+11)+abs(self.parents[i].yfitness))
			#furthest drive
			#parent_fitnesses.append(self.parents[i].xfitness+abs(self.parents[i].yfitness))
		#bestFitness = parent_fitnesses.index(min(parent_fitnesses))
		#self.parents[bestFitness].Start_Simulation('GUI')
