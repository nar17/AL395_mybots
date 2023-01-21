import numpy

class SOLUTION:
	def __init__(self):
		self.weights = numpy.random.rand(3,2)
		self.scaledWeight = self.weights * 2 - 1
		print(self.weights)
		print(self.scaledWeight)
		exit()