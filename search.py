import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#for i in range(5):
#	os.system("py generate.py")
#	os.system("py simulate.py")

phc = PARALLEL_HILL_CLIMBER()
#phc.Show_First()
phc.Evolve()
phc.Show_Best()