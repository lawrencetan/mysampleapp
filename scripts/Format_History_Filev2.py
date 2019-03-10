# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:20:03 2019

@author: s7462669
"""


import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator

#define the fixed width spaces for the dataframe
colspecs = [(0,19),(20,25),(26,34),(64,71),(157,167)]

#define header names
header_name = ["TIME_STAMP", "EVENT", "JOB NAME", "DURATION" ,"OUTCOME"]

#set to pandas fixed width format 
uh_history = pd.read_fwf('../data/History_2018_10.log',colspecs=colspecs,skiprows=3,names = header_name)


print("ORIG DTYPES uh_history", uh_history.dtypes)

#core_jobs = ['TOUHJ010','TOUHJ050','TOUHJ011', 'TOUHJ081', 'TOUHJ029']
core_jobs = ['TOUHJ081','TOUHJ050','TOUHJ029']
#filter to event = stop only
uh_core_jobs_history = uh_history.loc[uh_history['EVENT'] == 'STOP']
#filter to core jobs only
uh_core_jobs_history = uh_core_jobs_history[uh_core_jobs_history['JOB NAME'].isin(core_jobs)]


uh_core_jobs_history['TIME_STAMP'] = pd.to_datetime(uh_core_jobs_history['TIME_STAMP'])
print("the datatype of uh_core_jobs_history['TIME_STAMP'] is now:", uh_core_jobs_history['TIME_STAMP'].dtypes)
print("ORIG DTYPES uh_core_jobs_history", uh_core_jobs_history.dtypes)

print("creating 'DATE' and 'TIME' in the dataframe")
uh_core_jobs_history['DATE']=uh_core_jobs_history['TIME_STAMP'].apply(lambda x: x.date())
uh_core_jobs_history['END_TIME']=uh_core_jobs_history['TIME_STAMP'].apply(lambda x: x.time())
print("ORIG DTYPES uh_core_jobs_history", uh_core_jobs_history.dtypes)

#Convert to DATAETIME to get date only..
#dConvert duration to have a dates
DATES = [pd.to_datetime(d) for d in uh_core_jobs_history['DATE']]
DURATION = [pd.to_datetime(d) for d in uh_core_jobs_history['DURATION']]
y = uh_core_jobs_history['TIME_STAMP'].apply(lambda x: x.replace(year=1967, month=6, day=25)).tolist()

colors = {1:'red',2:'green',3:'blue'}

ax = plt.subplot()
#set y axis to 00:00 01:00 02:00
ax.yaxis.set_major_locator(HourLocator())
#set y-axis show MM/DD/YY HH:MM
ax.yaxis.set_major_formatter(DateFormatter('%D %H:%M'))
#plt.scatter(dates,duration)

#plt.plot_date(DATES,uh_core_jobs_history['TIME_STAMP'])

#colors
plt.annotate('', xy=(DATES, y), xytext=(0, 0), color=colors , textcoords='offset points')


plt.show()