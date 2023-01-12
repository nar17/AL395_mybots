import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValuesData.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValuesData.npy")

matplotlib.pyplot.plot(backLegSensorValues, linewidth=3, label='Back Leg')
matplotlib.pyplot.plot(frontLegSensorValues, linewidth=2, label='Front Leg')
matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()