# ADCIRC_CENAPRED
Scripts desarrollados en el marco del proyecto CENAPRED-IOA de la UNAM para la validacion del modelo ADCIRC. 

Scripts en el repositorio:

makeTimeSeries.py -- Toma datos de una salida fort.63.nc y una lista de nodos y extrae la serie de tiempo de altura del agua
		     para esos nodos. 

mkObsFrcstPairs.py --	Toma la serie de tiempo hecha con makeTimeSeries.py de fort.63.nc y un archivo de observaciones de 
			estaciones mareograficas del Servicio Mareografico Nacional de la UNAM y genera un archivo de pares
			observacion pronostico. Un ejemplo de la serie de tiempo y de la observacion esta incluido en el 
			repositorio en forma de archivos .txt

mkRScripts_Verify_Stations_Daily_120h.sh -- 	Este script genera automaticamente scripts de R para hacer la verificacion de 
						los pares observacion pronostico usando la libreria "verification". Para usar
						este script se necesita el template readStationVerify_daily.template.

readStationVerify_daily.template -- 	Ejemplo de script en R que usa la libreria "verification" para hacer una verificacion
					de datos continuos. 

execRScripts_Verif_Daily.sh -- 	Script de bash que permite ejecutar automaticamente los scripts generados por mkRScripts... 
				Para correrlo se necesita una carpeta con las fechas y meses a usar, asi como las estaciones,
				que en este caso son los nodos de la malla de interes. 

mkCSVErrors_Stations_Daily.sh -- 	Script de bash que toma los resultados de la ejecucion de execRScripts... y lee unicamente
					los valores estadisticos de interes, lo que permite manejarlos mas facilmente. 

testmarea.txt -- 	Documento ejemplo de observaciones mareograficas del SMN, obtenido en su pagina web. 

timeSeries_19564_node.txt -- 	Ejemplo de salida del programa makeTimeSeries.py
