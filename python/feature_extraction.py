import os
from os import path
from os import listdir
from os.path import isfile, join

from feature_list import *


def getFeature(df_x, df_y, df_z, df_x_DC, df_y_DC, df_z_DC, feature_type, sensor, start, length):

    # Simple pandas methods
    if feature_type in ['mean', 'min', 'max', 'median','std']:
        df_x_feature =  extract_simple_feature(df_x, start, length, feature_type, sensor, 'x');
        df_y_feature =  extract_simple_feature(df_y, start, length, feature_type, sensor, 'y');
        df_z_feature =  extract_simple_feature(df_z, start, length, feature_type, sensor, 'z');
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)
    
    elif feature_type == 'energy':
        return extract_energy_feature(df_x, df_y, df_z, start, length, feature_type, sensor)
    
    elif feature_type == 'correlation':
        df_xy_feature = extract_correlation_feature(df_x, df_y, start, length, feature_type, sensor, 'xy')
        df_xz_feature = extract_correlation_feature(df_x, df_z, start, length, feature_type, sensor, 'xz')
        df_yz_feature = extract_correlation_feature(df_y, df_z, start, length, feature_type, sensor, 'yz')
        return pd.concat([df_xy_feature, df_xz_feature, df_yz_feature],axis=1)
        
    elif feature_type == 'mean-crossing':
        df_x_feature = extract_mean_crossing_rate_feature(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_mean_crossing_rate_feature(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_mean_crossing_rate_feature(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)

    elif feature_type == 'rms':
        df_x_feature = extract_rms_feature(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_rms_feature(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_rms_feature(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)


    elif feature_type in ['fft-mean', 'fft-median', 'fft-max', 'fft-min', 'fft-std' ]:
        df_x_feature = extract_simple_fft_feature(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_simple_fft_feature(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_simple_fft_feature(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)

    elif feature_type == 'fft-spectral-centroid':
        df_x_feature = extract_fft_spectral_centroid(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_fft_spectral_centroid(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_fft_spectral_centroid(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)

    elif feature_type == 'fft-spectral-entropy':
        df_x_feature = extract_fft_spectral_entropy(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_fft_spectral_entropy(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_fft_spectral_entropy(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)

    elif feature_type == 'DC-angle':
        return extract_DC_angle(df_x_DC, df_y_DC, df_z_DC, start, length, feature_type, sensor)
    
    elif feature_type == 'fft-max-magnitude':
        df_x_feature = extract_fft_max_magnitude(df_x, start, length, feature_type, sensor, 'x')
        df_y_feature = extract_fft_max_magnitude(df_y, start, length, feature_type, sensor, 'y')
        df_z_feature = extract_fft_max_magnitude(df_z, start, length, feature_type, sensor, 'z')
        return pd.concat([df_x_feature, df_y_feature, df_z_feature],axis=1)
        
def add_feature(features,df_x,df_y,df_z,df_x_DC,df_y_DC,df_z_DC,feature_path,sensor,start,length):
    existing_features = []

    # if file exists
    try:
        df_features = pd.read_csv(feature_path, sep='\,')
        print("File does exist")
        exist = True

        
        # Get all the featues already computed
        for i in df_features.columns.values:
            n = i.split("_")
            n = n[0] + '_' + n[1]
            existing_features.append(n)

    except IOError:
        print("Files does not exist")
        exist = False


    for feature_type in features:
        check_feature_type = feature_type + "_" + sensor

        if check_feature_type not in existing_features:
            df_new_features = getFeature(df_x, df_y, df_z, df_x_DC,df_y_DC,df_z_DC, feature_type, sensor, start, length)
            print "Feature does NOT exist: " + feature_type
            # Add feature type to check list
            existing_features.append(check_feature_type)


            if exist:
                df_features = pd.concat([df_features, df_new_features],axis=1)
            else:
                df_features = df_new_features
                exist = True
        else: 
            print "Feature does exist: " + feature_type

    df_features.to_csv(feature_path, index=False)

def load_sensor_data(path, sensor):
    # Load DATA WINDOWS
    df_x = pd.read_csv(path + sensor + 'X.csv', header=None, sep='\,')
    df_y = pd.read_csv(path + sensor + 'Y.csv', header=None, sep='\,')
    df_z = pd.read_csv(path + sensor + 'Z.csv', header=None, sep='\,')
    return df_x,df_y,df_z



def extract_features_main(direct,features,window_size) :

    # name of parent directory
    dirname=os.path.dirname
    p = os.path.join(dirname(dirname(__file__)), 'data/'+direct)

    # Load data windows
    df_chest_x,df_chest_y,df_chest_z = load_sensor_data(p,'/DATA_WINDOW/'+str(window_size)+'/ORIGINAL/Axivity_CHEST_Back_')
    df_thigh_x,df_thigh_y,df_thigh_z = load_sensor_data(p,'/DATA_WINDOW/'+str(window_size)+'/ORIGINAL/Axivity_THIGH_Left_')

    df_chest_x_DC,df_chest_y_DC,df_chest_z_DC = load_sensor_data(p,'/DATA_WINDOW/'+str(window_size)+'/DC/Axivity_CHEST_Back_DC_')
    df_thigh_x_DC,df_thigh_y_DC,df_thigh_z_DC = load_sensor_data(p,'/DATA_WINDOW/'+str(window_size)+'/DC/Axivity_THIGH_Left_DC_')

    # name of path to FEATURES
    feature_path = path.relpath(p + '/FEATURES/'+str(window_size)+'/FEATURES.csv')

    # Size of smallest sensor data
    start = 0
    length = min(len(df_chest_x), len(df_thigh_x))-1 

    #Create feature folder for window size if it doesnt exist
    new_folder = p + '/FEATURES/' + str(window_size) 
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)


    # Add features
    add_feature(features, df_thigh_x, df_thigh_y, df_thigh_z, df_thigh_x_DC, df_thigh_y_DC, df_thigh_z_DC, feature_path, 'thigh', start, length)
    add_feature(features, df_chest_x, df_chest_y, df_chest_z, df_chest_x_DC, df_chest_y_DC, df_chest_z_DC, feature_path, 'chest', start ,length) 



def remove_feature_files(direct, window_size):
    dirname=os.path.dirname
    p = os.path.join(dirname(dirname(__file__)), 'data/'+direct)
    feature_path = path.relpath(p + '/FEATURES/'+str(window_size)+'/FEATURES.csv')
    os.remove(feature_path);