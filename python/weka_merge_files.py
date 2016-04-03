import pandas as pd
from os import path
import os
from os import listdir
SUBJECTS = ["P01","P03","P04","P05","P06","P07","P08","P09","P10","P11","P12","P13","P14","P15","P16","P17","P18","P19","P20","P21"]
SUBJECTS = ["01Y","02Y","03Y","04Y","05Y","06Y","07Y","08Y","09Y","11Y","12Y","13Y"]


SUBJECTS = ["01A","02A","03A","04A","05A","06A","07A","08A","09A","10A","11A","12A","13A","14A","15A","16A","18A","19A","20A","21A","22A","23A"]
#SUBJECTS = ["P03","P04","P06","P07","P08","P09","P10","P11","P14","P15","P16","P17","P18","P19","P20","P21"]#["P03","P06","P08","P10","P14","P16","P18","P20"]#
#SUBJECTS = ["PM01","PM02","PM03","PM04","PM05","PM06","PM07","PM08","PM09","PM11","PM12","PM13","PM14","PM15","PM16"]
data_set = "A"


START_SUB = SUBJECTS[0]
WINDOW_SIZE = "1.0"
RESULT_PATH = '../data/'+data_set+str(WINDOW_SIZE)+ '.arff'



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