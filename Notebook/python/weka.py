import pandas as pd
from os import path
import os
from os import listdir

def weka_main(direct, generalized,window_size, without_activity):




	# Get parent dir
	dirname = os.path.dirname
	FEATURES = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/FEATURES/'+str(window_size)+'/FEATURES.csv')

	#Create feature folder for window size if it doesnt exist
	new_folder =  os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/WEKA/'+str(window_size))
	if not os.path.exists(new_folder):
		os.makedirs(new_folder)


	df_features = pd.read_csv(FEATURES)

	if generalized:
		LABELS = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/DATA_WINDOW/'+str(window_size)+'/ORIGINAL/GoPro_LAB_All_L_GENERALIZED.csv')
	else:
		LABELS = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/DATA_WINDOW/'+str(window_size)+'/ORIGINAL/GoPro_LAB_All_L.csv')

	print LABELS
	df_labels = pd.read_csv(LABELS)
	df_labels.columns = ['label']

	df_features = df_features[:len(df_labels)]


	df_features = pd.concat([df_features,df_labels],axis=1)

	activities = []
	#activities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
	if without_activity:
		print "he"
		for activity in activities:
			df_features = df_features[df_labels['label'] != activity]

	if generalized:
		t = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/WEKA/' + str(window_size) +'/'+ direct + 'GENERALIZED.arff')
	else:
		t = os.path.join(dirname(dirname(__file__)), 'data/'+direct + '/WEKA/' + str(window_size) +'/' + direct + '.arff')


	finalList = []
	finalList.append(['@relation Activity'])
	finalList.append([''])

	a = []
	for i in df_features.columns:
		finalList.append(['@attribute ' + i + " real"])
	del finalList[-1]

	if generalized:
		label_pos = ["@attribute act {1.0,2.0}"]
	else: 
		label_pos = ["@attribute act {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0}"]#["@attribute act {1.0,6.0,7.0,8.0,9.0}"] #
		#label_pos = ["@attribute act {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0}"]
		label_string = "@attribute act {"
		for i in range(1,18):
			if i not in activities:
				label_string = label_string + str(i) + ".0,"
		label_pos = [label_string[:len(label_string)-1] + "}"]


	# ["@attribute act {1.0,3.0,6.0,7.0,8.0,9.0,10.0,12.0}"]
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