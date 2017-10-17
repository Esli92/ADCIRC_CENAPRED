#!/bin/bash

#Programa para unir todos los archivos de pares de observaciones en un solo archivo para usar en R. Genera un archivo mensual de todo, por estacion.

echo 'BULK PAIRS ALL V3.0 -----> ¡Dame un momento!'
#read -p 'Indica la resolucion (5 o 25): ' RESOLUTION
#read -p 'Indica el mes de simulacion (mm): ' MES



DIRECTORIO_ESTACIONES=../dataFiles/estaciones_texas   
DIRECTORIO_MESES=./fechas/months
IND=1
echo $IND
for INTERVALO in 02 24 47 79 91
do
    PAIR_FILES=../dataFiles/pares/${INTERVALO}
    rm ${PAIR_FILES}/monthlyPairs/gom/*
	#for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
	IND=1
	echo $IND
	for MES in 8 9 
	do
        
		

		if [ ! -d "${PAIR_FILES}/monthlyPairs/gom" ]
		then
			mkdir -p ${PAIR_FILES}/monthlyPairs/gom
			rm ${PAIR_FILES}/monthlyPairs/gom/*
		fi	
        
		HEADER_SAMPLE=pairHead
		#cd $PAIR_FILES

		#VARIABLE=TM
		for ESTACION in `ls $DIRECTORIO_ESTACIONES`
		do
				#rm ${PAIR_FILES}/${ESTACION}_m8.txt 
                #if [ $IND=1 ] 
                #then
                #    head -1 ${HEADER_SAMPLE} > ${PAIR_FILES}/${ESTACION}_m8.txt
                #    IND=False
                #    echo $IND
                #fi
				tail -n +2 -q ${PAIR_FILES}/ObsFct_Pairs_${ESTACION}_??_${MES}_e_${INTERVALO}_*  >> ${PAIR_FILES}/${ESTACION}_m8p.txt

				#awk 'BEGIN { FS = "," }; $4 != -99 {print $1","$2","$3","$4","$5}' ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.pre >> ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.txt

				
				#rm ${PAIR_FILES}/${ESTACION}_${VARIABLE}_m${MES}.pre
		done
        cat $HEADER_SAMPLE ${PAIR_FILES}/${ESTACION}_m8p.txt > ${PAIR_FILES}/${ESTACION}_m8.txt
		#Para hacer un archivo con TODOS los pares de TODAS las estaciones del mes
   
	done
	  ${PAIR_FILES}/*_m8.txt ${PAIR_FILES}/monthlyPairs/gom
done


