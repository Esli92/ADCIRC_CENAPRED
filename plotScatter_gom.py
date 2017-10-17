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

statnames = ['Tuxpan','Veracruz','Frontera','Campeche','Celestun','Progreso','Telchac','PtoMorelos','IslaMujeres']
stations = ['11129',  '19881',  '29907',  '40273',  '42550',  '44732',  '45878',  '73509',  '75448']
mesnams = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
x = range(len(statnames))

#intervalos = ['02','06','24','47','48','61','72','79','91','96','120']
intervalos = ['02','91']
internams = ['1 a 24 horas','97 a 120 horas']
i = 0
for intervalo in intervalos:
    j = 0
    for station in stations:
        k = 0
        for month in range(1,13):
            
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
                    
                    plt.title('Diagrama de dispersion del intervalo de {},\nestacion {} para el mes {}'.format(internams[i],statnames[j],mesnams[month-1]))
                    plt.ylabel('Pronostico de elevacion del nivel del mar (m)')
                    plt.xlabel('Observacion de elevacion del nivel del mar (m)')

                    plt.annotate('y = {:6.2f}x +{:6.2f} \nR = {:6.2f}'.format(fit[0],fit[1],corr), xy=(0.05, 0.85), xycoords='axes fraction')
                    
                    figstr = '../figures/scattergom/{}/scatterPlot_st_{}_m_{}'.format(intervalo,station,month)
                    plt.savefig(figstr)
                    plt.clf()
            k = k + 1
        j = j + 1
    i = i + 1
