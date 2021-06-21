

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



train_file_path = "/source.csv"

dataframe = pd.read_csv(train_file_path)

print('========================')
print('DATAFRAME DISCRITISATION')
print('========================')

dataframe = dataframe.dropna()

origin_date = dataframe.pop('date')

origin_water_flow = dataframe.pop('water_flow')

origin_water_volume = dataframe.pop('water_volume')

origin_water_height = dataframe.pop('water_height')

origin_water_precipitation = dataframe.pop('water_precipitation')

n_bins=3

dataframe['water_flow'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_flow)).reshape(-1, 1))

dataframe['water_volume'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_volume)).reshape(-1, 1))

dataframe['water_height'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_height)).reshape(-1, 1))

dataframe['water_precipitation'] = KBinsDiscretizer(n_bins=3, encode='ordinal').fit_transform(np.array(list(origin_water_precipitation)).reshape(-1, 1))



merged_df = np.column_stack(( origin_date, dataframe['water_flow'], dataframe['water_volume'], dataframe['water_height'], dataframe['water_precipitation'] ))


pd.DataFrame(merged_df).to_csv("discritization.csv")

