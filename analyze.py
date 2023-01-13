import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load("data/backLegSensorValuesData.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorValuesData.npy")
#targetAngles = numpy.load("data/targetAnglesData.npy")
targetAngles_BL = numpy.load("data/targetAnglesData_BL.npy")
targetAngles_FL = numpy.load("data/targetAnglesData_FL.npy")

#matplotlib.pyplot.plot(backLegSensorValues, linewidth=3, linestyle='dashed', label='Back Leg')
#matplotlib.pyplot.plot(frontLegSensorValues, linewidth=2, label='Front Leg')
matplotlib.pyplot.plot(targetAngles_BL, linewidth=3, label='Target Angles (backleg')
matplotlib.pyplot.plot(targetAngles_FL, linewidth=2, label='Target Angles (frontleg)')

matplotlib.pyplot.legend(loc=0, shadow=True)
matplotlib.pyplot.show()