#!/bin/bash

#mkVerifStatFiles_contData.sh
#Program that takes output of R scripts for verification, and creates a file for each station with its statistic values for each MES (like MAE,ME,MSE). 
#Programmer Oscar Jurado (ojurado@ciencias.unam.mx)
#Creation date: 25-Feb-2017

#------------------Requisites------------------------------------------------------------
#Results from verification tests with continuous data
#verify_daily directory

#-----------------Version---------------------------------------------------------------
#v1.0 25/Feb/17 Program is created


#----------------Known issues-----------------------------------------------------------

#-----------------Local directories----------------------------------------------------- 

DIRECTORIO_SCRIPTS=`pwd`
#DIRECTORIO_GRUPOS=../../observaciones/dataFiles/gruposEstaciones
DIRECTORIO_SEASONS=./season_months
TARGET_DIR=verify_daily/${INTERVALO}/out

DIRECTORIO_ESTACIONES=../dataFiles/estaciones_chidas
DIRECTORIO_MESES=./fechas/monthszero
DIRECTORIO_MESES2=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
INTERVALO=120

#-----------------BEGIN PROGRAM--------------------------------------------------------

#Example of result directory
#verify_daily/${INTERVALO}/out/${VARIABLE}/${MES}

for INTERVALO in 02
do

rm *.out 
rm verify_daily/${INTERVALO}/out/*.csv 
mkdir -p verify_daily/${INTERVALO}/csv 
rm  verify_daily/${INTERVALO}/csv/*
	#VARIABLE=WS
	
		for MES in `ls $DIRECTORIO_MESES`
		do
            for MONTH in `ls $DIRECTORIO_MESES2`
            do
			#head -1 csv_daily_header.txt > MAE_${RESOLUTION}_${MES}_${VARIABLE}.csv
			#head -1 csv_daily_header.txt > ME_${RESOLUTION}_${MES}_${VARIABLE}.csv
			#head -1 csv_daily_header.txt > MSE_${RESOLUTION}_${MES}_${VARIABLE}.csv
			for STATION in `ls $DIRECTORIO_ESTACIONES`
			do
				for DAY in `ls ../dataFiles/pares/02/ObsFct_Pairs_24780_??_${MONTH}_e_02_15.txt | awk -F'_' '{print $4}'`
				do
				
					TARGET=verify_daily/${INTERVALO}/out/R_scriptLines_${MES}_${DAY}_${STATION}.Rout
					
					if grep -Fq "MAE               =" $TARGET
					then
						grep -F "MAE               =" $TARGET > MAE_${MES}_${DAY}.out
						awk -F' ' -v OFS=',' -v DAY=$DAY '$3==($3+0) {print $3,DAY}' MAE_${MES}_${DAY}.out >> verify_daily/${INTERVALO}/csv/MAE_${MES}_${STATION}.csv
					else
						echo "NaN,$DAY" >> verify_daily/${INTERVALO}/csv/MAE_${MES}_${STATION}.csv
					fi

					if grep -Fq "ME                =" $TARGET
					then
						grep -F "ME                =" $TARGET > ME_${MES}_${DAY}.out
						awk -F' ' -v OFS=',' -v DAY=$DAY '$3==($3+0) {print $3,DAY}' ME_${MES}_${DAY}.out >> verify_daily/${INTERVALO}/csv/ME_${MES}_${STATION}.csv
					else
						echo "NaN,$DAY" >> verify_daily/${INTERVALO}/csv/ME_${MES}_${STATION}.csv
					fi
	
					if grep -Fq "MSE               =" $TARGET
					then
						grep -F "MSE               =" $TARGET > MSE_${MES}_${DAY}.out
						awk -F' ' -v OFS=',' -v DAY=$DAY '$3==($3+0) {print $3,DAY}' MSE_${MES}_${DAY}.out >> verify_daily/${INTERVALO}/csv/MSE_${MES}_${STATION}.csv
					else
						echo "NaN,$DAY" >> verify_daily/${INTERVALO}/csv/MSE_${MES}_${STATION}.csv
					fi
				done
			done
		done
    done
done

#rm *.out

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
# 				TARGET_DIR=verify_daily/${INTERVALO}/out
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
# 				TARGET_DIR=verify_daily/${INTERVALO}/out
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






