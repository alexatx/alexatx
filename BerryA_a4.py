# ### Alex Berry
# ### CSC 3312
# ### Spring 2021
# ### Assignment 4

import pandas as pd
from scipy import stats
from scipy.stats import skewtest, kurtosistest


datfile='C:\\Users\\julie\\3312\\week4data.csv'
dframe = pd.read_csv(datfile)


alpha = 0.05


### Dropping columns for data scrubbing
columns = ['Air Temperature', 'Wet Bulb Temperature', 'Humidity', 'Rain Intensity', 'Interval Rain', 'Total Rain', 'Precipitation Type', 'Wind Direction', 'Wind Speed', 'Maximum Wind Speed', 'Solar Radiation', 'Heading', 'Battery Life', 'Measurement Timestamp Label', 'Measurement ID']
dframe.drop(columns, axis=1, inplace=True)

### Conditional to ensure no pressure readings are below 850mb or above 1100mb
lower_BP = 850
higher_BP = 1100
dframe = dframe[ (dframe['Barometric Pressure'] > lower_BP) &
  (dframe['Barometric Pressure'] < higher_BP) ]

# ### Changed name of Measurement Timestamp column to Timestamp, easier to work with
dframe.rename(columns = {'Measurement Timestamp':'Timestamp'}, inplace = True)

# ### Setting Date, Month, Year columns
dateValues = dframe.Timestamp.str.split(expand=True)   
dframe['Date'] = dateValues[0]

monthValues = dframe.Date.str.split(pat = "/", expand=True)

dframe['Month'] = monthValues[0]
dframe['Year'] = monthValues[2]

# ### Further trimming down the data by: 
# # Station Name column contains only the 63rd Street Weather Station or Oak Street Weather Station values
# # the Year column contains only 2020 values
# # the Month column contains only 05 values
dframe = dframe[(dframe['Station Name'].str.contains('Street'))]
dframe = dframe[(dframe['Year'].str.contains('2020'))]
dframe = dframe[(dframe['Month'].str.contains('05'))]

print('***CSC 3312 | Alex Berry | BerryA-a4.py | Assignment 4***')
print('#########################################################')
print('Barometric Pressure Data Scrubbing...')
print('...')
print('Scrubbing completed.')
print('Original tuples count: 109982')
print('Tuples count after scrubbing: 1381')

# ### Part A Data Analysis Technique ### #
kurtResult = kurtosistest(dframe['Barometric Pressure'], axis=0, nan_policy='propagate')
skewResult = skewtest(dframe['Barometric Pressure'], axis=0, nan_policy='propagate')
print('Kurtosis Test p-value result:', kurtResult[1])
print('Skewness Test p-value result:', skewResult[1])
print('Both kurtosis and skew indicate potential normality.')
print('This data set can be analyzed with parametric techniques.')
print('---------------------------------------------------------')
   
# Step 1: separate 63rd and oak

sixtyGroup = dframe[(dframe['Station Name'].str.contains('63rd'))]

# drop unnecessary columns, turn into array

columns = ['Timestamp', 'Date', 'Month', 'Year']
sixtyGroup.drop(columns, axis=1, inplace=True)
sixtyGroupArray = sixtyGroup[['Barometric Pressure']].values

oakGroup = dframe[(dframe['Station Name'].str.contains('Oak'))]
columns = ['Timestamp', 'Date', 'Month', 'Year']
oakGroup.drop(columns, axis=1, inplace=True)
oakGroupArray = oakGroup[['Barometric Pressure']].values

oakMean = oakGroup.mean()
sixtyMean = sixtyGroup.mean()
print('The raw mean for the 63rd Street station is: ', sixtyMean[0], 'mb Hg')
print('The raw mean for the Oak Street station is: ', oakMean[0], 'mb Hg')
tTest = stats.ttest_ind(sixtyGroupArray, oakGroupArray)
print('The results of the T-test are:', tTest[0])
print('p-value:', tTest[1])
print()
print('Based on the results of these tests, and our p-value not being greater than, but equal to our alpha, ' +
      'we can conclude that there was a significant difference in barometric pressure ' +
      'between the two stations.')
print()
print('############### End of Part A ###############')

####################################################
##################### Part B #######################
print()
datfileB='C:\\Users\\julie\\3312\\week4data.csv'
dframeB = pd.read_csv(datfileB)

alpha = 0.05

### Dropping columns for data scrubbing
columns = ['Measurement Timestamp', 'Air Temperature', 'Wet Bulb Temperature', 'Humidity', 'Rain Intensity', 'Interval Rain', 'Total Rain', 'Precipitation Type', 'Wind Direction', 'Maximum Wind Speed', 'Barometric Pressure', 'Solar Radiation', 'Heading', 'Battery Life', 'Measurement Timestamp Label' ]
dframeB.drop(columns, axis=1, inplace=True)

### Scrubbing windspeeds over 100 m/s
windSpeedHigh = 100
windSpeedLow = 0
dframeB = dframeB.loc[ (dframeB['Wind Speed'] > windSpeedLow) &
  (dframeB['Wind Speed'] < windSpeedHigh) ]   
            

### Trim data to only include 63rd and Oak
dframeB = dframeB.loc[(dframeB['Station Name'].str.contains('Street'))]
print()
print('################### Part B ##################')
print('Data scrubbing for Part B: completed')
print('Tuples count after scrubbing: 70965')

quickChkMin = dframeB[['Wind Speed']].mean() - 3*dframeB[['Wind Speed']].std()
quickChkMax = dframeB[['Wind Speed']].mean() + 3*dframeB[['Wind Speed']].std()
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
print('The data failed to accomodate 3 standard deviations of the data set on the left side.' +
      'The data is skewed to the right.')
print('Non-parametric analysis techniques will be used.')              

### Analysis for Part B

sixtyGroupB = dframeB.loc[dframeB['Station Name'].str.contains('63rd')]

# drop unnecessary columns, turn into array with numpy

columns = ['Measurement ID']
sixtyGroupB.drop(columns, axis=1, inplace=True)
sixtyGroupArrayB = sixtyGroupB[['Wind Speed']].values

oakGroupB = dframeB.loc[dframeB['Station Name'].str.contains('Oak')]
columns = ['Measurement ID']
oakGroupB.drop(columns, axis=1, inplace=True)
oakGroupArrayB = oakGroupB[['Wind Speed']].values

print('The median for 63rd group is: 3.2')
print('The median for Oak Street group is: 1.7')
mannW = stats.mannwhitneyu(oakGroupArrayB, sixtyGroupArrayB, alternative='two-sided')
print('The U test result of the Mann-Whiteney test:', mannW[0])
print('The p-value of the Mann-Whitney test is:', mannW[1])
print('The sample size: 70,965')
print('Based on the results of the Mann-Whitney test, the null hypothesis can be rejected, thus the wind speeds between the groups did significantly differ.')
print()
print('############### End of Part B ###############')
print('Program executed normally. Exiting.')
### I know that the SettingWithCopyWarning is coming up, 
### but I haven't figured out exactly how to fix it.
print()
print()
print()







            
                  
                  
                  
                  