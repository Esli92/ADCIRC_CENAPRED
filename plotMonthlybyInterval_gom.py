#mkVerifStatFiles_contData.sh
#Program that takes output of R scripts for verification, and creates a file for each station with its statistic values for each MES (like MAE,ME,MSE). 
#Programmer Oscar Jurado (ojurado@ciencias.unam.mx)
#Creation date: 25-Feb-2017

#------------------Requisites------------------------------------------------------------
#Results from verification tests with continuous data
#verify_monthly directory

#-----------------Version---------------------------------------------------------------
#v1.0 25/Feb/17 Program is created


#----------------Known issues-----------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#---------------BEGIN PROGRAM-----------------------------------------------------------

#statnames = ['Aransas Pass','Port O Connor','Matagorda Bay','Sargent','Galveston Bay Entrance','Texas Point','Freshwater Canal','Calcasieau Pass','Bob Hall Pier','Packery Channel','SPI Brazos Santiago','South Padre Island','Port Isabel']
#stations = ['15178','18564','18931','21845','24375','26875','30973','28186','12594','12284','13801','13694','13646']
statnames = ['Aransas Pass','Matagorda Bay','Galveston Bay Entrance','Bob Hall Pier','SPI Brazos Santiago','South Padre Island','Port Isabel']
stations = ['15178','18931','24375','12594','13801','13694','13646']
#statnames = ['Galveston Bay Entrance']
#stations = ['24375']
internams = ['1 a 24','25 a 48','49 a 72','73 a 96', '97 a 120']
#internams = ['1 a 24','97 a 120']
#mesnams = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
mesnams = ['Harvey']
#stations = ['17522']
meses=[8]
lon = [-97.034,-96.31,-94.718,-97.216,-97.150,-97.166,-97.202]
lat = [27.833,28.41,29.351,27.568,26.066,26.067,26.051]

matplotlib.rcParams.update({'font.size': 12})

styles=['g-','b-']
linewidths=[2,1]
i = 0
j = 0
k = 0
oin = True
intervalos = ['02','24','47','79','91']
#intervalos = ['02','91']

file_str = "../dataFiles/sig/maximos.csv"
maxfile = open(file_str, 'w')
maxfile.write("lat,lon,station,obs,1-24,25-48,49-72,73-96,97-120")
maxfile.write("\n")

for station in stations:
    oin = True
    i = 0
    futstr = '{},{},{}'.format(lat[j],lon[j],statnames[j])
    for intervalo in intervalos:
        k = 0
        for month in meses:
            
            serfile='../dataFiles/pares/{}/monthlyPairs/gom/{}_m{}.txt'.format(intervalo,station,month)
            sertest = pd.read_csv(serfile,sep=',')
            sertest['datecol'] = '2017-'+sertest['MES'].astype(str) + '-' + sertest['DIA'].astype(str) + '-' + sertest['HORA'].astype(str)
            sertest['datecol'] = pd.to_datetime(sertest['datecol'],format='%Y-%m-%d-%H')
            sertest = sertest.set_index(sertest['datecol'])
            newser = pd.DataFrame({'observación' : sertest['OBSERVACION'],'modelo' : sertest['PRONOSTICO']})
            obs_max = newser['observación'].max()
            int_max = newser['modelo'].max()
            if oin:
                futstr += ',{}'.format(obs_max)
                oin = False

            futstr += ',{}'.format(int_max)
                

            fig, ax = plt.subplots(figsize=(7, 4))
            
            for col, style, lw in zip(newser.columns, styles, linewidths):
                newser[col].plot(style=style, lw=lw, ax=ax)
                
            plt.legend(loc='upper right')
            plt.title('Serie reconstruida con intervalo de {} horas, \n estación {}, evento {}.'.format(internams[i],statnames[j],mesnams[k]))
            plt.ylabel('Elevación del nivel del mar')
            plt.xlabel('Tiempo')
            plt.ylim(-0.6,1)
            figstr = '../figures/reconstex/rec_st_{}_int_{}_m{}'.format(station,intervalo,month)
            plt.savefig(figstr)
            plt.clf()
            
            
            k = k + 1
            
        
        i = i +1
        
    maxfile.write(futstr)
    maxfile.write("\n")
    j = j + 1
        
