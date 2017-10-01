#mkStationReadsSeasons.sh
#Programa para autogenerar lineas de leer ciertas estaciones para los scripts de R, de tal manera que no haya que hacerlo manual para cada estacion
#Programador Oscar Jurado
#Fecha de creacion: Nov/2016

#------------------Requisitos------------------------------------------------------------
#Directorio de estaciones a usar
#Archivos con datos estacionales en pares obs/pron para cada estacion

#-----------------Versiones---------------------------------------------------------------
#v1.0 Se crea el programa. 


#----------------Problemas Conocidos-----------------------------------------------------


#----------------Directorios Locales, cambiar si es necesario----------------------------
DIRECTORIO_ESTACIONES=../dataFiles/estaciones_chidas
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
DIR_FOR=../dataFiles/pronosticos/timeSeries

mkdir -p readStation/qq
rm readStation/qq/* 
#Vamos a ir de RES>VAR>SEAS>STAT

for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
do

		
		for STATION in `ls $DIRECTORIO_ESTACIONES`
		do
			
			#rm readStation/R_scriptLines_0p${RESOLUTION}_${VARIABLE}_${SEASON}.R
			
                        cat QQ_plot.template > readStation/qq/R_scriptLines_${INTERVALO}_${STATION}.R
			for SEASON in `ls $DIRECTORIO_MESES`
			do
                            
                            sed 's/'INTERVALO'/'${INTERVALO}'/g' readStationQQ_TM.template > readStation.pre

                            sed 's/'SEASON'/'${SEASON}'/g' readStation.pre > readStation.pre2
                            sed 's/'STATION'/'${STATION}'/g' readStation.pre2 > readStation.pre
                            cat readStation.pre >> readStation/qq/R_scriptLines_${INTERVALO}_${STATION}.R
                            rm readStation.pre readStation.pre2
			done
		done
done

