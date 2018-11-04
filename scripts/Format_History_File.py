###########################################
# FORMAT DATA
#
#
#
# L.TAN
###########################################

import pandas as pd

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


#Write output for next job
uh_core_jobs_history.to_csv('../work/uh_core_jobs_history.csv')