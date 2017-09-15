
#Comenzamos cargando la libreria sys, csv, numpy
import sys
import csv
import numpy as np
from datetime import datetime
import pandas as pd
#-----------ABRIR ARCHIVO----------------------------------
#leemos el archivo

cl_line = sys.argv

#Lineas usadas en el debug 
OBS_file_name = 'acapulco_obs.txt'
FOR_file_name = 'acapulco_marpron.txt'

#OBS_file_name = cl_line[1]
#WRF_file_name = cl_line[2]

#Abrir los archivos
OBS_file = open(OBS_file_name, "r")
FOR_file = open(FOR_file_name, "r")
#Y ahora lo pasamos a una lista
obs_lines = OBS_file.readlines()
for_lines = FOR_file.readlines()

#Cerramos el archivo ya que no lo necesitamos
OBS_file.close()
FOR_file.close()

######################OBSERVATION SECTION#####################################################

#Make two empty lists to add info later
obs_list = []
date_list = []

#From this loop we get two lists, one containing all the info from the obs file in a list with floats, and one with the dates as a string for the time series
for line in obs_lines:
	obs_lines_split = [x.strip() for x in line.split(' ')]
	obs_lines_split = [float(i) for i in obs_lines_split]
	obs_list.append(obs_lines_split)
	date = '{}/{}/{} {}:{}'.format(int(obs_lines_split[0]),int(obs_lines_split[1]),int(obs_lines_split[2]),int(obs_lines_split[3]),int(obs_lines_split[4])) 
	date_list.append(date)
    
#Extract only the relevant elevation data, on column number 6 from the observation file.    
elev = [obs_list[i][6] for i in range(len(obs_list))]
#Using the time string from before, create Timestamp objects to be used in the time series object. Note that this object does not need to have a consistent
#frequency on the dates (dates can have missing values).
dates = pd.to_datetime(date_list)

#Create the first time series object, allowing it to have missing values ("holes" in the data).
elev_series_original = pd.Series(elev, index=dates)

#############OBSERVATION DATE SECTION####################
#This section fixes the missing data issue, first filling the time series with nan's where there should be a value, and then using a forward value to fill the missing values.

#First create a date range with the desired frequency (this will have NO holes in it).
start_date = datetime(2015,1,1,0,0,0)
end_date = datetime(2015,12,31,23,0,0)
dates_full = pd.date_range(start_date,end_date,freq='H')

#Now "resample" the time series so it has the same lenght as the previously made date range list. 
elev_series = elev_series_original.reindex(dates_full)

#This section is optional, only to find out how many nan values there are in the time series. 
test = pd.isnull(elev_series)
indx = 0
for i in test:
    if i:
        indx = indx +  1

#This section fills the nan values with the closest existing value backwards. (Or as it's called, the forward method).
elev_series = elev_series.fillna(method='pad')


######################FORECAST SECTION#####################################################

#Make two empty lists to add info later
for_list = []
date_list = []

#From this loop we get two lists, one containing all the info from the for file in a list with floats, and one with the dates as a string for the time series
for line in for_lines:
	for_lines_split = [x.strip() for x in line.split(' ')]
	for_lines_split = [float(i) for i in for_lines_split]
	for_list.append(for_lines_split)
	date = '{}/{}/{} {}:{}'.format(int(for_lines_split[0]),int(for_lines_split[1]),int(for_lines_split[2]),int(for_lines_split[3]),int(for_lines_split[4])) 
	date_list.append(date)
    
#Extract only the relevant elevation data, on column number 6 from the forervation file.    
elevfor = [for_list[i][6] for i in range(len(for_list))]
#Using the time string from before, create Timestamp objects to be used in the time series object. Note that this object does not need to have a consistent
#frequency on the dates (dates can have missing values).
dates = pd.to_datetime(date_list)

#Create the first time series object, allowing it to have missing values ("holes" in the data).
fore_series_original = pd.Series(elevfor, index=dates)

#############FORECAST DATE SECTION####################
#This section fixes the missing data issue, first filling the time series with nan's where there should be a value, and then using a forward value to fill the missing values.

#First create a date range with the desired frequency (this will have NO holes in it).
start_date = datetime(2015,1,1,0,0,0)
end_date = datetime(2015,12,31,23,0,0)
dates_full = pd.date_range(start_date,end_date,freq='H')

#Now "resample" the time series so it has the same lenght as the previously made date range list. 
fore_series = fore_series_original.reindex(dates_full)

#This section is optional, only to find out how many nan values there are in the time series. 
test = pd.isnull(fore_series)
indx2 = 0
for i in test:
    if i:
        indx2 = indx2 +  1

#This section fills the nan values with the closest existing value backwards. (Or as it's called, the forward method).
fore_series = fore_series.fillna(method='pad')
