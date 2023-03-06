import os
import random
import constants as c
import numpy
from parallelHillClimber import PARALLEL_HILL_CLIMBER




phc = PARALLEL_HILL_CLIMBER()
phc.Show_First()
phc.Evolve()
#phc.Save_Fitness_Data_CONTROL()
#phc.Save_Fitness_Data_EXPERI()
phc.Show_Best()




# To change between Control and Experi, make sure the following is commented/uncommented:
#
#___File/Method_________________Control_____________________________________Experimental____________________________________
#	search.py:					phc.Save_Fitness_Data_CONTROL()				phc.Save_Fitness_Data_EXPERI()
#	solution.py:
#		__init__:				self.weights								self.weights_Sensors2HiddenOne,self.weights_HiddenOne2HiddenTwo,self.weights_HiddenTwo2HiddenThree,self.weights_HiddenThree2Motor
#		Start_Simulation:		self.Create_Brain_Control()					self.Create_Brain_Experi()
#		Mutate:					self.Mutate_Synapses_Control()				self.Mutate_Synapses_Experi()

