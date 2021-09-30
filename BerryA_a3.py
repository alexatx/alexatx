# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:18:01 2021

@author: julie
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
plt.close('all')

datfile='C:\\Users\\julie\\3312\\crashdata.csv'
dframe = pd.read_csv(datfile)

alpha = 0.05

### Part A - Data Scrubbing

#(len(dframe)) #2175084

### Dropping all columns EXCEPT: Index, Seating Position, Sex, Injury Severity
columns = ['Year', 'Case Individual ID', 'Case Vehicle ID', 'Victim Status', 'Role Type', 'Ejection', 'License State Code', 'Transported By', 'Safety Equipment', 'Injury Descriptor', 'Age', 'Injury Location']
dframe.drop(columns, axis=1, inplace=True)

### Pare down data to only include Drivers
frame = dframe[dframe['Seating Position'] == 'Driver'] 

### Rename 'Sex' column to 'Gender'
frame.rename(columns={'Sex': 'Gender'}, inplace=True)

### Drop unknown values from 'Gender' column
frame = frame[frame['Gender'] != 'U']

### Drop unknown values from 'Injury Severity' column
frame = frame[frame['Injury Severity'] != 'Injured with Unkn Severity']

## Drop 'Killed' values from 'Injury Severity' column 
frame = frame[frame['Injury Severity'] != 'Killed']
print()
print('Homework Assignment 3 for CSC 3312 by Alex Berry:')
print()
print('Part A:')
print('---------------------------------------------------')
print('Data scrubbing completed.')
print('The original number of data set tuples was: 2,175,084.')
print('The current number of data set tuples is 1,377,317.')
print('---------------------------------------------------')

### Part B - Analysis Approach
print('Part B - Analysis approach...')
print('All analyses use categorical or ordinal values.')
print('Nonparametic analysis techniques will be used.')
print('---------------------------------------------------')

### Part C - Analysis

### Get counts of F vs M
#frame.groupby('Gender').count()) #F = 523057 M = 854260
print('Part C - Analysis...')
print('Checking gender for 50/50 distribution between F and M')
print('Number of Females: 523057 or 37%')
print('Number of Males: 854260 or 62%')
print('P-value of binomial test outcome:' , stats.binom_test(523057, n=1377317, p=0.5))
print('There is a significant difference between the expected and')
print('observed gender frequencies in the data.')
print()
print('Testing for differences between male and female injury severities:')
table = [81606, 7551, 5233, 428667], [89038, 15740, 9538, 739944]
print('Female injury counts by severity')
print('[Minor, Moderate, Severe, Uninjured] are:')
print(table[0])
print()
print('Male injury counts by severity')
print('[Minor, Moderate, Severe, Uninjured] are:')
print(table[1])
print()
print('Males comprised of 62% of the sample...')
print('Injury severities between male and female drivers ' +
      'differed significantly.')
c, p, dof, expected = chi2_contingency(table)
print('Chi-Squared Test:', c, 'p-value:', p)
print()
print('****** End of program output stream ******')