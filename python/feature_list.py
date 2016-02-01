import numpy as np
import pandas as pd
import math 


'''____________________Root mean square_______________'''
def rms(l):
    return np.sqrt(l.dot(l)*1.0/len(l.values))

def extract_rms_feature(data_frame, start, length, feature_type, sensor, axis):
    data_frame = data_frame.apply(rms, axis=1)[start: start + length].to_frame()
    data_frame.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame

'''____________________Mean-crossing-rate_______________'''
def mean_crossing(l):
    return len(np.where(np.diff(np.sign(l.values - np.mean(l))))[0])*1.0 / len(l.values)

def extract_mean_crossing_rate_feature(data_frame, start, length, feature_type, sensor, axis):
    data_frame = data_frame.apply(mean_crossing, axis=1)[start: start + length].to_frame()
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

'''____________FFT simple features__________________________'''

def fft_mean(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    return np.mean(abs(fft))

def fft_median(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    return np.median(abs(fft))

def fft_max(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    return np.max(abs(fft))

def fft_min(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    return np.min(abs(fft))

def fft_std(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    return np.std(abs(fft))


def extract_simple_fft_feature(data_frame, start, length, feature_type, sensor, axis):
    if feature_type == 'fft-mean':
        data_frame_result = data_frame.apply(fft_mean, axis=1)[start: start + length].to_frame()
    elif feature_type == 'fft-median':
        data_frame_result = data_frame.apply(fft_median, axis=1)[start: start + length].to_frame()
    elif feature_type == 'fft-max':
        data_frame_result = data_frame.apply(fft_max, axis=1)[start: start + length].to_frame()
    elif feature_type == 'fft-min':
        data_frame_result = data_frame.apply(fft_min, axis=1)[start: start + length].to_frame()
    elif feature_type == 'fft-std':
        data_frame_result = data_frame.apply(fft_std, axis=1)[start: start + length].to_frame()

    data_frame_result.columns = [feature_type + '_' + sensor +  '_' + axis ]
    return data_frame_result



'''_____________________FFT Spectral Centroid __________________'''

def fft_spectral_centroid(l):
    fft = np.fft.fft(l)
    fft = fft[0:len(l)/2]
    sum_frequency_times_amplitude = 0
    sum_amplitude = 0
    for x in range(0, len(l)/2):
        sum_frequency_times_amplitude += x * abs(fft[x])
        sum_amplitude += abs(fft[x])
    if sum_amplitude == 0:
        return 25.0
    else:
        return sum_frequency_times_amplitude/sum_amplitude

def extract_fft_spectral_centroid(data_frame,start,length,feature_type,sensor,axis):
    data_frame_result = data_frame.apply(fft_spectral_centroid,axis=1)[start:start + length].to_frame()

    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result

'''_____________________FFT Spectral Entropy __________________'''

def fft_spectral_entropy(l):
    fft = np.fft.fft(l)
    fft = fft[0:len(l)/2]
    psum=0
    H=0

    for i in range(0,len(l)/2):
        a = (1.0/len(l)/2)*abs(fft[i])*abs(fft[i])
        psum = psum + a

    for i in range(0, len(l)/2):
        a = (1.0/len(l)/2)*abs(fft[i])*abs(fft[i])
        Pi = a/psum
        if Pi!=0:
            H = H + Pi*np.log2(Pi) 
    H=-H
    return H

def extract_fft_spectral_entropy(data_frame,start,length,feature_type,sensor,axis):
    data_frame_result = data_frame.apply(fft_spectral_entropy,axis=1)[start:start + length].to_frame()
    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result    

    '''_____________________Extract DC Angle __________________'''


def extract_DC_angle(df_x, df_y, df_z, start, length, feature_type, sensor):
    #
    df_x_mean = df_x.mean(axis=1)
    df_y_mean = df_y.mean(axis=1)
    df_z_mean = df_z.mean(axis=1)

    df_g = df_x_mean.pow(2,axis=0) + df_y_mean.pow(2,axis=0) + df_z_mean.pow(2,axis=0)
    df_g = df_g.apply(np.sqrt)

    df_div =  - df_x_mean.div(df_g,axis=0)
    df_angle = df_div.apply(np.arccos) * 180 / math.pi

    data_frame_result = df_angle[start:start+length].to_frame()
    data_frame_result.columns = [feature_type + '_' + sensor]
    return data_frame_result  

def fft_max_magnitude(l):
    fft = np.fft.fft(l)
    fft = abs(fft[5:len(l)/2])
    return np.argmax(fft)



def extract_fft_max_magnitude(data_frame,start,length,feature_type,sensor,axis):
    data_frame_result = data_frame.apply(fft_max_magnitude,axis=1)[start:start + length].to_frame()

    data_frame_result.columns = [feature_type + '_' + sensor + '_' + axis]
    return data_frame_result    
