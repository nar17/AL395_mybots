import numpy
import random

randomSeed = 5678
numpyRandomSeed = 5678


numberOfGenerations = 11
populationSize = 1

numSensorNeurons = 2 #4 #9
numMotorNeurons = 2 #8 #8

motorJointRange = 0.8
motormaxForce = 750

numSteps = 1000
timeSleep = 1/100
xNum = numpy.pi






###########################unused##########################################
#Links
length = 1
width = 1
height = 1

#backleg
amplitude_BL = numpy.pi/3
frequency_BL = 10
phaseOffset_BL = numpy.pi/4

#frontleg
amplitude_FL = numpy.pi/4
frequency_FL = 10
phaseOffset_FL = 0

amplitude = numpy.pi/4
frequency = 1
phaseOffset = 0