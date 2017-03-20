
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
df3.index =range(365)
df4.index =range(365)

df3[df3>df2]=np.nan
df4[df4<df1]=np.nan
   

import matplotlib.pyplot as plt
fig_size[0] = 12
fig_size[1] = 9

# plot the linear data and the exponential data
maxV = df1['TMAX']
minV = df2['TMIN']
minV15 = df3['TMIN']
maxV15 = df4['TMAX']
maxV.columns = ['maximum 2005 - 14']
minV.columns = ['minimum 2005 - 14']
maxV15.columns = ['maximum 2015']
minV15.columns = ['minimum 2015']
minV.renames = "hej"
plt.figure()
plt.plot(maxV, '-', minV, '-')
plt.fill_between(range(365), minV, maxV, facecolor='blue', alpha=0.25)
plt.scatter(range(365), minV15)
plt.scatter(range(365), maxV15)
plt.ylabel('Temperature')
plt.xlabel('Day of the year')
plt.title('Record of high and low temperatures by day of the year')
plt.legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, shadow=True, title="Legend", fancybox=True)



