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
statnames = ['Acpco','PtAng','Htlco','LzCar','SalCr','Mztln','PtVal']
x = range(len(statnames))

#intervalos = ['02','06','24','47','48','61','72','79','91','96','120']
intervalos = ['02','91']
internams = ['1 a 24 horas','97 a 120 horas']
i = 0
for intervalo in intervalos:

    for month in range(1,13):
        
        serfile='verify_monthly/{}/stats/pom/ioa_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['IOA'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de IOA del intervalo {} para el mes {}'.format(internams[i],month))
        plt.ylabel('IOA')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stem/{}/ioa/stemplot_ioa_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/pom/bias_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['BIAS'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor del sesgo (BIAS) del intervalo {} para el mes {}'.format(internams[i],month))
        plt.ylabel('BIAS (m)')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stem/{}/bias/stemplot_bias_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/pom/corr_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['Pearson'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor del coeficiente de correlacion del intervalo {} para el mes {}'.format(internams[i],month))
        plt.ylabel('Coeficiente de correlacion de Pearson')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stem/{}/corr/stemplot_corr_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/pom/rmse_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['RMSE'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de RMSE del intervalo {} para el mes {}'.format(internams[i],month))
        plt.ylabel('RMSE (m) ')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stem/{}/rmse/stemplot_rmse_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()

        serfile='verify_monthly/{}/stats/pom/rmsedb_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['RMSEdb'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de RMSEdb del intervalo {} para el mes {}'.format(internams[i],month))
        plt.ylabel('RMSEdb (m)')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stem/{}/rmsedb/stemplot_rmsedb_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
    i = i + 1 
