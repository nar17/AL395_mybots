import os
import numpy
import matplotlib.pyplot

seedZero = numpy.load("EightData/fitness_Zero_Seed.npy")
matplotlib.pyplot.plot(seedZero, linewidth=3)

seedOne = numpy.load("EightData/fitness_First_Seed.npy")
matplotlib.pyplot.plot(seedOne, linewidth=3)

seedTwo = numpy.load("EightData/fitness_Second_Seed.npy")
matplotlib.pyplot.plot(seedTwo, linewidth=3)

seedThree = numpy.load("EightData/fitness_Third_Seed.npy")
matplotlib.pyplot.plot(seedThree, linewidth=3)

seedFour = numpy.load("EightData/fitness_Fourth_Seed.npy")
matplotlib.pyplot.plot(seedFour, linewidth=3)

matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()