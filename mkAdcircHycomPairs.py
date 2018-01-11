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
for node in range(0,77):
    OBS_file_name = '../hycom/casos/03_nodosNoInversos/TimeSeries_{}_node_nossh.txt'.format(node)
    #WRF_file_name = '../dataFiles/pronosticos/timeSeries/2017/09/TimeSeries_gom_m_09_d_06_120h_30973_node.txt'

    #OBS_file_name = '../dataFiles/observaciones/2017/fixed/12284.txt'
    #WRF_file_name = '../dataFiles/pronosticos/timeSeries/2017/08/TimeSeries_gom_m_08_d_30_120h_12284_node.txt'
        
    #OBS_file_name = cl_line[1]
    #WRF_file_name = cl_line[2]

    #Abrir los archivos
    #OBS_file = open(OBS_file_name, "r")
    #WRF_file = open(WRF_file_name, "r")
    #Y ahora lo pasamos a una lista

    serobs = pd.read_csv(OBS_file_name,parse_dates=True,index_col=0)
    #sermod = pd.read_csv(WRF_file_name,sep=',',parse_dates=True,index_col=0,header=None)
    #serobs_cut = serobs.reindex(adcirc_series.index)

    ###############TIME SERIES FOR PLOT SECTION###################################
        
    ##adcirc_series = pd.Series(adcirc_forecast, index=dates)
    #observ_series = serobs_cut.elev_obs
    #astro_series = serobs_cut.mar_astr
    #astro_original = serobs.mar_astr

    #joint_series = pd.DataFrame({'obs' : observ_series,'adc' : adcirc_series})
    #mean_series = pd.DataFrame({'obs-mean' : observ_series - observ_series.mean(),'adcirc-mean' : adcirc_series - adcirc_series.mean()})
    #mean_astro_series = pd.DataFrame({'obs-mean' : observ_series - observ_series.mean(),'adcirc-mean' : adcirc_series - adcirc_series.mean(),'astro-mean' : astro_series - astro_series.mean()})
    mag_series = pd.DataFrame({'hycom-mag' : np.linalg.norm(serobs[[ 'ua_hycom','va_hycom']],axis=1),'adcirc-mag' : np.linalg.norm(serobs[[ 'u_adcirc','v_adcirc']],axis=1)})
    vel_series = pd.DataFrame({'ua_hycom' : serobs[ 'ua_hycom'],'va_hycom' : serobs[ 'va_hycom'],'u_adcirc' : serobs[ 'u_adcirc'],'v_adcirc' : serobs[ 'v_adcirc']})
    ssh_series = pd.DataFrame({'ssh_hycom' : serobs[ 'ssh_hycom'],'zeta_adcirc' : serobs[ 'zeta_adcirc']})

    ##For some names and dates
    #t = joint_series.index[0]
    #wrf_day = t.day 
    #wrf_month = t.month
    #wrf_nam = WRF_file_name.split('_')
    #adcirc_node = int(wrf_nam[7])


    mag_series.plot(title='Series de tiempo magnitud para el nodo {}'.format(node),yticks=[0.1,0.2,0.3,0.4,0.5,0.6],ylim=[0,0.7])
    plt.ylabel('Magnitud de velocidad (m/s)')
    figstr = '../figures/hycom/mag_node_{}'.format(node)
    plt.savefig(figstr)
    
    vel_series.plot(title='Series de tiempo componentes para el nodo {}'.format(node),ylim=[-0.6,0.6])
    plt.ylabel('velocidad (m/s)')
    figstr = '../figures/hycom/uv_node_{}'.format(node)
    plt.savefig(figstr)
    
    ssh_series.plot(title='Series de tiempo elevacion para el nodo {}'.format(node),ylim=[-0.5,0.5])
    plt.ylabel('Elevacion (m)')
    figstr = '../figures/hycom/ssh_node_{}'.format(node)
    plt.savefig(figstr)

