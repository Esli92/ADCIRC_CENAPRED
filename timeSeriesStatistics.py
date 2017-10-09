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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loop the 120 hours



for mes in range(1,13):
    
    date_file_str = "verif_hourly/bias/bias_st_17624_m_{}.txt".format(mes)
    date_file = open(date_file_str, 'w')
    date_file.write("mes,hora,BIAS")
    date_file.write("\n")
    
    for hour in range(1,120):

        tsfile='../dataFiles/pares/horarios/m{}/ObsFct_Pairs_st_17624_h{}_m{}.txt'.format(mes,hour,mes)

        df = pd.read_csv(tsfile,sep=',',parse_dates=[[0,1,2]],index_col=0,header=None)

        df.columns=['modelo','observacion']

        r_pears = df['modelo'].corr(df['observacion'])
        df['mod-obs'] = df['modelo'] - df['observacion']
        df['sq(mod-obs)'] = df['mod-obs']**2
        bias = df['mod-obs'].mean()
        rmse = df['sq(mod-obs)'].mean()
        df['mod-obs-bias'] = (df['mod-obs'] - bias)**2
        rmse_db = df['mod-obs-bias'].mean()

        #for IOA
        obs_mean = df['observacion'].mean()
        df['obs-mean'] = df['observacion']-df['observacion'].mean()
        sum_obs_mean = abs(sum(df['obs-mean'])) 
        sum_mod_obs = abs(sum(df['mod-obs']))
        c = 2

        if sum_mod_obs <= (c * sum_obs_mean):
            IOA = 1 - (sum_mod_obs/(c*sum_obs_mean))
        else:
            IOA = ((c*sum_obs_mean)/sum_mod_obs) - 1
        
        date_file.write("{}, {}, {}".format(mes,hour,bias))
        date_file.write("\n")
        
    date_file.close()


