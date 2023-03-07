import os
import numpy
import matplotlib.pyplot
import constants as c

#CONTROL
seedZero = numpy.load("finalProjectData_CONTROL/fitness_Zero_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedZero, linewidth=3, label='Seed 0: Control', color='y')

seedOne = numpy.load("finalProjectData_CONTROL/fitness_First_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedOne, linewidth=3, label='Seed 1: Control', color='g')

seedTwo = numpy.load("finalProjectData_CONTROL/fitness_Second_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=3, label='Seed 2: Control', color='r')

seedThree = numpy.load("finalProjectData_CONTROL/fitness_Third_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedThree, linewidth=3, label='Seed 3: Control', color='c')

seedFour = numpy.load("finalProjectData_CONTROL/fitness_Fourth_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedFour, linewidth=3, label='Seed 4: Control', color='k')

#EXPERIMENTAL
seedZero = numpy.load("finalProjectData_EXPERI/fitness_Zero_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedZero, linewidth=3, label='Seed 0: Exp.', linestyle='dashed', color='y')

seedOne = numpy.load("finalProjectData_EXPERI/fitness_First_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedOne, linewidth=3, label='Seed 1: Exp.', linestyle='dashed', color='g')

seedTwo = numpy.load("finalProjectData_EXPERI/fitness_Second_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=3, label='Seed 2: Exp.', linestyle='dashed', color='r')

seedThree = numpy.load("finalProjectData_EXPERI/fitness_Third_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedThree, linewidth=3, label='Seed 3: Exp.', linestyle='dashed', color='c')

seedFour = numpy.load("finalProjectData_EXPERI/fitness_Fourth_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedFour, linewidth=3, label='Seed 4: Exp.', linestyle='dashed', color='k')


font = {'family':'MingLiU-ExtB', 'color':'black', 'weight':'normal', 'size': 16}
matplotlib.pyplot.title('Evolution Fitness Plot', fontdict=font)
matplotlib.pyplot.xlabel('Number of Generations = 200 --> Population Size = 25 per Generation', fontdict=font)
matplotlib.pyplot.ylabel('fitness (locomotion in -x direction)', fontdict=font)
matplotlib.pyplot.legend(bbox_to_anchor=(1.01,1), loc='best', borderaxespad=0, shadow=True)
matplotlib.pyplot.show()

