# Alex Berry
# CSC 3312
# Spring 2
# Assignment 1: descriptors of data (mean, median, std)
# including extra credit

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

datfile='C:\\Users\\julie\\3312\\Assignment1Data.csv'
dframe = pd.read_csv(datfile)
yMean = dframe['Y'].mean()
dframe['Diff'] = dframe['Y']-yMean
dframe['DiffSqr'] = dframe['Diff'].pow(2)
total = dframe['DiffSqr'].sum()
count = dframe["DiffSqr"].count()
var = total / (count - 1)
std = np.sqrt(var)
libvar = dframe['Y'].var()
libstd = dframe['Y'].std()
dframe.describe()
yMax = dframe['Y'].max()
yMin = dframe['Y'].min()
yMedian = dframe['Y'].median()
print ("The sample size is:", count)
print ("The max value is:", yMax)
print ("The min value is:", yMin)
print ("The mean value for Y is:", yMean)
print ("The median value for Y is:", yMedian)
print ("The sum of squared differences for Y is:", total)
print ("The variance for Y is:", var)
print ("The standard deviation for Y is:", std)
print()
print ("The library-based calculation for the variance of Y is:", libvar)
print ("The library-based calculation for the standard deviation of Y is:", libstd)
print()
print()
dframe.plot.scatter(x='X', y='Y')
print ("--Extra Credit--")

####### Extra Credit #######
datafile2 ='C:\\Users\\julie\\3312\\a1ECdata.csv'
dframe2 = pd.read_csv(datafile2)

ecvar = dframe2['Y'].var()
print ("The variance for Y in the second data file is:", ecvar)
dframe2.plot.scatter(x='X', y='Y')