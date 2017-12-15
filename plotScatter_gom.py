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
import matplotlib.pyplot as plt

#---------------BEGIN PROGRAM-----------------------------------------------------------

#statnames = ['Acpco','PtAng','Htlco','PtChs','LzCar','Zihua','SalCr','Mztln','PtVal']

statnames = ['Aransas Pass','Port O Connor','Matagorda Bay','Sargent','Galveston Bay Entrance','Texas Point','Freshwater Canal','Calcasieau Pass','Bob Hall Pier','Packery Channel','SPI Brazos Santiago','South Padre Island','Port Isabel']
stations = [15178,18931,24375,12594,13801,13694,13646]
mesnams = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Harvey','Septiembre','Octubre','Noviembre','Diciembre']
x = range(len(statnames))

#intervalos = ['02','06','24','47','48','61','72','79','91','96','120']
intervalos = ['02','24','47','79','91']
internams = ['1 a 24','25 a 48','49 a 72','73 a 96', '97 a 120']

meses = [8]
i = 0
for intervalo in intervalos:
    j = 0
    for station in stations:
        k = 0
        for month in meses:
            
            serfile='../dataFiles/pares/{}/monthlyPairs/gom/{}_m{}.txt'.format(intervalo,station,month)
            sertest = pd.read_csv(serfile,sep=',')
            
            if sertest['OBSERVACION'].isnull().all():
                continue
            else:
                sertest = sertest.dropna()
                if len(sertest) > 1:
                    plt.scatter(sertest['OBSERVACION'],sertest['PRONOSTICO'],s=10)
                    minx = sertest['OBSERVACION'].min()
                    maxx = sertest['OBSERVACION'].max()
                    miny = sertest['PRONOSTICO'].min()
                    maxy = sertest['PRONOSTICO'].max()
                    plt.plot(sertest['OBSERVACION'],sertest['OBSERVACION'],'k-')
                    fit = np.polyfit(sertest['OBSERVACION'], sertest['PRONOSTICO'], deg=1)
                    plt.plot(sertest['OBSERVACION'], fit[0] * sertest['OBSERVACION'] + fit[1], color='red')
                    corr = sertest['OBSERVACION'].corr(sertest['PRONOSTICO'])
                    
                    plt.title('Diagrama de dispersion del intervalo de {} horas,\nestacion {} para el evento {}'.format(internams[i],statnames[j],mesnams[month-1]))
                    plt.ylabel('Pronostico de elevacion del nivel del mar (m)')
                    plt.xlabel('Observacion de elevacion del nivel del mar (m)')

                    plt.annotate('y = {:6.2f}x +{:6.2f} \nR = {:6.2f}'.format(fit[0],fit[1],corr), xy=(0.05, 0.85), xycoords='axes fraction')
                    
                    figstr = '../figures/scattertex/{}/scatterPlot_st_{}_m_{}'.format(intervalo,station,month)
                    plt.savefig(figstr)
                    plt.clf()
            k = k + 1
        j = j + 1
    i = i + 1
