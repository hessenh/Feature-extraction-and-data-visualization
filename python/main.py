from raw_signal_to_window import *
from feature_extraction import *
from weka import *
from label_generalization import *


def main(subjects, size_of_window, overlap_between_windows, create_sliding_windows, create_features, create_weka, create_weka_generalized):
	for subject_directory in subjects:
		print "Subject: " + subject_directory
		# Create sliding windows 
		if create_sliding_windows:
			print "Creating windows"
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows)

		# Extract features 
		if create_features:
			print "Extracting features"
			features = ['mean', 'min', 'max', 'median','std', 'energy', 'zero-crossing', 'correlation', 'rms']
			extract_features_main(subject_directory,features)


		# Create weka file
		if create_weka:
			print "Converting to weka-format"
			weka_main(subject_directory,False)

		# Create generalized weka file
		if create_weka_generalized:
			change_list = [1,1,1,1,1,2,2,2,1,2,3,1,1,2]
			label_generalization_main(change_list, subject_directory)
			weka_main(subject_directory,True)

subjects = ["P03"]
size_of_window = 50
overlap_between_windows = 25


main(subjects, size_of_window, overlap_between_windows, False, True, True, True)