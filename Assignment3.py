# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:13:36 2017

@author: jopa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(12345)

df = pd.DataFrame([np.random.normal(33500,150000,3650), 
                   np.random.normal(41000,90000,3650), 
                   np.random.normal(41000,120000,3650), 
                   np.random.normal(48000,55000,3650)], 
                  index=[1992,1993,1994,1995])

mean_values = df.mean(axis=1)
variance = df.var(axis=1)
error_margin = 1.96*(variance/3650)**0.5
bar_labels = ['1992', '1993', '1994', '1995']

fig = plt.gca()
# plot bars
x_pos = list(range(len(bar_labels)))
plt.bar(x_pos, mean_values, yerr=error_margin, align='center', alpha=0.5)

plt.xticks(x_pos, bar_labels)

max_y = max(zip(mean_values, error_margin)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])
# add a grid
plt.grid()
plt.ylabel('Mean')
plt.xticks(x_pos, bar_labels)
plt.title('Mean for each year')
plt.tick_params(axis="both", which="both", bottom="off", top="off",  
                labelbottom="on", left="on", right="off", labelleft="on")  
plt.show()


