import numpy as np
import pandas as pd
pd.set_option('html',False)

from os import path
from os import listdir
from os.path import isfile, join
import os

'''
http://pandas.pydata.org/pandas-docs/stable/api.html#id5
Information about mean, median... 
'''


#Zero crossing
def zero_crossing_rate(l,size):
    return len(np.where(np.diff(np.sign(l)))[0])*1.0 / size


#Correlation
def correlation(data_frame_one, data_frame_two):
    return data_frame_one.corr(data_frame_two)

def extractCorrelation(data_frame_one, data_frame_two, start, size):
    res = []
    
    for i in range(start, start + size):
        res.append(correlation(data_frame_one.iloc[i], data_frame_two.iloc[i]))
        
    return pd.DataFrame(np.array(res))


#Energy
def sumOfSqr(axis):
    l = []
    for i in axis:
        l.append(float(i))
    mean = sum(l)/len(l)
    s = 0
    for i in l:
        s += (i-mean)**2
    return s**0.5
    
def extractEnergy(x ,y ,z ,n_sample ,start, size):
    res = []
    for i in range(start, start + size):
        e = sumOfSqr(x.iloc[i]) + sumOfSqr(y.iloc[i]) + sumOfSqr(z.iloc[i])
        e = e/ 3
        e = e / n_sample
        res.append(e)
        
    return pd.DataFrame(np.array(res))



def extract(method, data_frame, start, size):
    res = []
    for i in range(start, start + size):
        
        if method == 'mean':
            res.append(data_frame.iloc[i].mean())
        elif method == 'median':
            res.append(data_frame.iloc[i].median())
        elif method == 'max':
            res.append(data_frame.iloc[i].max())
        elif method == 'min':
            res.append(data_frame.iloc[i].min())
        elif method == 'std':
            res.append(data_frame.iloc[i].std())
        elif method == 'zero-crossing':
            res.append(zero_crossing_rate(data_frame.iloc[i],size))
        elif method == 'rms':
            res.append(np.sqrt(data_frame.iloc[i].dot(data_frame.iloc[i])*1.0/size))
        
    return pd.DataFrame(np.array(res))




def add_feature(feature_type,df_x,df_y,df_z,path,sensor,size):
    start=0
   
    

    # If file exists
    try:
        df_features = pd.read_csv(path, sep='\,')
        
        l = []
        # Get all the featues already computed
        for i in df_features.columns.values:
            n = i.split("_")
            n = n[0] + '_' + n[1]
            l.append(n)
        
        # Create the string format of the feature: feature and sensor
        t = feature_type + "_" + sensor

        
        if t not in l:
            print "Adding feature: ", t
            # This is for all axis
            if feature_type == "energy":
                df_sensor_feature = extractEnergy(df_x,df_y,df_z,len(df_x.iloc[0].values), start, size)
                df_sensor_feature.columns = [feature_type + '_' + sensor ]
                
                df_features= pd.concat([df_features, df_sensor_feature],axis=1)
                
            elif feature_type == "correlation":
                df_correlation_xy = extractCorrelation(df_x, df_y, start, size)
                df_correlation_xy.columns = [feature_type + '_' + sensor + "_xy"]
                
                df_correlation_xz = extractCorrelation(df_x, df_z, start, size)
                df_correlation_xz.columns = [feature_type + '_' + sensor + "_xz"]
                
                df_correlation_yz = extractCorrelation(df_y, df_z, start, size)
                df_correlation_yz.columns = [feature_type + '_' + sensor + "_yz"]
                
                df_features= pd.concat([df_features, df_correlation_xy,df_correlation_xz, df_correlation_yz],axis=1)
            # Only for one axis
            else:
                df_x_feature = extract(feature_type,df_x,start,size)
                df_x_feature.columns = [feature_type + '_' + sensor +  '_x' ]
                df_y_feature = extract(feature_type,df_y,start,size)
                df_y_feature.columns = [feature_type + '_' + sensor +  '_y']
                df_z_feature= extract(feature_type,df_z,start,size)
                df_z_feature.columns = [feature_type + '_' + sensor +  '_z' ]
                
                df_features= pd.concat([df_features, df_x_feature,df_y_feature, df_z_feature],axis=1)
            
        else:
            print t, " is already computed"
           
        
        #If file does not exist
    except IOError:
        print 'make feature file'
        if feature_type == "energy":
            df_sensor_feature = extractEnergy(df_x,df_y,df_z,len(df_x.iloc[0].values), start, size)
            df_sensor_feature.columns = [feature_type + '_' + sensor ]

            df_features= df_sensor_feature
            
        elif feature_type == "correlation":
                df_correlation_xy = extractCorrelation(df_x, df_y, start, size)
                df_correlation_xy.columns = [feature_type + '_' + sensor + "_xy"]
                
                df_correlation_xz = extractCorrelation(df_x, df_z, start, size)
                df_correlation_xz.columns = [feature_type + '_' + sensor + "_xz"]
                
                df_correlation_yz = extractCorrelation(df_y, df_z, start, size)
                df_correlation_yz.columns = [feature_type + '_' + sensor + "_yz"]
                
                df_features= pd.concat([df_correlation_xy,df_correlation_xz, df_correlation_yz],axis=1)
        else:
            df_x_feature = extract(feature_type,df_x,start,size)
            df_x_feature.columns = [feature_type + '_' + sensor +  '_x' ]
            df_y_feature = extract(feature_type,df_y,start,size)
            df_y_feature.columns = [feature_type + '_' + sensor +  '_y']
            df_z_feature= extract(feature_type,df_z,start,size)
            df_z_feature.columns = [feature_type + '_' + sensor +  '_z' ]
            
            df_features= pd.concat([df_x_feature,df_y_feature, df_z_feature],axis=1)



    
    df_features.to_csv(path, index=False)





def extract_features_main(direct,features) :

	# name of parent directory
	dirname=os.path.dirname
	p = os.path.join(dirname(dirname(__file__)), 'data/'+direct)
	print p

	# Load DATA WINDOWS
	df_chest_x = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_X.csv', header=None, sep='\,')
	df_chest_y = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_Y.csv', header=None, sep='\,')
	df_chest_z = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_Z.csv', header=None, sep='\,')

	df_thigh_x = pd.read_csv(p + '/DATA_WINDOW/Axivity_THIGH_Left_X.csv', header=None, sep='\,')
	df_thigh_y = pd.read_csv(p + '/DATA_WINDOW/Axivity_THIGH_Left_Y.csv', header=None, sep='\,')
	df_thigh_z = pd.read_csv(p + '/DATA_WINDOW/Axivity_THIGH_Left_Z.csv', header=None, sep='\,')

	# name of path to FEATURES
	p = path.relpath(p + '/FEATURES/FEATURES.csv')
	
	size=min(len(df_chest_x), len(df_thigh_x))-1 

	# Add features
	for f in features:
	    add_feature(f, df_thigh_x, df_thigh_y, df_thigh_z, p, 'thigh',size)
	    add_feature(f, df_chest_x, df_chest_y, df_chest_z, p, 'chest',size) 



