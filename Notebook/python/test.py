import numpy as np
import pandas as pd
import os
from os import path
from os import listdir
from os.path import isfile, join
import math

dirname=os.path.dirname
p = os.path.join(dirname(dirname(__file__)), 'data/'+'P08')


df_x = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_' + 'X.csv', header=None, sep='\,')
df_y = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_' + 'Y.csv', header=None, sep='\,')
df_z = pd.read_csv(p + '/DATA_WINDOW/Axivity_CHEST_Back_' + 'Z.csv', header=None, sep='\,')

df_x = df_x.iloc[0:10]
df_y = df_y.iloc[0:10]
df_z = df_z.iloc[0:10]



df_x_mean = df_x.mean(axis=1)
df_y_mean = df_y.mean(axis=1)
df_z_mean = df_z.mean(axis=1)


print df_x_mean
print df_y_mean
print df_z_mean


df_g = df_x_mean.pow(2,axis=0) + df_y_mean.pow(2,axis=0) + df_z_mean.pow(2,axis=0)
df_g = df_g.apply(np.sqrt)
print df_g

df_div = df_z_mean.div(df_g,axis=0)

print df_div

df_angle = df_div.apply(np.arccos) * 180 / math.pi

print df_angle
