#!/bin/bash

#Programa para unir todos los archivos de pares de observaciones en un solo archivo para usar en R. Genera un archivo mensual de todo, por estacion.

echo 'BULK PAIRS ALL V2.0 -----> Indica los siguientes datos'
#read -p 'Indica la resolucion (5 o 25): ' RESOLUTION
#read -p 'Indica el mes de simulacion (mm): ' MES



DIRECTORIO_ESTACIONES=../dataFiles/estaciones
DIRECTORIO_MESES=./fechas/months

for MES in `ls $DIRECTORIO_MESES`
do

	for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
	do

		PAIR_FILES=../dataFiles/pares/${INTERVALO}

		if [ ! -d "${PAIR_FILES}/monthlyPairs" ]
		then
			mkdir ${PAIR_FILES}/monthlyPairs
		fi	

		HEADER_SAMPLE=pairHead
		#cd $PAIR_FILES

		#VARIABLE=TM
		for ESTACION in `ls $DIRECTORIO_ESTACIONES`
		do
				rm ${PAIR_FILES}/${ESTACION}_m${MES}.txt 

				head -1 ${HEADER_SAMPLE} > ${PAIR_FILES}/${ESTACION}_m${MES}.txt; tail -n +2 -q ${PAIR_FILES}/ObsFct_Pairs_${ESTACION}_??_${MES}_e_${INTERVALO}_*  >> ${PAIR_FILES}/${ESTACION}_m${MES}.txt

				#awk 'BEGIN { FS = "," }; $4 != -99 {print $1","$2","$3","$4","$5}' ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.pre >> ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.txt

				mv ${PAIR_FILES}/${ESTACION}_m${MES}.txt ${PAIR_FILES}/monthlyPairs
				#rm ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.pre
		done

		#Para hacer un archivo con TODOS los pares de TODAS las estaciones del mes

	done
done
