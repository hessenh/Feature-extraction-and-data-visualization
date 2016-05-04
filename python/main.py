from raw_signal_to_window import *
from feature_extraction import *
from weka import *
from label_generalization import *
from remove_activities import *
import split_activities
import remove_windows
''' 
Creating sliding window, extract features and creates the weka-files. 

input: Subjects, window size, overlap and boolean values depening one what you want to do, e.g create windows

'''
def main(subjects,split, size_of_window, overlap_between_windows, remove_activities, create_sliding_windows,remove_features, create_features, current_window_size, create_weka, create_weka_generalized, create_weka_without_activity, relabel_activities_boolean):
	i=0;
	for subject_directory in subjects:
		print "Subject: " + subject_directory

		# Remove activities such as undefined/static/dynamic
		if remove_activities:
			print "Removing activities"
			activities = [0,12,15]
			remove_activities_main(subject_directory, activities, False)
			remove_activities_main(subject_directory, activities, True)

		# Relabel activties
		if relabel_activities_boolean:
			print "Relabelling activities"
			split_activities.main(subject_directory)

		# Create sliding windows 
		if create_sliding_windows:
			print "Creating windows"
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows, False, 4)
			raw_signal_to_window_main(subject_directory, size_of_window, overlap_between_windows, True, 4)

		# Remove feature file
		if remove_features: 
			remove_feature_files(subject_directory, current_window_size)

		# Extract features 
		if create_features:
			print "Extracting features"# 

			features = ['mean']#True, 'min', 'max', 'median','std', 'energy','correlation','mean-crossing', 'rms','fft-mean', 'fft-median', 'fft-max', 'fft-std','fft-spectral-centroid','fft-spectral-entropy','DC-angle','fft-max-magnitude']
			#features = ['DC-angle']
		
			extract_features_main(subject_directory,features, current_window_size)

		# Remove messy windows
		print "Removing messy windows"
		remove_windows.main(subject_directory, current_window_size, 0.8)


		# Create weka file
		if create_weka:
			print "Converting to weka-format"
			weka_main(subject_directory,False,current_window_size, create_weka_without_activity,0,False)#split[i]
			

		# Create generalized weka file
		if create_weka_generalized:
			change_list = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
			label_generalization_main(change_list, subject_directory, current_window_size)
			weka_main(subject_directory,True,current_window_size, create_weka_without_activity)

		i+=1


subjects = ["P01","P03","P04","P05","P06","P07","P08","P09","P10","P11","P12","P13","P14","P15","P16","P17","P18","P19","P20","P21"]
subjects = ["01A"]#,"02A","03A","04A","05A","06A","07A","08A","09A","10A","11A","12A","13A","14A","15A","16A","18A","19A","20A","21A","22A","23A"]
subjects = ["01Y","02Y","03Y","04Y","05Y","06Y","07Y","08Y","09Y","11Y","12Y","13Y"]
#subjects = ["PM01","PM02","PM03","PM04","PM05","PM06","PM07","PM08","PM09","PM11","PM12","PM13","PM14","PM15","PM16"]
split = [int(180275/50),int(191316/50),int(165545/50),int(197434/50),int(189134/50),int(201924/50),int(171029/50),int(153501/50),int(165643/50),int(135574/50),int(164341/50),int(165844/50),int(181286/50),int(176569/50),int(181419/50),int(140479/50),int(130304/50),int(154552/50),int(154928/50),int(228764/50)]
size_of_window = 100
overlap_between_windows = 20#size_of_window/2

# subjects, size_of_window, overlap_between_windows, remove_activities, dc_comp, create_sliding_windows, create_features, create_weka, create_weka_generalized, 
main(subjects, 
	split,
	size_of_window, 
	overlap_between_windows,
	True, # Remove activities from signals
	True, # Create sliding windows,
	True, # Remove_features before creating new?
	True, # Create features? Remember to delete prev file if you are not appending a feature. 
	1.0, # What window-size are the feature generated from?
	False , # Create Weka?
	False, # Create generalized weka?
	False, # Create weka without activities?
	False) # Change labels of activities


''' Activities Adults people: 
0:'none'	
1:'walking'	
2:'Running'	
3:'shuffling'	
4:'stairs (ascending)'	
5:'stairs (descending)'	
6:'standing'	
7:'sitting'	
8:'lying'	
9:'transition'	
10:'Bending'	
11:'Picking'	
12:'Undefined'	
13:'Cycling (sitting)'	
14:'Cycling (stand)'	
15:'Heel-drop'	
16:'Vigorous Activities'	
17:'Non-Vigorous Activities'

'''

''' Activities older people: 
0:'none'	
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
