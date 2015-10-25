import numpy as np
import pandas as pd


'''____________________Root mean square_______________'''
def extract_rms_feature(data_frame, start, length, feature_type, sensor, axis):
    result = []

    for i in range(start, start+ length):
        result.append(np.sqrt(data_frame.iloc[i].dot(data_frame.iloc[i])*1.0/len(data_frame.iloc[i].values)))

    data_frame_result = pd.DataFrame(np.array(result))
    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result




'''____________________Zero-crossing-rate_______________'''
def extract_zero_crossing_rate_feature(data_frame, start, length, feature_type, sensor, axis):
    result = []
    
    for i in range(start, start + length):
        result.append(len(np.where(np.diff(np.sign(data_frame.iloc[i])))[0])*1.0 / len(data_frame.iloc[i].values))

    data_frame_result = pd.DataFrame(np.array(result))
    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result





'''____________________Correlation_______________'''
def extract_correlation_feature(data_frame_one, data_frame_two, start, length, feature_type, sensor, axis):
    result = []
    
    for i in range(start, start + length):
        result.append(data_frame_one.iloc[i].corr(data_frame_two.iloc[i]))

    data_frame_result = pd.DataFrame(np.array(result))
    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result





'''____________________ENERGY_______________'''
def sum_of_square(axis):
    l = []
    for i in axis:
        l.append(float(i))
    mean = sum(l)*1.0/len(l)
    s = 0
    for i in l:
        s += (i-mean)**2
    return s**0.5
    
def extract_energy_feature(df_x, df_y, df_z, start, length, feature_type, sensor):
    result = []
    for i in range(start, start + length):
        energy = sum_of_square(df_x.iloc[i]) + sum_of_square(df_y.iloc[i]) + sum_of_square(df_z.iloc[i])
        energy = energy*1.0 / 3
        energy = energy / len(df_x.iloc[start].values)
        result.append(energy)

    data_frame_result = pd.DataFrame(np.array(result))
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