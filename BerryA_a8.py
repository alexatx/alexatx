# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:21:34 2021

@author: julie
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

datfile='C:\\Users\\julie\\3312\\week8data.csv'
df = pd.read_csv(datfile)

ALPHA = 0.05

print('*********************************************************')
print('***CSC 3312 | Alex Berry | BerryA_a8.py | Assignment 8***')
print('*********************************************************')
print('=========================================================')
print('Data values read from input file...')
# #Drop all but the following columns:
# • 'Height'
# • 'Weight'
print('Scrubbing/Filtering complete.')
origCount = df.size
print('Original row count:', origCount)
df.drop(df.columns.difference(['Height', 'Weight']), 1, inplace=True)
df.dropna(how='all', inplace=True)
index = df.index
rowCount = len(index)
print('Post-processing count:', rowCount) ### Thanks for pointing out I was counting rows wrong!!
print('--------------------------------------')
print('Starting k-means cluster analysis...')
print('======================================')

df['BMI'] = df['Weight']/df['Height'].pow(2)

BMI = df['BMI']
testframe = pd.DataFrame(BMI)

for i in range (2,11):
    if i == 2:
        result2 = KMeans(n_clusters=2,n_init=10).fit(testframe)
    elif i == 3:
        result3 = KMeans(n_clusters=3,n_init=10).fit(testframe)
    elif i == 4:
        result4 = KMeans(n_clusters=4,n_init=10).fit(testframe)
    elif i == 5:
        result5 = KMeans(n_clusters=5,n_init=10).fit(testframe)
    elif i == 6:
        result6 = KMeans(n_clusters=6,n_init=10).fit(testframe)
    elif i == 7:
        result7 = KMeans(n_clusters=7,n_init=10).fit(testframe)
    elif i == 8:
        result8 = KMeans(n_clusters=8,n_init=10).fit(testframe)
    elif i == 9:
        result9 = KMeans(n_clusters=9,n_init=10).fit(testframe)
    elif i == 10:
        result10 = KMeans(n_clusters=10,n_init=10).fit(testframe)

BMI = np.array(df['BMI'])
newBMI = BMI.reshape(-1, 1)

## k = 2
cluster_centers = result2.cluster_centers_
meanDistortion2 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 3
cluster_centers = result3.cluster_centers_
meanDistortion3 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 4
cluster_centers = result4.cluster_centers_
meanDistortion4 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 5
cluster_centers = result5.cluster_centers_
meanDistortion5 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 6
cluster_centers = result6.cluster_centers_
meanDistortion6 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 7
cluster_centers = result7.cluster_centers_
meanDistortion7 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 8
cluster_centers = result8.cluster_centers_
meanDistortion8 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 9
cluster_centers = result9.cluster_centers_
meanDistortion9 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]
## k = 10
cluster_centers = result10.cluster_centers_
meanDistortion10 = sum(np.min(cdist(newBMI, cluster_centers,
 'euclidean'), axis=1))/newBMI.shape[0]

# Finding mean distortion for each k-value
print('For k = 2, the mean distortion is:', meanDistortion2)
print('Cluster centers are:', result2.cluster_centers_[0],'and', result2.cluster_centers_[1])
print()
print('For k = 3, the mean distortion is:', meanDistortion3)
print('Cluster centers are:', result3.cluster_centers_[0],'and', result3.cluster_centers_[1], result3.cluster_centers_[2])
print()
print('For k = 4, the mean distortion is:', meanDistortion4)
print('Cluster centers are:', result4.cluster_centers_[0],'and', result4.cluster_centers_[1], result4.cluster_centers_[2], result4.cluster_centers_[3])
print()
print('For k = 5, the mean distortion is:', meanDistortion5)
print('Cluster centers are:', result5.cluster_centers_[0],'and', result5.cluster_centers_[1], result5.cluster_centers_[2], result5.cluster_centers_[3], result5.cluster_centers_[4])
print()
print('For k = 6, the mean distortion is:', meanDistortion6)
print('Cluster centers are:', result6.cluster_centers_[0],'and', result6.cluster_centers_[1], result6.cluster_centers_[2], result6.cluster_centers_[3], result6.cluster_centers_[4], result6.cluster_centers_[5])
print()
print('For k = 7, the mean distortion is:', meanDistortion7)
print('Cluster centers are:', result7.cluster_centers_[0],'and', result7.cluster_centers_[1], result7.cluster_centers_[2], result7.cluster_centers_[3], result7.cluster_centers_[4], result7.cluster_centers_[5], result7.cluster_centers_[6])
print()
print('For k = 8, the mean distortion is:', meanDistortion8)
print('Cluster centers are:', result8.cluster_centers_[0],'and', result8.cluster_centers_[1], result8.cluster_centers_[2], result8.cluster_centers_[3], result8.cluster_centers_[4], result8.cluster_centers_[5], result8.cluster_centers_[6], result8.cluster_centers_[7])
print()
print('For k = 9, the mean distortion is:', meanDistortion9)
print('Cluster centers are:', result9.cluster_centers_[0],'and', result9.cluster_centers_[1], result9.cluster_centers_[2], result9.cluster_centers_[3], result9.cluster_centers_[4], result9.cluster_centers_[5], result9.cluster_centers_[6], result9.cluster_centers_[7], result9.cluster_centers_[8])
print()
print('For k = 10, the mean distortion is:', meanDistortion10)
print('Cluster centers are:', result10.cluster_centers_[0],'and', result10.cluster_centers_[1], result10.cluster_centers_[2], result10.cluster_centers_[3], result10.cluster_centers_[4], result10.cluster_centers_[5], result10.cluster_centers_[6], result10.cluster_centers_[7], result10.cluster_centers_[8], result10.cluster_centers_[9])

# Creating elbow diagram
distortionList = meanDistortion2, meanDistortion3, meanDistortion4, meanDistortion5, meanDistortion6, meanDistortion7, meanDistortion8, meanDistortion9, meanDistortion10
k = 2, 3, 4, 5, 6, 7, 8, 9, 10
plt.plot(k, distortionList)
plt.xlabel('k-value')
plt.ylabel('Distortion')
plt.title('Elbow Diagram Showing Optimal k')
print()
print('An elbow (distortion) plot has been generation and is available for inspection.')
print()
print('Outcomes and Findings')
print('---------------------')
print('The distortion inflection occurs at the value k = 6.')
print('The optimal value of k appeares more consistent with the CDC (6) than')
print('the NObeyesdad count determined by the study designers (7).')
print()
print('****** Boom ******')
