# Importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
sns.set(color_codes=True)

CurrentDirectory = os.getcwd()
filepath = CurrentDirectory + '\\ninja_europe_wind_v1.1\\ninja_wind_europe_v1.1_future_longterm_national.csv'
df = pd.read_csv(filepath)

# Explore dataframe 
print(df.head(5))
#print(df.tail(5))
print(df.dtypes)
#print(df.shape)clear
#print(df.count())
#print(df.info())
print(df.describe())

# Finding the null values.
#print(df.isnull().sum())

# Indexing by time
df['time'] = pd.to_datetime(df['time'])
df.set_index('time',inplace=True)

print(df.head(5))
print(df.dtypes)

#subset=df['2015-01-01 00:00:00':'2015-02-01 00:00:00']
subset=df['2010':'2015']
print(subset.head(5))
print(subset.head(5))
subset=subset[['PT','ES','FR','DE']]
print(subset.head(5))
monthlydata=subset.resample('W').mean()

# Lineplot
sns.lineplot(data=monthlydata,palette="tab10", linewidth=2.5)
#plt.show()

# Scatterplot Matrix
sns.pairplot(monthlydata)
#plt.show()

# Linear regression with marginal distributions
sns.jointplot('ES', 'FR', data=monthlydata, kind="reg", xlim=(0, 1), ylim=(0, 1), color="m", height=7)
plt.show()

exit()
# Heat Maps
c= monthlydata.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
plt.show()

# Boxplots
sns.boxplot(x=df['ES'])
plt.show()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
print(IQR)
# Remove outliers
#df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=2)]

# Heat Maps
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
plt.show()

# Scatterplot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['ES'], df['FR'])
ax.set_xlabel('ES')
ax.set_ylabel('FR')
plt.show()
