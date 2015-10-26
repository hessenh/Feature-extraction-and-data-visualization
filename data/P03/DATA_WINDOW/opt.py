import pandas as pd
import numpy as np

df_x = pd.read_csv('Axivity_THIGH_Left_X.csv', header=None, sep='\,')
df_y = pd.read_csv('Axivity_THIGH_Left_Y.csv', header=None, sep='\,')
df_z = pd.read_csv('Axivity_THIGH_Left_Z.csv', header=None, sep='\,')


def zero_crossing(l):
	return len(np.where(np.diff(np.sign(l.values)))[0])*1.0 / len(l.values)


def rms(l):
	return np.sqrt(l.dot(l)*1.0/len(l.values))

def cor(l,o):

	print o


df_x = df_x[0:10]


def fft_mean(l):
    fft = np.fft.fft(l)
    print ftt
    return np.mean(abs(fft))

#print df_x.apply(fft_mean, axis=1)


#print ((np.sqrt(np.square(df_x.sub(np.mean(df_x,axis=1),axis=0)).sum(axis=1)) + np.sqrt(np.square(df_y.sub(np.mean(df_y,axis=1),axis=0)).sum(axis=1)) + np.sqrt(np.square(df_z.sub(np.mean(df_z,axis=1),axis=0)).sum(axis=1)))/3.0)/len(df_x.iloc[0].values)


#print df_n.iloc[0]

def sum_of_square(axis):
    l = []
    for i in axis:
        l.append(float(i))
    mean = sum(l)*1.0/len(l)
    s = 0
    for i in l:
        s += (i-mean)**2
    return s**0.5

x = [-0.048714,-0.036863,-0.03307,-0.053156,-0.076115,-0.081725,-0.077405,-0.061581,-0.054688,-0.054688,-0.056015,-0.058594,-0.049492,-0.03665,-0.057759,-0.047182,-0.080882,-0.15898,-0.17762,-0.19861,-0.10873,-0.065334,-0.049074,-0.016008,-0.035156,-0.038949,0.027803,0.15375,0.23453,0.38213,0.48564,0.36783,0.12002,0.0087602,0.048215,0.017578,-0.19933,-0.16975,-0.058173,-0.0446,-0.10218,-0.16922,-0.13637,-0.048127,-0.033625,-0.10778,-0.21986,-0.32953,-0.41889,-0.44967]
y = [1.0074,1.0146,0.9953,1.0083,1.0028,1.0249,1.0535,1.0101,1.0108,1.0199,1.0181,1.0086,1.0023,0.99207,1.1139,1.0176,0.93566,1.1107,0.94393,1.1128,1.0938,1.2114,1.3208,1.2523,1.1719,1.005,0.96657,1.0117,1.0262,1.1297,1.0612,0.98563,0.80308,0.8133,0.99621,1.1226,1.0571,0.64256,0.98315,1.3377,1.2039,0.95623,0.85673,0.90371,1.0129,1.0761,1.0961,1.1462,1.1514,1.0691]
z = [-0.098116,-0.10938,-0.11563,-0.10317,-0.082145,-0.085325,-0.097163,-0.10639,-0.092043,-0.05576,-0.057418,-0.071538,-0.070806,-0.079044,-0.13638,-0.1466,-0.037072,0.037204,0.044577,0.0080779,-0.15765,-0.20596,-0.18534,-0.063419,0.085938,0.2566,0.37688,0.48369,0.50276,0.14893,-0.32881,-0.48293,-0.41207,-0.43917,-0.21427,-0.0017234,0.085634,0.080325,0.18834,0.1933,-0.0036766,-0.20495,-0.26471,-0.17646,-0.013863,0.096974,0.15889,0.20312,0.19669,0.15564]

#print 'mean', np.mean(x)
#print ((sum_of_square(x) + sum_of_square(y)+ sum_of_square(z))*1.0 / 3)/50

def fft_spectral_centroid(l):
    fft = np.fft.fft(l)
    fft = fft[0:50]
    sum_frequency_times_amplitude = 0
    sum_amplitude = 0
    for x in range(0, 50):
        sum_frequency_times_amplitude += x * abs(fft[x])
        sum_amplitude += abs(fft[x])

    print sum_frequency_times_amplitude/sum_amplitude
    return sum_frequency_times_amplitude/sum_amplitude

df_x = df_x[0:10]
print df_x
data_frame_result = df_x.apply(fft_spectral_centroid,axis=1).to_frame()

