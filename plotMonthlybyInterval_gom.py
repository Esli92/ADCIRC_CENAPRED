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

statnames = ['Tuxpan','Veracruz','Frontera','Campeche','Celestun','Progreso','Telchac','PtoMorelos','IslaMujeres']
stations = ['11129',  '19881',  '29907',  '40273',  '42550',  '44732',  '45878',  '73509',  '75448']
#internams = ['1 a 24','25 a 48','49 a 72','73 a 96', '97 a 120']
internams = ['1 a 24','97 a 120']
mesnams = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
#stations = ['17522']



matplotlib.rcParams.update({'font.size': 12})

styles=['g-','b-']
linewidths=[2,1]
i = 0
j = 0
k = 0
#intervalos = ['02','24','47','79','91']
intervalos = ['02','91']
for intervalo in intervalos:
    i = 0
    for station in stations:
        k = 0
        for month in range(1,13):
            
            serfile='../dataFiles/pares/{}/monthlyPairs/gom/{}_m{}.txt'.format(intervalo,station,month)
            sertest = pd.read_csv(serfile,sep=',')
            sertest['datecol'] = '2015-'+sertest['MES'].astype(str) + '-' + sertest['DIA'].astype(str) + '-' + sertest['HORA'].astype(str)
            sertest['datecol'] = pd.to_datetime(sertest['datecol'],format='%Y-%m-%d-%H')
            sertest = sertest.set_index(sertest['datecol'])
            newser = pd.DataFrame({'observación' : sertest['OBSERVACION'],'modelo' : sertest['PRONOSTICO']})
            fig, ax = plt.subplots(figsize=(7, 4))
            for col, style, lw in zip(newser.columns, styles, linewidths):
                newser[col].plot(style=style, lw=lw, ax=ax)
            
            #myFmt = mdates.DateFormatter('%d')
            #ax.xaxis.set_major_formatter(myFmt)
            plt.legend(loc='upper left')
            plt.title('Serie reconstruida con intervalo de {} horas, \n estación {}, mes {}, año 2015'.format(internams[j],statnames[i],mesnams[k]))
            plt.ylabel('Elevación del nivel del mar')
            plt.xlabel('Tiempo')
            
            figstr = '../figures/reconsgom/rec_st_{}_int_{}_m{}'.format(statnames[i],intervalo,month)
            plt.savefig(figstr)
            plt.clf()
            k = k + 1
        i = i +1
    j = j + 1
        
