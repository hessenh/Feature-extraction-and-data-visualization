import numpy as np
import pandas as pd
from os import path
import os
from os import listdir


# Changing labels from spesific label to generalized label, eg. walking => Dynamic
def label_generalization_main(convertion_list, direct):
	dirname = os.path.dirname
	p = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/DATA_WINDOW/')
	
	from_filename = '/Usability_LAB_All_L.csv'
	to_filename = '/Usability_LAB_All_L_GENERALIZED.csv'
	
	df = pd.read_csv(p + from_filename, header=None, sep='\,')

	for i in range(len(convertion_list)):
		df[0][df[0]==i+1] = convertion_list[i] 
	df.to_csv(p + to_filename,  header=None, index=False)
