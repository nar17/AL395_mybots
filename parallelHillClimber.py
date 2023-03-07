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
		self.bestGenFitnessList.append(0)
		

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
			print("parent fitness: "+str(self.parents[i].fitness)+", Children fitness: "+str(self.children[i].fitness))
		
		print(" ")
		print(" ")
		

	def Select(self):
		self.parentsFitnessesList = []
		
		for i in self.parents.keys():
		#newA7
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]
			self.parentsFitnessesList.append(self.parents[i].fitness)
			self.bestGenFitness = min(self.parentsFitnessesList)
		self.bestGenFitnessList.append(self.bestGenFitness)
		

	def Save_Fitness_Data_CONTROL(self):
		if c.randomSeed == 0:
			self.fitness_Zero_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_CONTROL','fitness_Zero_Seed_CONTROL'), self.fitness_Zero_Seed)
		elif c.randomSeed == 1:
			self.fitness_First_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_CONTROL','fitness_First_Seed_CONTROL'), self.fitness_First_Seed)
		elif c.randomSeed == 2:
			self.fitness_Second_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_CONTROL','fitness_Second_Seed_CONTROL'), self.fitness_Second_Seed)
		elif c.randomSeed == 3:
			self.fitness_Third_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_CONTROL','fitness_Third_Seed_CONTROL'), self.fitness_Third_Seed)
		else:
			self.fitness_Fourth_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_CONTROL','fitness_Fourth_Seed_CONTROL'), self.fitness_Fourth_Seed)


	def Save_Fitness_Data_EXPERI(self):
		if c.randomSeed == 0:
			self.fitness_Zero_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_EXPERI','fitness_Zero_Seed_EXPERI'), self.fitness_Zero_Seed)
		elif c.randomSeed == 1:
			self.fitness_First_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_EXPERI','fitness_First_Seed_EXPERI'), self.fitness_First_Seed)
		elif c.randomSeed == 2:
			self.fitness_Second_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_EXPERI','fitness_Second_Seed_EXPERI'), self.fitness_Second_Seed)
		elif c.randomSeed == 3:
			self.fitness_Third_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_EXPERI','fitness_Third_Seed_EXPERI'), self.fitness_Third_Seed)
		else:
			self.fitness_Fourth_Seed = numpy.array(self.bestGenFitnessList)*-1
			numpy.save(os.path.join('finalProjectData_EXPERI','fitness_Fourth_Seed_EXPERI'), self.fitness_Fourth_Seed)

		


	def Show_First(self):
		self.parents[0].Start_Simulation('GUI')
		self.parents[0].Wait_For_Simulation_To_End('GUI')

	def Show_Best(self):
		parent_fitnesses = []
		
		for i in self.parents:
			parent_fitnesses.append(self.parents[i].fitness)
		bestFitness = parent_fitnesses.index(min(parent_fitnesses))
		self.parents[bestFitness].Start_Simulation('GUI')
