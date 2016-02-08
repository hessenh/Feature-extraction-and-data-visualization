import numpy as np
import pandas as pd
import os
from os import path
from os import listdir
from os.path import isfile, join


        


subjects = ["01A"] #,"02A","03A"]#,"04A","05A","07A","08A","09A","10A","11A","12A","13A","14A","15A","16A","18A","19A","21A","22A","23A"]
split = [300000]

for i in range(0,len(subjects)):
	signal_folder = "/RAW_SIGNALS/"
	dirname=os.path.dirname
	p = os.path.join(dirname(dirname(__file__)), 'data/'+subjects[i])
	files_in_dir = [ f for f in listdir(p + signal_folder) if isfile(join(p+ signal_folder,f)) ]
	for f in files_in_dir:

		f = p + signal_folder + f
		print f
		df = pd.read_csv(f, header=None, sep='\,')
		print df

		df_in_lab = df[0:split[i]]
		df_out_lab = df[split[i]+1:len(df)-1]

		print df_in_lab

		print df_out_lab