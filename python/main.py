from raw_signal_to_window import *
from feature_extraction import *
from weka import *
from label_generalization import *
from remove_activities import *

''' 
Creating sliding window, extract features and creates the weka-files. 

input: Subjects, window size, overlap and boolean values depening one what you want to do, e.g create windows

'''
def main(subjects, size_of_window, overlap_between_windows, remove_activities, create_sliding_windows, create_features, create_weka, create_weka_generalized):
	for subject_directory in subjects:
		print "Subject: " + subject_directory

		# Remove activities such as undefined/static/dynamic
		if remove_activities:
			print "Removing activities"
			activities = [11,13,14]
			remove_activities_main(subject_directory, activities)


		# Create sliding windows 
		if create_sliding_windows:
			print "Creating windows"
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows)

		# Extract features 
		if create_features:
			print "Extracting features"
			features = ['mean', 'min', 'max', 'median','std', 'energy', 'zero-crossing', 'correlation', 'rms','fft-mean', 'fft-median', 'fft-max', 'fft-min', 'fft-std','fft-spectral-centroid']
			#features = ['energy']
			extract_features_main(subject_directory,features)

		# Create weka file
		if create_weka:
			print "Converting to weka-format"
			weka_main(subject_directory,False)

		# Create generalized weka file
		if create_weka_generalized:
			change_list = [1,2,2,2,2,2,2,2,2,2,2,2,2,2]
			label_generalization_main(change_list, subject_directory)
			weka_main(subject_directory,True)


subjects = ["P03"]
size_of_window = 1000
overlap_between_windows = 500


main(subjects, size_of_window, overlap_between_windows,True, True, True, True, True)