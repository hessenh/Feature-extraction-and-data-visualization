import numpy as np
import pandas as pd
from Sliding import *
from os import path
import os
from os import listdir
from os.path import isfile, join



    
    
def main(subject_directory):
   path = get_path(subject_directory)
   print path
   label_matrix = load_file_as_matrix(path)

   # What label occurs before 
   before_label = 18 #Bending down
   
   criteria_label = 11 #Picking
   after_label = 10 #Bending up

   df_label = relabel_matrix(label_matrix, before_label, criteria_label, after_label)
   df_label.to_csv(path,  header=None, index=False)

def relabel_matrix(matrix, before_label, criteria_label, after_label):
  change_boolean = False
  for i in range(1, len(matrix)):
    # if the previous was the shifting activity and this is the activity to be changed
    if matrix[i-1] == criteria_label and matrix[i] == before_label:
      change_boolean = True
      #print i, change_boolean
    # If the previous activity have been changed and this is not an activity to be changed
    if matrix[i-1] == after_label and matrix[i] != before_label:
      change_boolean = False
      #print i, change_boolean

    # Change the label
    if change_boolean:
      matrix[i] = [after_label]
  return pd.DataFrame(matrix)


def load_file_as_matrix(path):
    return pd.read_csv(path, header=None, sep='\,').as_matrix()

    

def get_path(subject_directory):
    signal_folder = "/RAW_SIGNALS/"
    # Get parent dir
    dirname=os.path.dirname
    p = os.path.join(dirname(dirname(__file__)), 'data/'+subject_directory)

    # Files in current directory
    files_in_dir = [ f for f in listdir(p + signal_folder) if isfile(join(p+ signal_folder,f)) ]

    for f in files_in_dir:
        if "LAB" in f:
            file = f

    path = p + signal_folder + file
    return path

if __name__ == "__main__":
    main("01A")