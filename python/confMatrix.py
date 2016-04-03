#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt



a="9156    33   311    35    38   330     5     0    60     9     0     0     0     0     0     7     0 \
    22   879     0     3     8     0     0     0     0     0     0     0     0     0     0    69     0 \
  1385     7  1150    20    10  2824    15     0   151    15     0     0     1     1     0    14     0 \
   321     3     5  1433     1     0     0     0    18     0     0     0     0     0     0     4     0 \
   132    19     4     8   586     1     0     0     0     0     0     0     0     0     0    66     1 \
   333     0   340     1     3 17132   438     0    80    64     0     0     0     1     0     0    24 \
     8     0     5     1     0    31 47553   424   450     9     3     0     3     0     0     0     0\
     0     0     0     0     0     0    59  1870    97     0     0     0     0     0     0     1     0 \
    76     0    30    11     0    26    97    94   869    21     0     0     3     2     0     1     2 \
    20     0    14     0     0    39    16     1   119   202     0     0     1     3     0     1     0 \
     0     0     1     0     0    17    18    11    24    42     2     0     0     0     0     0     0 \
     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0 \
     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0 \
     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0 \
     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0 \
     0    42     0     3     0     4     0     0     0     0     0     0     0     0     0    22     0\
    21     0     4     0     1   141    49     3    11     7     0     0     3     0     0     0   122 "



# Split, remove spaces and convert
b = []
a = a.split(" ")
for i in a:
  if i != "":
    b.append(i)
for i in range(0,len(b)):
  b[i] = float(b[i])


# Divide into activity list
n = []

for i in range(0,17):
  n.append(b[i*17:(i+1)*17])

# Remove activities: 
n = np.delete(n, 14, axis=0)
n = np.delete(n, 14, axis=1)
n = np.delete(n, 13, axis=0)
n = np.delete(n, 13, axis=1)
n = np.delete(n, 12, axis=0)
n = np.delete(n, 12, axis=1)
n = np.delete(n, 11, axis=0)
n = np.delete(n, 11, axis=1)



conf_arr = n
# conf_arr = [[6861,526,311,11,0,0,0,2,0], 
#             [843,1836,891,7,0,1,0,2,5], 
#             [314,613,19305,8,0,1,5,0,6], 
#             [2,6,7,20192,3,0,0,3,1], 
#             [0,0,0,12,2177,0,0,0,0], 
#             [0,3,27,0,0,17,0,0,0],
#             [15,1,10,0,0,0,10,0,0], 
#             [1,4,3,10,0,0,0,56,1], 
#             [14,15,79,1,0,0,0,0,111]]


norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(norm_conf), cmap=plt.cm.summer, 
                interpolation='nearest')

width = len(conf_arr)
height = len(conf_arr[0])

for x in xrange(width):
    for y in xrange(height):
        ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
                    horizontalalignment='center',
                    verticalalignment='center')

cb = fig.colorbar(res)

plt.title('Confusion Matrix')
labels = ['Walking', 'Running','shuffling','stairs (ascending)','stairs (descending)','standing','sitting','lying','transition','Bending','Picking','Cycling (sitting)','Cycling (stand)','Vigorous Activities','Non-Vigorous Activities']
plt.xticks(range(width), labels,rotation='vertical')
plt.yticks(range(height), labels)
plt.show()