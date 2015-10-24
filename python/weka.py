import pandas as pd
from os import path
import os
from os import listdir

def weka_main(direct, generalized):

	# Get parent dir
	dirname = os.path.dirname
	FEATURES = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/FEATURES/FEATURES.csv')

	df_features = pd.read_csv(FEATURES)

	if generalized:
		LABELS = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/DATA_WINDOW/Usability_LAB_All_L_GENERALIZED.csv')
	else:
		LABELS = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/DATA_WINDOW/Usability_LAB_All_L.csv')

	df_labels = pd.read_csv(LABELS)
	df_labels.columns = ['label']

	df_features = df_features[:len(df_labels)]


	df_features = pd.concat([df_features,df_labels],axis=1)

	if generalized:
		t = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/WEKA/' + direct + 'GENERALIZED.arff')
	else:
		t = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/WEKA/' + direct + '.arff')


	finalList = []
	finalList.append(['@relation Activity'])
	finalList.append([''])

	a = []
	for i in df_features.columns:
		finalList.append(['@attribute ' + i + " real"])
	del finalList[-1]

	if generalized:
		label_pos = ["@attribute act {1.0,2.0,3.0}"]
	else: 
		label_pos = ["@attribute act {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0}"]

	finalList.append(label_pos)
	finalList.append([''])


	finalList.append(['@data'])


	for i in range(len(df_features)-1):
		new_l = ""
		for i in df_features.iloc[i].values:
			new_l += str(i)
			new_l += ","
		new_l = new_l[:-1]
		finalList.append([new_l])


	with open(t, 'w') as file:
	    file.writelines('\t'.join(i) + '\n' for i in finalList)