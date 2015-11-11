import pandas as pd
from os import path
import os
from os import listdir

SUBJECTS = ["P03","P04","P05","P06","P07","P08","P09","P10","P11","P14","P15","P16","P17","P18","P19","P20","P21"]

START_SUB = SUBJECTS[0]
WINDOW_SIZE = "1.0"
RESULT_PATH = '../data/'+str(WINDOW_SIZE)+ '.arff'



# Create first file
Start_weka = '../data/'+START_SUB + '/WEKA/'+str(WINDOW_SIZE)+'/' + START_SUB + '.arff'

with open(Start_weka) as f:
    result = f.readlines()


with open(RESULT_PATH, 'w') as file:
	file.writelines(result)

DATA_INDEX = result.index("@data\n")

for i in range(1,len(SUBJECTS)):
	PATH = '../data/'+ SUBJECTS[i] + '/WEKA/'+str(WINDOW_SIZE)+'/' + SUBJECTS[i] + '.arff'
	with open(PATH) as f:
		result = f.readlines()


	with open(RESULT_PATH, 'a') as file:
		file.writelines(result[DATA_INDEX+1:])