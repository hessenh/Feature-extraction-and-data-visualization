import pandas as pd
from os import path
import os
from os import listdir

WINDOW_SIZE = "1.0"
RESULT_PATH = '../data/'+str(WINDOW_SIZE)+ '.arff'


with open(RESULT_PATH) as f:
	result = f.readlines()



label_number = len(result[1000].split(','))
#print label_number, result[1000][label_number]
#print result[1000].split(',')[label_number-1]
DATA_INDEX = result.index("@data\n")

j= 0
for i in range(DATA_INDEX+1,len(result)):
	l = result[i].split(',')[label_number-1]
	if l == '16.0\n':
		j +=1
	elif l != '16.0\n' and j>0:
		print j
		j=0