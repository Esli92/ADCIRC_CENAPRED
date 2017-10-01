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

DIRECTORIO_ESTACIONES=../dataFiles/estaciones_chidas
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
YEAR=2015
#-----------------BEGIN PROGRAM--------------------------------------------------------

#Example of result directory
#verify_monthly/${INTERVALO}/out/${VARIABLE}/${MES}

find ./verify_monthly -name "???_all.csv" -exec rm {} \;

	#VARIABLE=WS
		for STAT in MAE ME MSE
		do
			#head -1 csv_daily_header.txt > MAE_${RESOLUTION}_${MES}_${VARIABLE}.csv
			#head -1 csv_daily_header.txt > ME_${RESOLUTION}_${MES}_${VARIABLE}.csv
			#head -1 csv_daily_header.txt > MSE_${RESOLUTION}_${MES}_${VARIABLE}.csv
			for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
			#for INTERVALO in 02
            do
                mkdir -p verify_monthly/${INTERVALO}/stats
                TARGET=verify_monthly/${INTERVALO}/stats/${STAT}_all.csv
                rm pre* 
                echo "months" > pre_001.txt
                awk -F',' -v OFS=',' '{print $2}' verify_monthly/${INTERVALO}/csv/${STAT}_17521.csv >> pre_001.txt
                
                
                for STATION in `ls $DIRECTORIO_ESTACIONES`
                do
                    source ${DIRECTORIO_ESTACIONES}/${STATION}
                    echo ${NAME} > pre_${STATION}.txt
					awk -F',' -v OFS=',' '{print $1}' verify_monthly/${INTERVALO}/csv/${STAT}_${STATION}.csv >> pre_${STATION}.txt
					paste -d"," pre_*.txt > $TARGET 
					
				done
			done
		done


rm pre_*

# 
# #############-----------------------------ADDING MONTHS FOR DIFFERENT SEASONS-----------------------------------------------------------------------------------
# 
# for SEASON in `ls $DIRECTORIO_SEASONS`
# do
# 	source $DIRECTORIO_SEASONS/$SEASON
# 	for RESOLUTION in `ls $DIRECTORIO_RESOLUCIONES`
# 	do
# 		for VARIABLE in `ls $DIRECTORIO_VARIABLES`
# 		do
# 		#VARIABLE=WS
# 			for STATION in `ls $DIRECTORIO_ESTACIONES`
# 			do
# 				TARGET_DIR=verify_monthly/${INTERVALO}/out
# 				mkdir ${TARGET_DIR}/${SEASON}
# 				cat ${TARGET_DIR}/MSE_${RESOLUTION}_${MES1}_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_${MES2}_${VARIABLE}_${STATION}.csv > ${TARGET_DIR}/${SEASON}/MSE_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 
# 				cat ${TARGET_DIR}/ME_${RESOLUTION}_${MES1}_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_${MES2}_${VARIABLE}_${STATION}.csv > ${TARGET_DIR}/${SEASON}/ME_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 
# 				cat ${TARGET_DIR}/MAE_${RESOLUTION}_${MES1}_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_${MES2}_${VARIABLE}_${STATION}.csv > ${TARGET_DIR}/${SEASON}/MAE_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 			done
# 		done
# 	done
# done
# 		
# #--------------------For ALL seasons---------------------------------------------------------------------------------------------------	
# #for SEASON in `ls $DIRECTORIO_SEASONS`
# #do
# SEASON=ALL
# 	for RESOLUTION in `ls $DIRECTORIO_RESOLUCIONES`
# 	do
# 		for VARIABLE in `ls $DIRECTORIO_VARIABLES`
# 		do
# 		#VARIABLE=WS
# 			for STATION in `ls $DIRECTORIO_ESTACIONES`
# 			do
# 				TARGET_DIR=verify_monthly/${INTERVALO}/out
# 				mkdir ${TARGET_DIR}/${SEASON}
# 				cat ${TARGET_DIR}/MSE_${RESOLUTION}_04_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_05_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_08_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_09_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_11_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MSE_${RESOLUTION}_12_${VARIABLE}_${STATION}.csv  > ${TARGET_DIR}/${SEASON}/MSE_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 
# 				cat ${TARGET_DIR}/ME_${RESOLUTION}_04_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_05_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_08_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_09_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_11_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/ME_${RESOLUTION}_12_${VARIABLE}_${STATION}.csv  > ${TARGET_DIR}/${SEASON}/ME_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 
# 				cat ${TARGET_DIR}/MAE_${RESOLUTION}_04_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_05_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_08_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_09_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_11_${VARIABLE}_${STATION}.csv ${TARGET_DIR}/MAE_${RESOLUTION}_12_${VARIABLE}_${STATION}.csv  > ${TARGET_DIR}/${SEASON}/MAE_${RESOLUTION}_${SEASON}_${VARIABLE}_${STATION}.csv
# 			done
# 		done
# 	done
# #done






