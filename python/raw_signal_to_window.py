import numpy as np
import pandas as pd
from Sliding import *
from os import path
import os
from os import listdir
from os.path import isfile, join
from collections import Counter
import shutil

'''
Using the Sliding file to create a the windows
'''
def find_most_common_label(l):

    word_counts = Counter(l.values)
    most_common_label = word_counts.most_common(1)
    return most_common_label[0][0]
  

def extract_axis(df, size, overlap):
    df = df.values.tolist();
    df = np.array(df)
    df_windows = sliding_window(df, size, overlap)

    df_windows = pd.DataFrame(df_windows)
    return df_windows
    
    
def create_sliding_window(path, filename, seperator, size, overlap, signal_folder, dc_component, len_of_start_name):

    axis = ["X", "Y", "Z"]
    
    pd.set_option('html',False)

    f = path + signal_folder + filename
    print f


    df = pd.read_csv(f, header=None, sep=seperator)

    num_of_axis = len(df.iloc[0].values)

    for i in range(num_of_axis):
       
        # Acc - xyz
        if num_of_axis > 1:
            df_windows = extract_axis(df[i], size, overlap)
            file_name_axis = filename[len_of_start_name:len(filename)-4] + "_"+ axis[i] + ".csv"
            
        # Label
        else: 
            df_windows = extract_axis(df[i], size, overlap)
            #print df_windows
            # label the window with the maximum number of labels in that window
            
            #df_windows = df_windows.apply(find_most_common_label,axis=1)


            

            file_name_axis = filename[len_of_start_name:len(filename)-4] + "_L.csv"
        
        
        if dc_component:
            folder_name = "DC"
        else: 
            folder_name = "ORIGINAL"

        # Check if folder exist, create
        new_folder = path + '/DATA_WINDOW/' + str(size*1.0 / 100) + '/' + folder_name

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)


        df_windows.to_csv(new_folder + '/'+file_name_axis,  header=None, index=False)



def raw_signal_to_window_main(direct, size, overlap, dc_component, len_of_start_name):
    if dc_component:
        signal_folder = "/RAW_SIGNALS_DC/"
    else:
        signal_folder = "/RAW_SIGNALS/"


    # Get parent dir
    dirname=os.path.dirname
    p = os.path.join(dirname(dirname(__file__)), 'data/'+direct)

    print p
    # Remove folder and content - window
    if dc_component:
        shutil.rmtree(p +'/DATA_WINDOW/' + str(size*1.0 / 100) + "/DC")
    else:
        shutil.rmtree(p +'/DATA_WINDOW/' + str(size*1.0 / 100) + "/ORIGINAL")




    # Files in current directory
    files_in_dir = [ f for f in listdir(p + signal_folder) if isfile(join(p+ signal_folder,f)) ]

    for f in files_in_dir:
        create_sliding_window(p, f, '\,', size, overlap, signal_folder, dc_component, len_of_start_name)
