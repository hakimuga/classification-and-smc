
from sklearn.linear_model import LogisticRegression
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import scipy.spatial.distance as sdist
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv
import collections


train_file_path = "/home/baouyaa/VMSHARED/telvadataset.csv"

dataframe = pd.read_csv(train_file_path)

print('========================')
print('DATAFRAME DISCRETIZATION')
print('========================')

dataframe = dataframe.dropna()

origin_date = dataframe.pop('date')

origin_water_flow = dataframe.pop('water_flow')

origin_water_volume = dataframe.pop('water_volume')

origin_water_height = dataframe.pop('water_height')

origin_water_precipitation = dataframe.pop('water_precipitation')

n_bins=6

dataframe['water_flow'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_flow)).reshape(-1, 1))

dataframe['water_volume'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_volume)).reshape(-1, 1))

dataframe['water_height'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_height)).reshape(-1, 1))

dataframe['water_precipitation'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_precipitation)).reshape(-1, 1))



#combinig weather and temp into single listof tuples
features=list(zip(dataframe['water_volume'], dataframe['water_height'], dataframe['water_precipitation']))

model = LogisticRegression()

# Train the model using the training sets
model.fit(features,dataframe['water_flow'])

#Predict Output
predicted= model.predict(features) # 0:Overcast, 2:Mild

#print("PREDICTION ", predicted)

merged_df = np.column_stack(( dataframe['water_volume'], dataframe['water_height'], dataframe['water_precipitation'], dataframe['water_flow'], predicted ))

matrix_size = len(merged_df)

print("Trained data size :", matrix_size)
#merged_df = np.delete(merged_df, (0), axis=0)

print("PREDICTION ", merged_df)
pd.DataFrame(merged_df).to_csv("classification.csv")


c1 = []
c2 = []
c3 = []

for row in merged_df:
    if row[4] == 0 :
        c1.append(row)
    if row[4] == 1 :
        c2.append(row)
    if row[4] == 2 :
        c3.append(row)


pd.DataFrame(c1).to_csv("class1.csv")

pd.DataFrame(c2).to_csv("class2.csv")

pd.DataFrame(c3).to_csv("class3.csv")


print('========================')
print('WATER FLOW RATE')
print('========================')



c1 =np.array(c1)
c2 =np.array(c2)
c3 =np.array(c3)


print('========================')
print('WATER FLOW RATE - Class 1')
print('========================')

matrix_size = len(c1)

print("Class 1 size :", matrix_size)

y = c1[:, 3]

print (y)
freq = collections.Counter(y)

for (key, value) in freq.items():
    print(key, " -> ", value/matrix_size)

#frequencies = np.asarray((unique, counts)).T

print('========================')
print('WATER FLOW RATE - Class 2')
print('========================')

matrix_size = len(c2)

print("Class 2 size :", matrix_size)

y = c2[:, 3]

print (y)
freq = collections.Counter(y)

for (key, value) in freq.items():
    print(key, " -> ", value/matrix_size)


print('========================')
print('WATER FLOW RATE - Class 3')
print('========================')

matrix_size = len(c3)

print("Class 3 size :", matrix_size)

y = c3[:, 3]

print (y)
freq = collections.Counter(y)

for (key, value) in freq.items():
    print(key, " -> ", value/matrix_size)
