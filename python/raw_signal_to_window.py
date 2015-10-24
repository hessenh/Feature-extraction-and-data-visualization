import numpy as np
import pandas as pd
from Sliding import *
from os import path
import os
from os import listdir
from os.path import isfile, join

'''
Using the Sliding file to create a the windows
'''
def extract_axis(df, size, overlap):
    df = df.values.tolist();
    df = np.array(df)
    df_windows = sliding_window(df, size, overlap)

    df_windows = pd.DataFrame(df_windows)
    return df_windows
    
    
    
'''
Creates a dataframe with every Nth value. This is done to match the windows. 
This may be a naive approach, because we could lose information.. 
??? If less than 80% have the same lable, lable the window as transition ??? 
Original: [1,2,3,4,5,6,7]
New: [1,3,5,7]
'''
def extract_label(df, size, overlap):
    df = df.values.tolist();
    df = np.array(df)
    step = size/2
    df_windows = df[step::step]
    df_windows = pd.DataFrame(df_windows)
    return df_windows
    
    
    
def create_sliding_window(path, filename, seperator, size, overlap):
    
    axis = ["X", "Y", "Z"]
    
    pd.set_option('html',False)

    f = path + "/RAW_SIGNALS/" + filename
    
    df = pd.read_csv(f, header=None, sep=seperator)

    num_of_axis = len(df.iloc[0].values)

    for i in range(num_of_axis):
       
        # Acc - xyz
        if num_of_axis > 1:
            df_windows = extract_axis(df[i], size, overlap)
            file_name_axis = filename[4:len(filename)-4] + "_"+ axis[i] + ".csv"
            
        # Label
        else: 
            df_windows = extract_label(df[i], size, overlap)

            file_name_axis = filename[4:len(filename)-4] + "_L.csv"
        
    
        df_windows.to_csv(path + '/DATA_WINDOW/'+file_name_axis,  header=None, index=False)



def raw_signal_to_window_main(direct, size, overlap):
    # Get parent dir
    dirname=os.path.dirname
    p = os.path.join(dirname(dirname(__file__)), 'data/'+direct)

    # Files in current directory
    files_in_dir = [ f for f in listdir(p + "/RAW_SIGNALS/") if isfile(join(p+ "/RAW_SIGNALS/",f)) ]
    print p

    for f in files_in_dir:
        create_sliding_window(p, f, '\,', size, overlap)
