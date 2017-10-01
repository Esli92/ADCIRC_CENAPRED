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
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
YEAR=2015

for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
do
    mkdir -p ../figures/stats_all/${INTERVALO}
    for ESTAD in MAE MSE ME 
    do

            sed 's:'ESTADISTICO':'$ESTAD':g' plotStatisticsAll.py > pltStats.py.pre
            sed 's:'INFILE':'verify_monthly/${INTERVALO}/stats/${ESTAD}_all':g' pltStats.py.pre > pltStats.py2.pre
            sed 's:'INTERVALO':'$INTERVALO':g' pltStats.py2.pre > pltStats.py
            
            rm *.pre
            python pltStats.py
            
    done
done
