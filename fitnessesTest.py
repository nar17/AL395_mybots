import numpy
import matplotlib.pyplot
import constants as c
import os

fitnesses = numpy.zeros(c.numberOfGenerations*c.populationSize)
poopy = numpy.zeros(c.numberOfGenerations*c.populationSize)

for i in range(c.numberOfGenerations*c.populationSize):
	fitnesses[i] = 1/(i+1)
	poopy[i] = 6/(i**2+1)

numpy.save(os.path.join('data', 'fitnesses'), fitnesses)
numpy.save(os.path.join('data', 'poopy'), poopy)

X = numpy.load("data/fitnesses.npy")
Y = numpy.load("data/poopy.npy")

#matplotlib.pyplot.scatter(X,Y)
matplotlib.pyplot.plot(Y,X, linewidth=3, linestyle='dashed', label='Back Leg')
matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()