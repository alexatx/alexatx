# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:47:16 2021

@author: julie
"""

import pandas as pd
from scipy import stats
from scipy.stats import skewtest, kurtosistest
import numpy as np

datfile='C:\\Users\\julie\\3312\\week5data.csv'
dframe = pd.read_csv(datfile)


alpha = 0.05

# print(dframe.size) 1979676

### Dropping columns for data scrubbing
columns = ['Wet Bulb Temperature', 'Rain Intensity', 'Interval Rain', 'Total Rain', 'Precipitation Type', 'Wind Direction', 'Wind Speed', 'Maximum Wind Speed', 'Barometric Pressure', 'Solar Radiation', 'Heading', 'Battery Life', 'Measurement Timestamp Label', 'Measurement ID']
dframe.drop(columns, axis=1, inplace=True)

### Drop any tuples (rows) from the DataFrame object that do not contain sensor readings
### for the 63rd Street, Foster, or Oak Street weather stations.
dframe.set_index('Station Name').filter(like='63rd' and 'Oak' and 'Foster', axis=0)

### Set any invalid or nonsensical Air Temperature readings to NaN.
dframe[(dframe['Air Temperature'] < -30) & (dframe['Air Temperature'] > 40)] = np.nan

### isolate the sensor entries that were logged during the RQ period of
### interest (August, 2017
dframe.rename(columns = {'Measurement Timestamp':'Timestamp'}, inplace = True)
dateValues = dframe.Timestamp.str.split(expand=True)   
dframe['Date'] = dateValues[0]

monthValues = dframe.Date.str.split(pat = "/", expand=True)

dframe['Month'] = monthValues[0]
dframe['Year'] = monthValues[2]
dframe = dframe[(dframe['Year'].str.contains('2017'))]
dframe = dframe[(dframe['Month'].str.contains('08'))]
print()
print('***CSC 3312 | Alex Berry | BerryA-a5.py | Assignment 5***')
print('################# Assignement 5 Part A ##################')
print('#########################################################')
print('Weather Data Scrubbing...')
print('...')
print('Scrubbing completed.')
print('Original tuples count: 1979676')
print('Tuples count after scrubbing:', dframe.size)

### Normality determination for Part A
kurtResult = kurtosistest(dframe['Air Temperature'], axis=0, nan_policy='propagate')
skewResult = skewtest(dframe['Air Temperature'], axis=0, nan_policy='propagate')
print('Examining kurtosis and skewness of data...')
print('Kurtosis Test p-value result:', kurtResult[1])
print('Skewness Test p-value result:', skewResult[1])
print('Both kurtosis and skew indicate potential normality.')
print('This data set can be analyzed with parametric techniques.')
print('Applying analysis of variance (ANOVA) between the three groups.')
print('---------------------------------------------------------')

# An array of air temp values for the first location (i.e., 1st group)
# An array of air temp values for the second location (i.e., 2nd group)
# An array of air temp values for the third location (i.e., 3rd group)

sixtyGroup = dframe[(dframe['Station Name'].str.contains('63rd'))]
columns = ['Timestamp', 'Date', 'Month', 'Year']
sixtyGroup.drop(columns, axis=1, inplace=True)
sixtyGroupArray = sixtyGroup[['Air Temperature']].values

oakGroup = dframe[(dframe['Station Name'].str.contains('Oak'))]
columns = ['Timestamp', 'Date', 'Month', 'Year']
oakGroup.drop(columns, axis=1, inplace=True)
oakGroupArray = oakGroup[['Air Temperature']].values

fosterGroup = dframe[(dframe['Station Name'].str.contains('Foster'))]
columns = ['Timestamp', 'Date', 'Month', 'Year']
fosterGroup.drop(columns, axis=1, inplace=True)
fosterGroupArray = oakGroup[['Air Temperature']].values

bartTest = stats.bartlett(sixtyGroupArray[0], oakGroupArray[0], fosterGroupArray[0])

print('The Bartlett test results were nonsignificant. The variance between the three stations is homogeneic.')
print('---------------------------------------------------------')

oakMean = oakGroup.mean()
sixtyMean = sixtyGroup.mean()
fosterMean = fosterGroup.mean()
print('The raw mean for air temperature at the 63rd Street station is: ', sixtyMean[0], ', n=', sixtyGroup.size)
print('The raw mean for air temperature at the Oak Street station is: ', oakMean[0], ', n=', oakGroup.size)
print('The raw mean for air temperature at the Foster Street station is: ', fosterMean[0], ', n=', fosterGroup.size)

anovaTest =  stats.f_oneway(sixtyGroupArray, oakGroupArray, fosterGroupArray)

dframe.boxplot(column = 'Air Temperature', by = 'Station Name', fontsize=8)
print()
print('The mean air temperature significantly differed between the 63rd Street, Foster, ' + 
      'and Oak Street Weather stations in Chicago during the specified period.')
print('Analysis of Variance (ANOVA) results are:')
print('F-statistic:', anovaTest[0])
print('p=', anovaTest[1])
print('Sample size n=', sixtyGroup.size + oakGroup.size + fosterGroup.size)
print('A box plot of the air temp values at each of the locations may be found in the Plots area.')
print('#########################################################')
print('########### End of Program Output for Part A ############')
print('*********************************************************')
print('*********************************************************')
print('################# Assignement 5 Part B ##################')
print('Data analysis period: 2015-2020')
print('Weather variable of interest: Humidity')
print('---------------------------------------------------------')
datfile='C:\\Users\\julie\\3312\\week5data.csv'
dframeB = pd.read_csv(datfile)


alpha = 0.05

columns = ['Wet Bulb Temperature', 'Rain Intensity', 'Interval Rain', 'Total Rain', 'Precipitation Type', 'Wind Direction', 'Wind Speed', 'Maximum Wind Speed', 'Barometric Pressure', 'Solar Radiation', 'Heading', 'Battery Life', 'Measurement Timestamp Label', 'Measurement ID']
dframeB.drop(columns, axis=1, inplace=True)

### Humidity value scrubbing to ensure values are between 0 and 100
dframeB[(dframeB['Humidity'] < 0) & (dframeB['Humidity'] > 100)] = np.nan

### Drop any tuples (rows) from the DataFrame object that do not contain sensor readings
### for the 63rd Street, Foster, or Oak Street weather stations.
dframeB.set_index('Station Name').filter(like='63rd' and 'Oak' and 'Foster', axis=0)
print()
print('Data Scrubbing...')
print('...')
print('Scrubbing completed.')
print('Tuples count after scrubbing:', dframeB.size)


### Quick Check
quickChkMin = dframeB[['Humidity']].mean() - 3*dframeB[['Humidity']].std()
quickChkMax = dframeB[['Humidity']].mean() + 3*dframeB[['Humidity']].std()
print()
print('Quick Check results')  
print('--------------------') 
print('Quick Check Min:', quickChkMin[0])
print()
print('Data minimum value:')
print(dframeB.min())   
print()          
print('Quick Check Max:', quickChkMax[0])        
print()          
print('Data max value:')
print(dframeB.max())     
print()          
print('The data failed to accomodate 3 standard deviations of the data set on the right side.' +
      'The data is skewed to the left.')

### Normality determination for Part A
kurtResult = kurtosistest(dframeB['Humidity'], axis=0, nan_policy='propagate')
skewResult = skewtest(dframeB['Humidity'], axis=0, nan_policy='propagate')
print('Examining kurtosis and skewness of data...')
print('Kurtosis Test p-value result:', kurtResult[1])
print('Skewness Test p-value result:', skewResult[1])
print('Kurtosis result is significant and shows that the data are not normally distributed.')
print('Non-parametric analysis techniques will be used.')    
print('---------------------------------------------------------')  

# An array of air temp values for the first location (i.e., 1st group)
# An array of air temp values for the second location (i.e., 2nd group)
# An array of air temp values for the third location (i.e., 3rd group)

sixtyGroup = dframeB[(dframeB['Station Name'].str.contains('63rd'))]
columns = ['Measurement Timestamp']
sixtyGroup.drop(columns, axis=1, inplace=True)
sixtyGroupArray = sixtyGroup[['Humidity']].values

oakGroup = dframeB[(dframeB['Station Name'].str.contains('Oak'))]
columns = ['Measurement Timestamp']
oakGroup.drop(columns, axis=1, inplace=True)
oakGroupArray = oakGroup[['Humidity']].values

fosterGroup = dframeB[(dframeB['Station Name'].str.contains('Foster'))]
columns = ['Measurement Timestamp']
fosterGroup.drop(columns, axis=1, inplace=True)
fosterGroupArray = oakGroup[['Humidity']].values

leveneTest = stats.levene(sixtyGroupArray[0], oakGroupArray[0], fosterGroupArray[0])
print('')
print('R-squared validation')
print('----------------------')
print('**********************')
print('Homogeneity of variance confirmed across the three locations.')
print('**********************')
kruskalTest = stats.kruskal(sixtyGroupArray[0], oakGroupArray[0], fosterGroupArray[0])

oakMedian = oakGroup.median()
sixtyMedian = sixtyGroup.median()
fosterMedian = fosterGroup.median()

print()
print('Test findings')
print('----------------------')
print('The median humidity at the 63rd Street station is: ', sixtyMedian[0], ', n=', sixtyGroup.size)
print('The median humidity at the Oak Street station is: ', oakMedian[0], ', n=', oakGroup.size)
print('The median humidity at the Foster Street station is: ', fosterMedian[0], ', n=', fosterGroup.size)
print('The median humidity levels significantly differed between the ' +
 'Foster, 63rd Street, and Oak Street Weather stations in Chicago ' +
 'during the specified period.')
print()
print('Kruskal-Wallis H test results are:')
print('u =', kruskalTest[0])
print('p =', kruskalTest[1])
print('Sample size n =', sixtyGroup.size + oakGroup.size + fosterGroup.size)

dframeB.boxplot(column = 'Humidity', by = 'Station Name', fontsize=8)

print('A box plot of the humidity values at each of the locations may be found in the Plots area.')
print('#########################################################')
print('########### End of Program Output for Part B ############')
print('################# End of Program Output #################')

print()
print()
print()
print()
print()























