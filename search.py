import os
import random
import constants as c
import numpy
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#for i in range(5):
#	os.system("py generate.py")
#	os.system("py simulate.py")

random.seed(c.randomSeed)
numpy.random.seed(c.numpyRandomSeed)

phc = PARALLEL_HILL_CLIMBER()
phc.Show_First()
phc.Evolve()
#phc.Save_Fitness_Data_CONTROL()
#phc.Save_Fitness_Data_EXPERI()
phc.Show_Best()