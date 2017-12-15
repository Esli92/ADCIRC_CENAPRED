#mkObsFrcstPair.py
#Programa que toma datos procesados de estaciones mareograficas y series de tiempo de ADCIRC y genera un archivo de pares observacion-pronostico para ser usado en la verificacion 
#Programador Oscar Jurado
#Fecha de creacion 5 de Julio 2016
#Modificado para uso en ADCIRC en Septiembre 2017

#-------------Requisitos--------------------------------------------------------------
#Para correr el programa se necesita tener la utilidad de python xlrd,csv,numpy instalados. 
#Los datos de entrada deben provenir de archivos procesados con programa leerEma.py, leerRedmet.py y mkTimeSeriesWRF.sh 
#Formato de archivos de tal manera que exista ../dataFiles/pairs

#-------------Uso---------------------------------------------------------------------
#El programa se corre desde la terminal, poniendo el nombre de los archivos como entrada en este orden: 1)Archivo de estacion 2)Archivo WRF
#Ejemplo:
#python mkObsFrcstPair.py ACO_TM.txt CCA_27_TEMP.txt
#Se recomienda usar en conjunto con la utileria 

#------------Versiones----------------------------------------------------------------
#v1.0 5/Jul/2016 Se crea el programa. 


#-----------Problemas conocidos--------------------------------------------------------
#b01 -- El programa requiere que el archivo de inicio wrf tenga un nombre muy particular, el cual creo que aun no esta automatizado

#----------INICIO DEL PROGRAMA--------------------------------------------------------

#Comenzamos cargando la libreria sys, csv, numpy
import sys
import csv
import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from shutil import copyfile

#-----------ABRIR ARCHIVO----------------------------------
#leemos el archivo

#cl_line = sys.argv

#Lineas usadas en el debug 
OBS_file_name = '../dataFiles/observaciones/2017/fixed/30973.txt'
WRF_file_name = '../dataFiles/pronosticos/timeSeries/2017/09/TimeSeries_gom_m_09_d_06_120h_30973_node.txt'

#OBS_file_name = '../dataFiles/observaciones/2017/fixed/12284.txt'
#WRF_file_name = '../dataFiles/pronosticos/timeSeries/2017/08/TimeSeries_gom_m_08_d_30_120h_12284_node.txt'
	
#OBS_file_name = cl_line[1]
#WRF_file_name = cl_line[2]

#Abrir los archivos
OBS_file = open(OBS_file_name, "r")
WRF_file = open(WRF_file_name, "r")
#Y ahora lo pasamos a una lista

serobs = pd.read_csv(OBS_file_name,parse_dates=True,index_col=0)
sermod = pd.read_csv(WRF_file_name,sep=',',parse_dates=True,index_col=0,header=None)
adcirc_series=sermod.iloc[:,0]
serobs_cut = serobs.reindex(adcirc_series.index)

##############TIME SERIES FOR PLOT SECTION###################################
    
#adcirc_series = pd.Series(adcirc_forecast, index=dates)
observ_series = serobs_cut.elev_obs
astro_series = serobs_cut.mar_astr
astro_original = serobs.mar_astr

joint_series = pd.DataFrame({'obs' : observ_series,'adc' : adcirc_series})
#mean_series = pd.DataFrame({'obs-mean' : observ_series - observ_series.mean(),'adcirc-mean' : adcirc_series - adcirc_series.mean()})
#mean_astro_series = pd.DataFrame({'obs-mean' : observ_series - observ_series.mean(),'adcirc-mean' : adcirc_series - adcirc_series.mean(),'astro-mean' : astro_series - astro_series.mean()})
mean_series = pd.DataFrame({'obs-mean' : observ_series - astro_original.mean(),'adcirc-mean' : adcirc_series})
mean_astro_series = pd.DataFrame({'obs-mean' : observ_series - astro_original.mean(),'adcirc' : adcirc_series,'astro-mean' : astro_series - astro_original.mean()})

#For some names and dates
t = joint_series.index[0]
wrf_day = t.day 
wrf_month = t.month
wrf_nam = WRF_file_name.split('_')
adcirc_node = int(wrf_nam[7])


mean_astro_series.plot(title='Series de tiempo estacion FreshwaterCanal')
plt.ylabel('Elevacion (m)')
figstr = '../figures/astro_tx/ts_plot_d_{}_m_{}_st_FreshwaterCanal.png'.format(wrf_day,wrf_month)
plt.savefig(figstr)
# 
# ############GET different pairs (24h, 48h, 120h, l24h, l48h, etc).
oi = 0
opts = ['02','24','47','79','91']
for i in range(0,120,24):
    cut_series = mean_series[i:i+24]
    namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format(opts[oi],adcirc_node,wrf_day+10,wrf_month,opts[oi])
    oi = oi + 1
    copyfile('pairHead',namestr)
    cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')

#oi = 0
#opts = ['06','61']
#for i in range(0,120,60):
    #cut_series = mean_series[i:i+60]
    #namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format(opts[oi],adcirc_node,wrf_day+10,wrf_month,opts[oi])
    #oi = oi + 1
    #copyfile('pairHead',namestr)
    #cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')
    
#cut_series = mean_series[0:48]
#namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format('48',adcirc_node,wrf_day+10,wrf_month,'48')
#copyfile('pairHead',namestr)
#cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')

#cut_series = mean_series[96:120]
#namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format('96',adcirc_node,wrf_day+10,wrf_month,'96')
#copyfile('pairHead',namestr)
#cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')


#cut_series = mean_series[72:120]
#namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format('72',adcirc_node,wrf_day+10,wrf_month,'72')
#copyfile('pairHead',namestr)
#cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')

#cut_series = mean_series
#namestr = "../dataFiles/pares/{}/ObsFct_Pairs_{}_{}_{}_e_{}_15.txt".format('120',adcirc_node,wrf_day+10,wrf_month,'120')
#copyfile('pairHead',namestr)
#cut_series.to_csv(namestr,sep=',',na_rep='nan',date_format='%m,%d,%H',header=False,quotechar=' ',mode='a')
