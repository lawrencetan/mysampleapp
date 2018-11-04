###########################################
# FORMAT DATA
#
#
#
#
###########################################


import pandas as pd
from pathlib import Path
#import plotly as py
#import plotly.figure_factory as ff

from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import *
import plotly.figure_factory as ff

#test
#import numpy as np

#job_number="LAW010"
#init_notebook_mode(connected=True)  # initiate notebook for offline plot
workpath = Path("../work")

#define the fixed width spaces for the dataframe
colspecs = [(0,19),(20,25),(26,34),(64,71),(157,167)]

#define header names
header_name = ["TIME", "EVENT", "JOB NAME", "DURATION" ,"OUTCOME"]

#set to pandas fixed width format 
uh_history = pd.read_fwf('../data/History_2018_04.log',colspecs=colspecs,skiprows=3,names = header_name)

#convert Time column into datetime data type
uh_history['TIME'] = pd.to_datetime(uh_history.TIME)
uh_history['DURATION'] = pd.to_timedelta(uh_history.DURATION)

#define all core jobs
core_jobs = ['TOUHJ010','TOUHJ050','TOUHJ011','TOUHJ028', 'TOUHJ081', 'TOUHJ029']

#filter to event = stop only
uh_core_jobs_history = uh_history.loc[uh_history['EVENT'] == 'STOP']
#filter to core jobs only
uh_core_jobs_history = uh_core_jobs_history[uh_core_jobs_history['JOB NAME'].isin(core_jobs)]



#SUBTRACT DURATION FROM END TIME
uh_core_jobs_history['START TIME'] = uh_core_jobs_history['TIME'] - uh_core_jobs_history['DURATION']
uh_core_jobs_history['END TIME'] = uh_history['TIME']

#uh_history.close()

uh_core_jobs_history.to_csv('../work/uh_core_jobs_history.csv')

#print(uh_core_jobs_history)


#remove duplicate rows
#uh_core_jobs_history = uh_core_jobs_history.drop_duplicates()


#pivot table to show start and end time
#for each job name; start time = event is start 

#for start_job in uh_core_jobs_history:
#    uh_core_jobs_history['JOB NAME','EVENT'] is jobname, start
#    where uh_core_jobs_history['EVENT'] is start
#    start_job = 
    

#uh_core_jobs_history_test=uh_core_jobs_history.set_index(['JOB NAME', 'EVENT'], drop=False)



#uh_core_start_end=uh_core_jobs_history.groupby('JOB NAME').agg(nth())
#uh_core_jobs_history_test = uh_core_jobs_history.head(14).pivot(index="JOB NAME",columns= "EVENT").reset_index(drop=False,inplace=True)
#print (uh_core_jobs_history)


#uh_core_jobs_history = uh_core_jobs_history.pivot_table(index='JOB NAME',
#                     columns='EVENT',
#                     aggfunc=np.count_nonzero).reset_index().fillna(0).astype(int)


#uh_core_start_end = uh_core_jobs_history_test.pivot(index="JOB NAME",columns= "EVENT")




#uh_core_start_end = uh_core_jobs_history.unstack()
#print(uh_core_jobs_history_test)


#print(np.where(uh_core_start_end.index.duplicated()))

#   
#uh_plot = pd.concat([uh_core_jobs_history['JOB NAME'],uh_core_jobs_history['START TIME'],uh_core_jobs_history['END TIME']],axis=1, keys=['Task', 'Start', 'Finish'])
##
#fig = ff.create_gantt(uh_plot,index_col='Resource', title='UH CORE JOBS',
#                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
#*.plot(fig,filename = 'my-uh-gantt')
##py.offline.iplot(fig, filename='temp-plot.html', auto_open=True,
##                    image_width=1280, image_height=800,
##                    image_filename='fname', image='svg', save_img=True)
#
#
#






#uh_core_jobs_history = uh_history({'Job Name': core_jobs})

#uh_core_jobs_history = uh_history[(uh_history.values  == "TOUHJ010")|(uh_history.values  == "TOUHJ050" ) ]
#do a loop for each job
#for core_jobs in core_jobs:
#    uh_core_jobs_history = uh_history[uh_history['JOB NAME'].str.contains(core_jobs)]





#print (uh_history)
#print (uh_history.dtypes)
#to get the julian date of the time the job run
#uh_history.TIME.dt.dayofyear




