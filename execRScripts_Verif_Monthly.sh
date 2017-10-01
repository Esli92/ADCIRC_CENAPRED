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
for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
#for INTERVALO in 02
do
rm ./verify_monthly/${INTERVALO}/out/*
find ./verify_monthly/${INTERVALO}/ -name "*.R" -exec R CMD BATCH {} \;

mkdir -p ./verify_monthly/${INTERVALO}/out


mv *.Rout verify_monthly/${INTERVALO}/out


done
