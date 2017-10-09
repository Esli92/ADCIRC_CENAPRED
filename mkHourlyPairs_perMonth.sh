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

DIR_SCRIPT=`pwd`
DIR_PARES=../dataFiles/pares/120
DIR_OUT=../dataFiles/pares/horarios
DIR_ESTACIONES=../dataFiles/estaciones_chidas
DIRECTORIO_MESES=./fechas/months

mkdir -p ${DIR_OUT}
rm -rf ${DIR_OUT}/*

for STATION in `ls ${DIR_ESTACIONES}`
do
    for MES in `ls ${DIRECTORIO_MESES}`
    do
        mkdir -p ${DIR_OUT}/m${MES}
        #ObsFct_Pairs_19701_37_10_e_120_15.txt
        for FILE in `ls ${DIR_PARES}/ObsFct_Pairs_${STATION}_??_${MES}_e_120_*`
        do
            for HOUR in $(seq 2 120)
            do
                HOUR1=$(($HOUR-1))
                sed "${HOUR}q;d" ${FILE} >> ${DIR_OUT}/m${MES}/ObsFct_Pairs_st_${STATION}_h${HOUR1}_m${MES}.txt
            done
        done
    done
done
