import math
from scipy.stats.stats import pearsonr 

x = [2,3,2,1,2,5,3]
y = [1,2,4,1,2,4,2]

def mean(values):
	return sum(values) / float(len(values))

def SD(values): 
	# Mean value
	_x = mean(values)
	# Length of list
	N = float(len(values));
	s = 0.0
	# Sum og squared values
	for x in values: 
		s += math.pow((x - _x),2)

	return s / N



def coorelation(x,y):
	return pearsonr(x,y)

def meanCrossing(x,y):
	

print meanCrossing(x,y)