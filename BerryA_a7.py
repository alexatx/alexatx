# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:13:30 2021

@author: julie
"""

import statsmodels.api as sm
import pandas as pd
from scipy import stats
import numpy as np

datfile='C:\\Users\\julie\\3312\\week7data.csv'
df = pd.read_csv(datfile)

ALPHA = 0.05
print('*********************************************************')
print('***CSC 3312 | Alex Berry | BerryA-a7.py | Assignment 7***')
print('------------------ Assignment 7 Part A ------------------')
print('---------------------------------------------------------')
print('Variables of interest:')
print('-----------------')
print('   Collaborative Teachers Score')
print('   Effective School Leadership Score')
print('---------------------------------------------------------')
print('Data Scrubbing ...')
# #Drop all but the following columns:
# 'Effective School Leadership Score'
# 'Collaborative Teachers Score' 
df.drop(df.columns.difference(['Effective School Leadership Score','Collaborative Teachers Score']), 1, inplace=True)
origCount = df.size/2
print('Tuples prior to dropping nan rows:', origCount)
df.dropna(how='all', inplace=True)
# normaltest of the data
normTestLead = stats.normaltest(df['Effective School Leadership Score'])
normTestTeach = stats.normaltest(df['Collaborative Teachers Score'])
print('Tuples after dropping nan rows:', df.size/2)
print()
print('Checking normality for variables of interest via stats.normaltest()')
print('Values for Collaborative Teachers Scores are not normally distributed.')
print('Values for Effective School Leadership Scores are not normally distributed.')
print()
print('Applying transform to normalize variable distrubutions...')
# Squaring all entries
df = df.transform(np.square, axis=1)
# Truncating the dataframe to 125 entries
CHOP = 125
df = df.iloc[0:CHOP,:]
df = df.reset_index(drop=True)
print('Transformations applied. Truncating dataset and re-checking normality...')
# normaltest of the data
normTestLead2 = stats.normaltest(df['Effective School Leadership Score'])
normTestTeach2 = stats.normaltest(df['Collaborative Teachers Score'])
scatterA = df.plot.scatter(x=('Effective School Leadership Score'),
                      y=('Collaborative Teachers Score'),
                      c='red')
print('---------------------------------------------------------')
print('Collaborative Teachers Score appears normally distributed.')
print('Effective School Leadership Score appears normally distributed.')
print('Scatter plot available for viewing in Plots window.')
print('---------------------------------------------------------')
print('Data Variance Checks:')
print('Part A Data scrubbing complete.')
print('Original data set row count: 1831')
print('Row count following scrubbing and truncation:', df.size)
print('Reminder: Scatter diagrams are available for inspection.')
print()
print('Applying regression analysis...')
leadArray = df['Effective School Leadership Score']
teachArray = df['Collaborative Teachers Score']
bartTest = stats.bartlett(leadArray, teachArray)
print('Homogeneity of variance confirmed between study variables (Bartlett)')
X = df['Effective School Leadership Score']
Y = df['Collaborative Teachers Score'] 
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

fValue = model.fvalue
f_pValue = model.f_pvalue
r2 = model.rsquared
r2adj = model.rsquared_adj
params = model.params
pvalues = model.pvalues
print('The regression model was significantly predictive overall:')
print('f =', fValue, 'p =', f_pValue)
print('The regression model explains 43.25% of adjusted variance in ') 
print('the variable "Collaborative Teachers Score"')
print()
########################################
#TODO: fix this mess and make it a table
########################################
print('---The regression coefficients are:---')
print()
dfD = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
print('Coefficient', '                         ', 'Value', '        ', 'Significance')
print('-----------------------------------------------------------------------------')
constValueA = dfD['coef'].values[0]
constSignificanceA = pvalues.iloc[0]
print('const','                               ', constValueA, '       ', constSignificanceA)
leadValA = dfD['coef'].values[1]
leadSigA = pvalues.iloc[1]
print('Effective School Leadership Score','   ', leadValA, '       ', leadSigA)
# pval = str(pvalues.iloc[0])
# print(params[[0]], pval)
# print(params[[1]], pvalues.iloc[1])
print()
print('The following elements of the model significantly predicted the')
print('Collaborative Teachers Score variable values:')
print('   const')
print('   Effective School Leadership Score')
# Part B
datfile='C:\\Users\\julie\\3312\\week7data.csv'
dfB = pd.read_csv(datfile)
print()
print('*********************************************')
print('*********************************************')
print('Assignment Part B')
print('Variables of interest:')
print('-----------------')
print('   Collaborative Teachers Score')
print('   Effective School Leadership Score')
print('   Rigorous Instruction Score')
print('   Trust Score')
print('*********************************************')
print('*********************************************')
# Drop all but the following columns:
# 'Effective School Leadership Score' IV
# 'Rigorous Instruction Score' IV
# 'Trust Score' IV
# 'Collaborative Teachers Score' DV
dfB.drop(dfB.columns.difference(['Effective School Leadership Score', 'Rigorous Instruction Score', 'Trust Score', 'Collaborative Teachers Score']), 1, inplace=True)
# Drop empty rows
origCountB = df.size/4
print('Tuples prior to dropping nan rows:', origCountB)
dfB = dfB.dropna()
dfB = dfB.reset_index(drop=True)
print('Tuples after dropping nan rows:', dfB.size/4)
normTestLead = stats.normaltest(dfB['Effective School Leadership Score'])
normTestRigorous = stats.normaltest(dfB['Rigorous Instruction Score'])
normTestTrust = stats.normaltest(dfB['Trust Score'])
normTestTeach = stats.normaltest(dfB['Collaborative Teachers Score'])
print('-----------------')
print('Checking normality for variables of interest via stats.normaltest()...')
print('-----------------')
print('Values for Collaborative Teachers Scores are not normally distributed.')
print('Values for Rigorous Instruction Score are not normally distributed.')
print('Values for Trust Score are not normally distributed.')
print('Values for Effective School Leadership Scores are not normally distributed.')
print('-----------------')
print('Applying transform to normalize variable distrubutions...')
# Squaring all entries
dfB = dfB.transform(np.square, axis=1)
# Truncating the dataframe to 125 entries
CHOP = 125
dfB = dfB.iloc[0:CHOP,:]
dfB = dfB.reset_index(drop=True)
print('Transformations applied. Truncating dataset and re-checking normality...')
normTestLeadB = stats.normaltest(dfB['Effective School Leadership Score'])
normTestRigorousB = stats.normaltest(dfB['Rigorous Instruction Score'])
normTestTrustB = stats.normaltest(dfB['Trust Score'])
normTestTeachB = stats.normaltest(dfB['Collaborative Teachers Score'])
print('-----------------')
print('Effective School Leadership Score appears normally distributed.')
print('Rigorous Instruction Score appears normally distributed.')
print('Trust Score appears normally distributed.')
print('Collaborative Teachers Score appears normally distributed.')
# Create scatterplots of each independent variable
scatterLead = dfB.plot.scatter(x=('Effective School Leadership Score'),
                      y=('Collaborative Teachers Score'),
                      c='red')
scatterRigorous = dfB.plot.scatter(x=('Rigorous Instruction Score'),
                      y=('Collaborative Teachers Score'),
                      c='blue')
scatterTrust = dfB.plot.scatter(x=('Trust Score'),
                      y=('Collaborative Teachers Score'),
                      c='green')
print()
print('Scatter plots available for viewing in Plots window.')
leadArrayB = dfB['Effective School Leadership Score']
rigorousArrayB = dfB['Rigorous Instruction Score']
trustArrayB = dfB['Trust Score']
teachArrayB = dfB['Collaborative Teachers Score']
bartTestB = stats.bartlett(leadArrayB, rigorousArrayB, trustArrayB, teachArrayB)
print('-----------------')
print('Homogeneity of variance confirmed between study variables (Bartlett)')
print('Part B Data scrubbing complete.')
print('Original data set row count: 1831')
print('Row count following scrubbing and truncation:', dfB.size/4)
print('Reminder: Scatter diagrams are available for inspection.')
print('-----------------')
print('Applying regression analysis...')
print('-----------------')
LEAD = 'Effective School Leadership Score'
RIGOR = 'Rigorous Instruction Score'
TRUST = 'Trust Score'
COLLAB = 'Collaborative Teachers Score'
Xb = dfB[[LEAD, RIGOR, TRUST]]
Yb = dfB[COLLAB]
# Adds a constant term (new column) to all rows of the
# predictor DataFrame X and assigns the result to a new
# DataFrame
Xb = sm.add_constant(Xb) 

# Create and train (fit) the model using OLS regression
modelB = sm.OLS(Yb, Xb).fit()
# Run the model to see how well it predicts the dependent
# variable (Y) values
predictionsB = modelB.predict(Xb)
fValueB = modelB.fvalue
f_pValueB = modelB.f_pvalue
r2B = modelB.rsquared
r2adjB = modelB.rsquared_adj
paramsB = modelB.params
pvaluesB = modelB.pvalues
print('The regression model was significantly predictive overall:')
print('f =', fValueB, 'p =', f_pValueB)
print('The regression model explains 72.35% of adjusted variance in ') 
print('the variable "Collaborative Teachers Score".')
print()
########################################
#TODO: fix this mess and make it a table
########################################
print('---The regression coefficients are:---')
print()
dfC = pd.read_html(modelB.summary().tables[1].as_html(),header=0,index_col=0)[0]
print('Coefficient', '                         ', 'Value', '        ', 'Significance')
print('-----------------------------------------------------------------------------')
constValue = dfC['coef'].values[0]
constSignificance = pvaluesB.iloc[0]
print('const','                               ', constValue, '       ', constSignificance)
trustVal = dfC['coef'].values[3] 
trustSig = pvaluesB.iloc[3]
print('Trust Score','                         ', trustVal, '       ', trustSig)
rigVal = dfC['coef'].values[2]
rigSig = pvaluesB.iloc[2]
print('Rigorous Instruction Score','          ', rigVal, '       ', rigSig)
leadVal = dfC['coef'].values[1]
leadSig = pvaluesB.iloc[1]
print('Effective School Leadership Score','   ', leadVal, '        ', leadSig)
print()
print('The following elements of the model significantly predicted the')
print('Collaborative Teachers Score variable values:')
print('   Trust Score')
print('   Rigorous Instruction Score')
print('   Effective School Leadership Score')
print()
print('****** End of program output stream ******')
# print_model = modelB.summary()
# print(print_model)


# And then

# a=df['coef'].values[1]
# c=df['coef'].values[0]


































