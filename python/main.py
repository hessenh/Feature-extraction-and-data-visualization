import numpy as np
import matplotlib.pylab as plt
import os.path
from KnnDtw import KnnDtw

# Import the HAR dataset
x_train_file = open(os.path.dirname(__file__) + '/../K-Nearest-Neighbors-with-Dynamic-Time-Warping-master/data/UCI-HAR-Dataset/train/X_train.txt', 'r')
y_train_file = open(os.path.dirname(__file__) + '/../K-Nearest-Neighbors-with-Dynamic-Time-Warping-master/data/UCI-HAR-Dataset/train/y_train.txt', 'r')

x_test_file = open(os.path.dirname(__file__) + '/../K-Nearest-Neighbors-with-Dynamic-Time-Warping-master/data/UCI-HAR-Dataset/test/X_test.txt', 'r')
y_test_file = open(os.path.dirname(__file__) + '/../K-Nearest-Neighbors-with-Dynamic-Time-Warping-master/data/UCI-HAR-Dataset/test/y_test.txt', 'r')

# Create empty lists
x_train = []
y_train = []
x_test = []
y_test = []

# Mapping table for classes
labels = {1:'WALKING', 2:'WALKING UPSTAIRS', 3:'WALKING DOWNSTAIRS',
          4:'SITTING', 5:'STANDING', 6:'LAYING'}

# Loop through datasets
for x in x_train_file:
    x_train.append([float(ts) for ts in x.split()])
    
for y in y_train_file:
    y_train.append(int(y.rstrip('\n')))
    
for x in x_test_file:
    x_test.append([float(ts) for ts in x.split()])
    
for y in y_test_file:
    y_test.append(int(y.rstrip('\n')))
    
# Convert to numpy for efficiency
x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)



plt.figure(figsize=(11,7))
colors = ['#D62728','#2C9F2C','#FD7F23','#1F77B4','#9467BD',
          '#8C564A','#7F7F7F','#1FBECF','#E377C2','#BCBD27']

for i, r in enumerate([0,27,65,100,145,172]):
    plt.subplot(3,2,i+1)
    plt.plot(x_train[r][:100], label=labels[y_train[r]], color=colors[i], linewidth=2)
    plt.xlabel('Samples @50Hz')
    plt.legend(loc='upper left')
    plt.tight_layout()

#plt.show()
m = KnnDtw(n_neighbors=1, max_warping_window=10)
m.fit(x_train[::10], y_train[::10])
label, proba = m.predict(x_test[::10])