#Day 3 Assignment

import numpy as np
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt
import seaborn as sns

fmri=sns.load_dataset('fmri')
#print(fmri)

sns.relplot(x='subject',y='signal',data=fmri) #Scatter-Plot
plt.show()

sns.relplot(x='timepoint',y='signal',data=fmri,style='region',hue='event') #Scatter-Plot with 2 different spec"
plt.show()

sns.relplot(x='subject',y='signal',data=fmri,kind='line') #Line-Plot 
plt.show()

sns.relplot(x='subject',y='signal',data=fmri,kind='line',hue='event',style='region') #Line-Plot with 2 different spec"
plt.show()

sns.catplot(x='subject',y='signal',data=fmri,kind='box',hue='region') #Box-Plot with 'region' spec"
plt.show()