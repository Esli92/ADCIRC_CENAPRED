#!/bin/bash +x

#bulkTimeSeries.sh 
#Programa para generar series de tiempo de muchas salidas de ADCIRC (como todo un año por ejemplo), usando el programa getTimeSeries.py para cada archivo individual. 
#Este programa es un wrapper para usar getTimeSeries.py en muchos archivos.
#Programador Oscar Jurado
#Fecha de creacion: Sep/2017

#------------------Requisitos------------------------------------------------------------
#Lista de nodos a usar para cada dominio

#-----------------Versiones---------------------------------------------------------------
#v1.0 Se crea el programa. 


#----------------Problemas Conocidos-----------------------------------------------------


#----------------Directorios Locales, cambiar si es necesario----------------------------
DIR_ADCIRC=/LUSTRE/ID/validacion_ADCIRC
DIR_SCRIPT=`pwd`
DIR_OUT=/LUSTRE/ID/ADCIRC/TimeSeries2017

#En este caso particular los archivos tienen este camino:
#/LUSTRE/ID/validacion_ADCIRC/2015/01/gom/gom-2015-01-21-120h-fort.63.nc

#Comenzamos con el anio que vamos a leer, que esta dentro del directorio validacion_ADCIRC

#for YEAR in `ls $DIR_ADCIRC`
for YEAR in 2017
do
    #Ahora necesitamos movernos entre los meses del anio
    for MONTH in `ls $DIR_ADCIRC/$YEAR`
    #for MONTH in 02 10
    do
        mkdir -p ${DIR_OUT}/${MONTH}
        #Y por ultimo nos movemos entre los dos dominios, gom y pom
        for DOMAIN in gom
        do
	    mkdir -p ${DIR_OUT}/${MONTH}
	    rm ${DIR_OUT}/${MONTH}/*
            #Ahora nos movemos entre los diferentes archivos que hay, solo los fort.63.nc
            for DAY in `ls $DIR_ADCIRC/$YEAR/$MONTH/${DOMAIN}/*fort.63.nc | awk -F'-' '{print $4}'`
            do
                FILENAME=${DOMAIN}-${YEAR}-${MONTH}-${DAY}-120h-fort.63.nc
                #Aqui es donde empieza lo bueno, modificar el template para usarlo. 
                #El primer paso es cambiar el nombre del archivo a usar
                sed 's:'FILENAME':'$DIR_ADCIRC/$YEAR/$MONTH/${DOMAIN}/$FILENAME':g' makeTimeSeries.py.template_${DOMAIN} > makeTimeSeries1.py 
                sed 's:'OUTFILE':'${DIR_OUT}/${MONTH}/TimeSeries_${DOMAIN}_m_${MONTH}_d_${DAY}_120h':g' makeTimeSeries1.py > makeTimeSeries.py
		python makeTimeSeries.py                
            done
        done
    done
done
