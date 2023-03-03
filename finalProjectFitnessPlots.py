import os
import numpy
import matplotlib.pyplot
import constants as c

#CONTROL
seedZero = numpy.load("finalProjectData_CONTROL/fitness_Zero_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedZero, linewidth=3, label='Seed 0')

seedOne = numpy.load("finalProjectData_CONTROL/fitness_First_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedOne, linewidth=3, label='Seed 1')

seedTwo = numpy.load("finalProjectData_CONTROL/fitness_Second_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=3, label='Seed 2')

seedThree = numpy.load("finalProjectData_CONTROL/fitness_Third_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedThree, linewidth=3, label='Seed 3')

seedFour = numpy.load("finalProjectData_CONTROL/fitness_Fourth_Seed_CONTROL.npy")
matplotlib.pyplot.plot(seedFour, linewidth=3, label='Seed 4')

#EXPERIMENTAL
seedZero = numpy.load("finalProjectData_EXPERI/fitness_Zero_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedZero, linewidth=4.5, label='Seed 0', linestyle='dashed')

seedOne = numpy.load("finalProjectData_EXPERI/fitness_First_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedOne, linewidth=4.5, label='Seed 1', linestyle='dashed')

seedTwo = numpy.load("finalProjectData_EXPERI/fitness_Second_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=4.5, label='Seed 2', linestyle='dashed')

seedThree = numpy.load("finalProjectData_EXPERI/fitness_Third_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedThree, linewidth=4.5, label='Seed 3', linestyle='dashed')

seedFour = numpy.load("finalProjectData_EXPERI/fitness_Fourth_Seed_EXPERI.npy")
matplotlib.pyplot.plot(seedFour, linewidth=4.5, label='Seed 4', linestyle='dashed')


font = {'family':'MingLiU-ExtB', 'color':'black', 'weight':'normal', 'size': 16}
matplotlib.pyplot.title('Final Project: Robot Evolution Fitness', fontdict=font)
matplotlib.pyplot.xlabel('Number of Generations = '+str(c.numberOfGenerations), fontdict=font)
matplotlib.pyplot.ylabel('fitness (movement in -x direction)', fontdict=font)
matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()

