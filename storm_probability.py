# This is a simple program takes the historical data of storms and hurricances in the state of Florida and determines the probability of a future storm. This is useful in risk management and adapation as part of resilience in the built environment as part of climate change mitigation efforts. This can also be used to determine risks in the financial industry, insurance assessments, etc.

import pandas as pd

#Read the data from the storms file
df=pd.read_csv('florida_storms.csv')

#Exploratory data analysis
df.info()

# Conert the ISO_TIME field in a new column in the dataframe to a datetime field
df['date_time'] = pd.to_datetime(df['ISO_TIME'])

# Find out the earliest storm and latest storm dates
df.date_time.describe()
#The earliest storm date recorded is in the year 1857 and the latest in #2010

#Calculate the probability of storms
import math
rate = len(df) / (2010-1857)
prob = 1-math.exp(-rate)
print(rate)
print(prob)

#We can find other storm-rates and probability like month with the highest number of storms, probability of a particular type of storm

#Finding out the month which has the highest number of storms
df['month'] = pd.DatetimeIndex(df['date_time']).month

import numpy as np

df_month = df.groupby('month').count()
df_month
df_month['rate'] = df_month['date_time'] / (2010-1857)
df_month['prob'] = 1-np.exp(-df_month['rate'])
df_month.describe()

#Finding the probability of a 'tropical' storm passing through
df_nonTS = df[df['NATURE'] != 'TS']
df_nonTS.describe()
rate_nonTS = len(df_nonTS) / (2010-1857)
prob_nonTS = 1-math.exp(-rate_nonTS)
print(rate)
print(prob)