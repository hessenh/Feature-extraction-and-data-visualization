from numpy import genfromtxt
import numpy

data = genfromtxt('P03_LABEL.csv', delimiter=',')



print data


n_data = []

for i in data:
	n_data.extend([i]*4)

a = numpy.asarray(n_data)

numpy.savetxt("P03_LABEL2.csv", a, delimiter=",")