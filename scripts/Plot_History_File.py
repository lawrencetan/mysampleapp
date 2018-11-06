# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 23:01:00 2018

@author: Lawrence
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates


#ind = np.arange(5)    
#width = 0.3 
#order=[2,3,1,5,4]
#supply=[3,4,2,6,5]
#feedback=[1,1,1,1,1]
#
#p1 = plt.bar(ind, order,width, color='yellow')
#p2 = plt.bar(ind, supply, width, color='red',bottom=order)
#p3 = plt.bar(ind, feedback, width, color='green',bottom=[order[j] +supply[j] for j in range(len(order))])
#
#plt.xlabel('date')
#plt.title('time')
#plt.legend((p1[0], p2[0], p3[0]), ('order', 'supply', 'feedback'))
#
#plt.show()

#READ FROM CSV
uh_history = pd.read_csv('../work/uh_core_jobs_history.csv',parse_dates=['END TIME', 'START TIME'])
print(uh_history.dtypes)

#PARSE DATE TO GET month day year only for x-axis

uh_history.set_index('END TIME',inplace=True) #set date as index


#plot data
fig, ax = plt.subplots(figsize=(15,7))
ax.bar(uh_history.index, uh_history['count'])

#get the start time and convert to date format for plot
#core_start = uh_history[uh_history.columns[6]]
#core_end = uh_history[uh_history.columns[7]]

#x=datetime.datetime(core_start[1])
#y=datetime.strptime(core_start[1])



#convert to date time format via string parse time
#datetime_object1 = datetime.strptime('2018-04-01 00:01:06', '%Y-%m-%d %H:%M:%S')
#print(datetime_object1)
#
#for core_start in core_start:
#   
#    datetime_object3 = datetime.strptime(core_start, '%Y-%m-%d %H:%M:%S')
#
#
#print(datetime_object3)