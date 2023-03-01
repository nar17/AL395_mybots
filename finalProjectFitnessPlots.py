import os
import numpy
import matplotlib.pyplot
import constants as c

seedZero = numpy.load("EightData/fitness_Zero_Seed.npy")
matplotlib.pyplot.plot(seedZero, linewidth=3, label='Seed 0')

seedOne = numpy.load("EightData/fitness_First_Seed.npy")
matplotlib.pyplot.plot(seedOne, linewidth=3, label='Seed 1')

seedTwo = numpy.load("EightData/fitness_Second_Seed.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=3, label='Seed 2')

seedThree = numpy.load("EightData/fitness_Third_Seed.npy")
matplotlib.pyplot.plot(seedThree, linewidth=3, label='Seed 3')

seedFour = numpy.load("EightData/fitness_Fourth_Seed.npy")
matplotlib.pyplot.plot(seedFour, linewidth=3, label='Seed 4')



font = {'family':'MingLiU-ExtB', 'color':'black', 'weight':'normal', 'size': 16}
matplotlib.pyplot.title('Assignment 8: Robot Evolution Fitness', fontdict=font)
matplotlib.pyplot.xlabel('Number of Generations = '+str(c.numberOfGenerations), fontdict=font)
matplotlib.pyplot.ylabel('fitness (movement in -x direction)', fontdict=font)
matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()

