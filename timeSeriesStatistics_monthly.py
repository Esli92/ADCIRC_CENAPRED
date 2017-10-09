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

intervalos = ['02','06','24','47','48','61','72','79','91','96','120']
for intervalo in intervalos:

    for mes in range(1,13):
        
        bias_file_str = "verify_monthly/{}/stats/bias_m_{}.txt".format(intervalo,mes)
        bias_file = open(bias_file_str, 'w')
        bias_file.write("station,BIAS")
        bias_file.write("\n")
        
        rmse_file_str = "verify_monthly/{}/stats/rmse_m_{}.txt".format(intervalo,mes)
        rmse_file = open(rmse_file_str, 'w')
        rmse_file.write("station,RMSE")
        rmse_file.write("\n")
        
        rmsedb_file_str = "verify_monthly/{}/stats/rmsedb_m_{}.txt".format(intervalo,mes)
        rmsedb_file = open(rmsedb_file_str, 'w')
        rmsedb_file.write("station,RMSEdb")
        rmsedb_file.write("\n")
        
        corr_file_str = "verify_monthly/{}/stats/corr_m_{}.txt".format(intervalo,mes)
        corr_file = open(corr_file_str, 'w')
        corr_file.write("station,Pearson")
        corr_file.write("\n")
        
        ioa_file_str = "verify_monthly/{}/stats/ioa_m_{}.txt".format(intervalo,mes)
        ioa_file = open(ioa_file_str, 'w')
        ioa_file.write("station,IOA")
        ioa_file.write("\n")
        
        for station in [17522,17615,17624,18734,19545,19564,21037,23758,24780]:

            tsfile='../dataFiles/pares/{}/monthlyPairs/{}_m{}.txt'.format(intervalo,station,mes)

            df = pd.read_csv(tsfile,sep=',',parse_dates=[[0,1,2]])

            df.columns=['date','modelo','observacion']

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

            bias_file.write("{}, {}".format(station,bias))
            bias_file.write("\n")
            
            rmse_file.write("{}, {}".format(station,rmse))
            rmse_file.write("\n")
            
            rmsedb_file.write("{}, {}".format(station,rmse_db))
            rmsedb_file.write("\n")
            
            corr_file.write("{}, {}".format(station,r_pears))
            corr_file.write("\n")
            
            ioa_file.write("{}, {}".format(station,IOA))
            ioa_file.write("\n")
            
        bias_file.close()
        rmse_file.close()
        rmsedb_file.close()
        corr_file.close()
        ioa_file.close()

