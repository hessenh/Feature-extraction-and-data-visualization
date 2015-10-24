from raw_signal_to_window import *
from feature_extraction import *
from weka import *
from label_generalization import *

# Create sliding windows 
subject_directory = "P03"
size_of_window = 100
overlap_between_windows = 50

#raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows)


# Extract features 
features = ['mean', 'min', 'max', 'median','std', 'energy', 'zero-crossing', 'correlation', 'rms']

#extract_features_main(subject_directory,features)



# Create weka file
weka_main(subject_directory,False)

# Create generalized weka file
change_list = [1,1,1,1,1,2,2,2,1,2,3,1,1,2]
label_generalization_main(change_list, subject_directory)
weka_main(subject_directory,True)