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
DIR_OBS=../dataFiles/observaciones/2015
DIR_SCRIPT=`pwd`
DIR_FOR=../dataFiles/pronosticos/timeSeries
DIR_OUT=../dataFiles/pares/120h
NODE=17521
#En este caso particular los archivos tienen este camino:
#OBS: ../dataFiles/observaciones/2015/testout.txt
#FOR: ../dataFiles/pronosticos/timeSeries/2015/01/TimeSeries_pom_m_01_d_31_120h_25492_node.txt

#Comenzamos con el anio que vamos a leer, que esta dentro del directorio validacion_ADCIRC

for YEAR in `ls $DIR_FOR`
do
    #Ahora necesitamos movernos entre los meses del anio
    for MONTH in `ls $DIR_FOR/$YEAR`
    do
        mkdir -p ${DIR_OUT}/${MONTH}
        #Y por ultimo nos movemos entre los dos dominios, gom y pom
        for DOMAIN in gom pom
        do
            #Ahora nos movemos entre los diferentes archivos que hay, solo los fort.63.nc
            for DAY in `ls $DIR_FOR/$YEAR/$MONTH/TimeSeries_${DOMAIN}_* | awk -F'_' '{print $6}'`
            do
                FILENAME=TimeSeries_${DOMAIN}_m_${MONTH}_d_${DAY}_120h_${NODE}_node.txt
                #Aqui es donde empieza lo bueno, modificar el template para usarlo. 
                #El primer paso es cambiar el nombre del archivo a usar
                sed 's:'FILENAME':'$DIR_FOR/$YEAR/$MONTH/$FILENAME':g' mkObsFrcstPairs.py.template > mkPairs.py
		python mkPairs.py               
            done
        done
    done
done
