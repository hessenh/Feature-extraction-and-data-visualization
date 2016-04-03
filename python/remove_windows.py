import numpy as np
import pandas as pd
from Sliding import *
from os import path
import os
from os import listdir
from os.path import isfile, join
from collections import Counter

def main(direct, size, threshold):
   # Get the label and feature paths
   paths = get_file_paths(direct, size)


   # Load label and feature data frame
   df_label = load_file_to_dataframe(paths[0], None)
   df_features = load_file_to_dataframe(paths[1], True)
   #print len(df_label),len(df_features)

   # A boolean data frame where number of labels are bellow threshold
   df_label_boolean = get_boolean_dataframe(df_label, threshold, size)

   # Remove windows bellow threshold
   df_removed_windows_label = remove_windows(df_label, df_label_boolean)
   df_removed_windows_features = remove_windows(df_features, df_label_boolean)
   #print len(df_removed_windows_features), len(df_removed_windows_label)

   # Now the labels are in this format : [1,1,1,1,1,1,1,1,1]
   # Will change it to [1]
   df_label = df_label.apply(most_common_label, axis=1)
   df_removed_windows_label = df_removed_windows_label.apply(most_common_label, axis = 1)


   # Save old labels, new labels, new features
   save_data_frame(df_label, paths[0], False)
   save_data_frame(df_removed_windows_label, paths[2], False)
   save_data_frame(df_removed_windows_features, paths[3], True)



def save_data_frame(df, path, header_boolean):
    if header_boolean:
        df.to_csv(path, index=False)
    else:
        df.to_csv(path, header=None, index = False)
def boolean_dataframe(l, threshold, size):

    word_counts = Counter(l.values)
   
    most_common_label = word_counts.most_common(1)
    if most_common_label[0][1]*1.0 / (size*100) > threshold:
        return True
    return False
    #return most_common_label[0][0]

def most_common_label(l):
    word_counts = Counter(l.values)
    most_common_label = word_counts.most_common(1)
    return most_common_label[0][0]


def get_boolean_dataframe(df, threshold, size):
    return df.apply(boolean_dataframe,args=(threshold, size) ,axis=1)

def remove_windows(df, boolean_dataframe):
    
    return df[boolean_dataframe==True]
    


def load_file_to_dataframe(path, header_boolean):
    if header_boolean:
        return pd.read_csv(path, sep='\,', engine="python")
    else:
        return pd.read_csv(path, header=None, sep='\,', engine="python")


def get_file_paths(direct, size):

    feature_path = "/FEATURES/"+str(size) + "/FEATURES.csv"
    label_path = "/DATA_WINDOW/"+str(size) + "/ORIGINAL/"

    signal_folder = "/DATA_WINDOW/"
    # Get parent dir
    dirname=os.path.dirname
    sub_folder = os.path.join(dirname(dirname(__file__)), 'data/' + direct)

    files_in_dir = [ f for f in listdir(sub_folder+label_path) if isfile(join(sub_folder + label_path,f)) ]
    for file in files_in_dir:
        if "LAB" in file:
            label_path = sub_folder + label_path + file

    feature_path = sub_folder + feature_path
    feature_path_removed_messy_windows = feature_path[:-4] + "_REMOVED_MESSY_WINDOWS.csv"
    label_path_removed_messy_windows = label_path[:-4] + "_REMOVED_MESSY_WINDOWS.csv"

    return [label_path, feature_path, label_path_removed_messy_windows, feature_path_removed_messy_windows]



if __name__ == "__main__":
    main("01A",1.0, 0.7)