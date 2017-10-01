#!/bin/bash

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

#-----------------Local directories----------------------------------------------------- 

DIRECTORIO_SCRIPTS=`pwd`
#DIRECTORIO_GRUPOS=../../observaciones/dataFiles/gruposEstaciones
DIRECTORIO_SEASONS=./season_months
TARGET_DIR=verify_monthly/${INTERVALO}/out

DIRECTORIO_ESTACIONES=../dataFiles/estaciones
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
YEAR=2015

for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
do

    for ESTAD in MAE MSE ME 
    do
        for STATION in `ls $DIRECTORIO_ESTACIONES`
        do
            sed 's:'ESTADISTICO':'$ESTAD':g' plotStatistics.py > pltStats.py.pre
            sed 's:'INFILE':'verify_monthly/${INTERVALO}/csv/${ESTAD}_${STATION}':g' pltStats.py.pre > pltStats.py2.pre
            sed 's:'STATION':'$STATION':g' pltStats.py2.pre > pltStats.py 
            
            rm *.pre
            python pltStats.py
            
        done
    done
done
