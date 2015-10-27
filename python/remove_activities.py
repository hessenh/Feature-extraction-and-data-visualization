import numpy as np
import pandas as pd
from os import path
import os
from os import listdir
from os.path import isfile, join




def remove_activities_main(subject_directory, activities):
	# Get parent dir
	dirname=os.path.dirname
	p = os.path.join(dirname(dirname(__file__)), 'data/'+subject_directory)
	# Files in current directory
	files_in_dir = [ f for f in listdir(p + "/RAW_SIGNALS/") if isfile(join(p+ "/RAW_SIGNALS/",f))]
	dic = {}
	for i in files_in_dir:
		dic[i.split('_')[2]] = i
	# figure out which is the label data_frame
	one = files_in_dir[0].split('_')
	two = files_in_dir[1].split('_')
	three = files_in_dir[2].split('_')

	df_chest = pd.read_csv(p + '/RAW_SIGNALS/' + dic['CHEST'], header=None, sep='\,')
	df_thigh = pd.read_csv(p + '/RAW_SIGNALS/' + dic['THIGH'], header=None, sep='\,')
	df_label = pd.read_csv(p + '/RAW_SIGNALS/' + dic['LAB'], header=None, sep='\,')



	# Trimming the data to the shortes data frame. 
	size = min(len(df_chest),len(df_thigh),len(df_label)) 
	df_chest = df_chest[0:size]
	df_thigh = df_thigh[0:size]
	df_label = df_label[0:size]

	for activity in activities:
		df_chest = df_chest[df_label[0] != activity]
		df_thigh = df_thigh[df_label[0] != activity]
		df_label = df_label[df_label[0] != activity]


	df_chest.to_csv(p + '/RAW_SIGNALS/'+dic['CHEST'],  header=None, index=False)
	df_thigh.to_csv(p + '/RAW_SIGNALS/'+dic['THIGH'],  header=None, index=False)
	df_label.to_csv(p + '/RAW_SIGNALS/'+dic['LAB'],  header=None, index=False)


