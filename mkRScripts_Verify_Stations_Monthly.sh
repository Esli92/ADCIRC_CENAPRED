#mkStationReadsSeasons.sh
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
DIRECTORIO_ESTACIONES=../dataFiles/estaciones_chidas
DIRECTORIO_MESES=./fechas/months
DIRECTORIO_DIAS=./fechas/days
DIRECTORIO_MESES_SIM=meses_sim
DIR_FOR=../dataFiles/pronosticos/timeSeries

#Vamos a ir de RES>VAR>SEAS>STAT

rm *.Rout

if [ ! -d "verify_monthly/" ]
then
	mkdir verify_monthly
fi

for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
do


if [ ! -d "verify_monthly/${INTERVALO}" ]
then
	mkdir verify_monthly/${INTERVALO}
fi

rm verify_monthly/${INTERVALO}/*

for YEAR in `ls $DIR_FOR`
do
    #mkdir verify_daily/${INTERVALO}/${VARIABLE}

       for MONTH in `ls ${DIRECTORIO_MESES}`
       do
       DOMAIN=pom
       # source $DIRECTORIO_MESES/$MES

                for STATION in `ls $DIRECTORIO_ESTACIONES`
                do


                        #sed 's/'MES'/'${MES}'/g' readStation.pre > readStation.pre2
                        sed 's/'STATION'/'${STATION}'/g' readStationVerify_monthly.template > readStation.pre
                        sed 's/'INTERVALO'/'${INTERVALO}'/g' readStation.pre > readStation.pre2
                        sed 's/'NUES'/'${MONTH}'/g' readStation.pre2 > verify_monthly/${INTERVALO}/R_scriptLines_m${MONTH}_${STATION}.R
                        rm readStation.pre readStation.pre2
                done
            done
      done       
done


