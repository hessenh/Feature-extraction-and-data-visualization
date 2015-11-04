from raw_signal_to_window import *
from feature_extraction import *
from weka import *
from label_generalization import *
from remove_activities import *

''' 
Creating sliding window, extract features and creates the weka-files. 

input: Subjects, window size, overlap and boolean values depening one what you want to do, e.g create windows

'''
def main(subjects, size_of_window, overlap_between_windows, remove_activities, create_sliding_windows, create_features, current_window_size, create_weka, create_weka_generalized):
	for subject_directory in subjects:
		print "Subject: " + subject_directory

		# Remove activities such as undefined/static/dynamic
		if remove_activities:
			print "Removing activities"
			activities = [-1,11,13,14,15] 
			remove_activities_main(subject_directory, activities, False)
			remove_activities_main(subject_directory, activities, True)


		# Create sliding windows 
		if create_sliding_windows:
			print "Creating windows"
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows, False)
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows, True)

		# Extract features 
		if create_features:
			print "Extracting features"
			features = ['mean', 'min', 'max', 'median','std', 'energy', 'zero-crossing', 'correlation', 'rms','fft-mean', 'fft-median', 'fft-max', 'fft-min', 'fft-std','fft-spectral-centroid','fft-spectral-entropy','DC-angle']
			#features = ['energy']
			extract_features_main(subject_directory,features, current_window_size)

		# Create weka file
		if create_weka:
			print "Converting to weka-format"
			weka_main(subject_directory,False)

		# Create generalized weka file
		if create_weka_generalized:
			change_list = [1,2,2,2,2,2,2,2,2,2,2,2,2,2]
			label_generalization_main(change_list, subject_directory)
			weka_main(subject_directory,True)


subjects = ["P01"]#["P01","P05","P07","P08","P09","P10","P11","P13","P12","P14","P15","P16","P17","P18","P19","P20","P21"]
size_of_window = 100
overlap_between_windows = 50

# subjects, size_of_window, overlap_between_windows, remove_activities, dc_comp, create_sliding_windows, create_features, create_weka, create_weka_generalized, 
main(subjects, 
	size_of_window, 
	overlap_between_windows,
	False, # Remove activities from signals
	False, # Create sliding windows
	True, # Create features? Remember to delete prev file if you are not appending a feature. 
	1, # What window-size are the feature generated from?
	False, # Create Weka?
	False) # Create generalized weka?


''' Activities: 
:'none'	
1:'walking'	
2:'walking with transition'	
3:'shuffling'	
4:'stairs (ascending)'	
5:'stairs (descending)'	
6:'standing'	
7:'sitting'	
8:'lying'	
9:'transition'	
10:'leaning'	
11:'undefined'	
12:'jumping'	
13:'Dynamic'	
14:'Static'	
15:'Shake'	
16:'picking'	
17:'kneeling'

'''