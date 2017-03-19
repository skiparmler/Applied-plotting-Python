
import numpy as np    
import pandas as pd
data = pd.read_csv('c:/tmp/ass2/data.txt')
del data['ID']

df = data.pivot(index='Date', columns='Element', values='Data_Value')

df.index= pd.to_datetime(df.index)
idx = pd.date_range(df.index.min(), df.index.max())
df = df.reindex(idx, fill_value="")

#df = df[~((df.index.month == 2) & (df.index.day == 29))]
#df = df[~df.index.str.endswith('02-29')]
#df=df.replace(r'\s+', np.nan, regex=True)

df=df.replace(r'\s+',np.nan,regex=True).replace('',np.nan)






dff=df['2005':'2014'] #730 rows
dfff=df['2012']
df_overlay = df['2015']
df1= dff.groupby([dff.index.dayofyear, dff.index.hour]).max()
df2= dff.groupby([dff.index.dayofyear, dff.index.hour]).min()
df3= df_overlay.groupby([df_overlay.index.dayofyear, df_overlay.index.hour]).min()
df4= df_overlay.groupby([df_overlay.index.dayofyear, df_overlay.index.hour]).max()

df1 = df1.drop(df1.index[[59]])
df2 = df2.drop(df2.index[[59]])
df1.index =range(365)
df2.index =range(365)



import matplotlib.pyplot as plt
plt.figure()
# plot the linear data and the exponential data
maxV = df1['TMAX']
minV = df2['TMIN']
minV15 = df3['TMIN']
maxV15 = df4['TMAX']
plt.plot(maxV, '-', minV, '-')
plt.fill_between(range(365), minV, maxV, facecolor='blue', alpha=0.25)
plt.scatter(range(365), minV15)
plt.scatter(range(365), maxV15)
