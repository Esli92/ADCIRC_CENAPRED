#!/bin/bash

#execRscripts_Verif_Daily.sh
#Programa para autogenerar lineas de leer ciertas estaciones para los scripts de R, de tal manera que no haya que hacerlo manual para cada estacion, usando los archivos diarios de las estaciones individuales.
#Programador Oscar Jurado
#Fecha de creacion: Feb/2017

#------------------Requisitos------------------------------------------------------------
#Directorio de estaciones a usar
#Archivos con datos estacionales en pares obs/pron para cada estacion

#-----------------Versiones---------------------------------------------------------------
#v1.0 Se crea el programa. 


#----------------Problemas Conocidos-----------------------------------------------------


#----------------Directorios Locales, cambiar si es necesario----------------------------
DIRECTORIO_ESTACIONES=../dataFiles/estaciones
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
DIR_FOR=../dataFiles/pronosticos/timeSeries
INTERVALO=120
DOMAIN=pom

rm *.Rout
#for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
for INTERVALO in 02
do

find ./verify_daily/${INTERVALO}/ -name "*.R" -exec R CMD BATCH {} \;

mkdir -p ./verify_daily/${INTERVALO}/out


for MES in `ls $DIR_FOR/2015`
do
			for STATION in `ls $DIRECTORIO_ESTACIONES`
			do
				for DAY in `ls $DIR_FOR/2015/$MES/TimeSeries_${DOMAIN}_*_17521_node.txt | awk -F'_' '{print $6}'`
				do
				mv R_scriptLines_${MES}_${DAY}_${STATION}.Rout verify_daily/${INTERVALO}/out
				done
			done
done

done
