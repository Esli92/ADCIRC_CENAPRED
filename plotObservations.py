
#Comenzamos cargando la libreria sys, csv, numpy
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
#-----------ABRIR ARCHIVO----------------------------------
#leemos el archivo

cl_line = sys.argv

#Lineas usadas en el debug 
OBS_file_name = 'acapulco_obs.txt'
	
#OBS_file_name = cl_line[1]
#WRF_file_name = cl_line[2]

#Abrir los archivos
OBS_file = open(OBS_file_name, "r")

#Y ahora lo pasamos a una lista
obs_lines = OBS_file.readlines()


#Cerramos el archivo ya que no lo necesitamos
OBS_file.close()


obs_list = []
for line in obs_lines:
	obs_lines_split = [x.strip() for x in line.split(' ')]
	date = obs_lines_split[0].split('-')
	obs_lines_split = obs_lines_split[1:len(obs_lines_split)]
	[obs_lines_split.insert(0,i) for i in reversed(date)]
	obs_lines_split = [float(i) for i in obs_lines_split]
	obs_list.append(obs_lines_split)

elev = [obs_list[i][6] for i in range(len(obs_list))]

plt.plot(elev)
plt.xlabel('Time')
plt.ylabel('Sea level elevation (m)')
plt.title('Acapulco station 2015')
plt.show()
