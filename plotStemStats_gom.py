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

statnames = ['Txpan','Vercz','Frnt','Progs','Telch','PtoMo','IsMuj']
mesnams = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
x = range(len(statnames))

intervalos = ['02','91']
internams = ['1 a 24 horas','97 a 120 horas']
i = 0
for intervalo in intervalos:

    for month in range(1,13):
        
        serfile='verify_monthly/{}/stats/gom/ioa_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['IOA'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de IOA del intervalo {} para el mes {}'.format(internams[i],mesnams[month-1]))
        plt.ylabel('IOA')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stemgom/{}/ioa/stemplot_ioa_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/gom/bias_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['BIAS'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor del sesgo (BIAS) del intervalo {} para el mes {}'.format(internams[i],mesnams[month-1]))
        plt.ylabel('BIAS (m)')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stemgom/{}/bias/stemplot_bias_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/gom/corr_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['Pearson'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor del coeficiente de correlacion \ndel intervalo {} para el mes {}'.format(internams[i],mesnams[month-1]))
        plt.ylabel('Coeficiente de correlacion de Pearson')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stemgom/{}/corr/stemplot_corr_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
        
        serfile='verify_monthly/{}/stats/gom/rmse_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['RMSE'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de RMSE del intervalo {} para el mes {}'.format(internams[i],mesnams[month-1]))
        plt.ylabel('RMSE (m)')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stemgom/{}/rmse/stemplot_rmse_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()

        serfile='verify_monthly/{}/stats/gom/rmsedb_m_{}.txt'.format(intervalo,month)
        sertest = pd.read_csv(serfile,sep=',')
        
        plt.stem(x,sertest['RMSEdb'])
        plt.xticks(x,statnames)
        plt.xticks(rotation=90)
        
        plt.title('Valor de RMSEdb del intervalo {} para el mes {}'.format(internams[i],mesnams[month-1]))
        plt.ylabel('RMSEdb (m)')
        plt.xlabel('Estacion')
        
        figstr = '../figures/stemgom/{}/rmsedb/stemplot_rmsedb_m{}'.format(intervalo,month)
        plt.savefig(figstr)
        plt.clf()
    i = i + 1
