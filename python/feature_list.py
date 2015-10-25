import numpy as np
import pandas as pd


'''____________________Root mean square_______________'''
def rms(l):
    return np.sqrt(l.dot(l)*1.0/len(l.values))

def extract_rms_feature(data_frame, start, length, feature_type, sensor, axis):
    data_frame = data_frame.apply(rms, axis=1)[start: start + length].to_frame()
    data_frame.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame

'''____________________Zero-crossing-rate_______________'''
def zero_crossing(l):
    return len(np.where(np.diff(np.sign(l.values)))[0])*1.0 / len(l.values)

def extract_zero_crossing_rate_feature(data_frame, start, length, feature_type, sensor, axis):
    data_frame = data_frame.apply(zero_crossing, axis=1)[start: start + length].to_frame()
    data_frame.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame

'''____________________Correlation_______________'''
def extract_correlation_feature(data_frame_one, data_frame_two, start, length, feature_type, sensor, axis):
    data_frame = data_frame_one.corrwith(data_frame_two, axis=1)[start: start + length].to_frame()
    data_frame.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame

'''____________________ENERGY_______________'''    
def extract_energy_feature(df_x, df_y, df_z, start, length, feature_type, sensor):    
    data_frame_result = ((np.sqrt(np.square(df_x.sub(np.mean(df_x,axis=1),axis=0)).sum(axis=1)) + np.sqrt(np.square(df_y.sub(np.mean(df_y,axis=1),axis=0)).sum(axis=1)) + np.sqrt(np.square(df_z.sub(np.mean(df_z,axis=1),axis=0)).sum(axis=1)))/3.0)/len(df_x.iloc[0].values)
    data_frame_result = pd.DataFrame(np.array(data_frame_result))
    data_frame_result.columns = [feature_type + '_' + sensor]
    return data_frame_result



'''_____________Simple features__________________'''

def extract_simple_feature(data_frame, start, length, feature_type, sensor, axis):

    if feature_type == 'mean':
        data_frame_result = data_frame.mean(axis=1)[start: start + length].to_frame()
    elif feature_type == 'median':
        data_frame_result = data_frame.median(axis=1)[start: start + length].to_frame()
    elif feature_type == 'max':
        data_frame_result = data_frame.max(axis=1)[start: start + length].to_frame()
    elif feature_type == 'min':
        data_frame_result = data_frame.min(axis=1)[start: start + length].to_frame()
    elif feature_type == 'std':
        data_frame_result = data_frame.std(axis=1)[start: start + length].to_frame()

    data_frame_result.columns = [feature_type + '_' + sensor +  '_' + axis ]
    return data_frame_result