import pandas as pd


FEATURES_P03 = "/home/hessenh/Development/Prosjektoppgave/Notebook/data/FEATURES_P03.csv"
df_features = pd.read_csv(FEATURES_P03)
 
LABELS_P03 = "/home/hessenh/Development/Prosjektoppgave/Notebook/data/P03_DATA_WINDOW/P03_LABEL_L.csv"
df_labels = pd.read_csv(LABELS_P03)
df_labels.columns = ['label']

df_features = df_features[:len(df_labels)]


df_features = pd.concat([df_features,df_labels],axis=1)

print df_features.tail()


t = 'proc.arff'


finalList = []
finalList.append(['@relation Activity'])
finalList.append([''])

a = []
for i in df_features.columns:
	finalList.append(['@attribute ' + i + " real"])
del finalList[-1]

label_pos = ["@attribute act {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0}"]
finalList.append(label_pos)
finalList.append([''])


finalList.append(['@data'])

print finalList

for i in range(len(df_features)-1):
	new_l = ""
	for i in df_features.iloc[i].values:
		new_l += str(i)
		new_l += ","
	new_l = new_l[:-1]
	finalList.append([new_l])

print len(finalList)

with open(t, 'w') as file:
    file.writelines('\t'.join(i) + '\n' for i in finalList)