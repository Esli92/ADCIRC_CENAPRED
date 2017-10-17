#!/bin/bash

#bulkPairsPlots.sh 
#Programa para generar pares obs/pron de series de tiempo de muchas salidas de ADCIRC (como todo un año por ejemplo), usando el programa mkObsFrcstPairs.py para cada archivo individual. 
#Este programa es un wrapper para usar mkObsFrcstPairs.py en muchos archivos.
#Programador Oscar Jurado
#Fecha de creacion: Sep/2017

#------------------Requisitos------------------------------------------------------------
#Lista de nodos a usar para cada dominio

#-----------------Versiones---------------------------------------------------------------
#v1.0 Se crea el programa. 


#----------------Problemas Conocidos-----------------------------------------------------


#----------------Directorios Locales, cambiar si es necesario----------------------------
DIR_OBS=../dataFiles/observaciones/2017/texas
DIR_SCRIPT=`pwd`
DIR_FOR=../dataFiles/pronosticos/timeSeries
DIR_OUT=../dataFiles/observaciones/2017/fixed
DIR_STATIONS=../dataFiles/estaciones_texas
#En este caso particular los archivos tienen este camino:
#OBS: ../dataFiles/observaciones/2015/testout.txt
#FOR: ../dataFiles/pronosticos/timeSeries/2015/01/TimeSeries_pom_m_01_d_31_120h_25492_node.txt
rm fixObservation.py
#Comenzamos con el anio que vamos a leer, que esta dentro del directorio validacion_ADCIRC

#for STATION in campeche celestun frontera islamujeres morelos progreso sisal telchac tuxpan veracruz acapulco angel chiapas huatulco lazaro mazatlan salina vallarta zihuatanejo
for STATION in `ls ${DIR_STATIONS}`
do

        for YEAR in 2015
        do

            STATNAME=${DIR_OBS}/${STATION}
            #Aqui es donde empieza lo bueno, modificar el template para usarlo. 
            #El primer paso es cambiar el nombre del archivo a usar
            sed 's:'STATION':'$STATNAME':g' fixObservationdates.py.template_tx > fixObservation.py.pre
            sed 's:'OUTFILE':'${DIR_OUT}/${STATION}':g' fixObservation.py.pre > fixObservation.py
            python fixObservation.py
            rm fixObservation.py.pre 
        done
    

done
