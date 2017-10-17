#mkStationReadsSeasons.sh
#Programa para autogenerar scripts que generan diagramas de Taylor.
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

#Vamos a ir de RES>VAR>SEAS>STAT

mkdir -p readStation/taylor

rm readStation/taylor/*.R

figlet TAYLOR DIAGRAM
echo "GENERATING R SCRIPTS FOR THE TAYLOR DIAGRAMS, PLEASE WAIT!"
for SEASON in `ls $DIRECTORIO_MESES`
do
        TARGET=readStation/taylor/R_scriptLines_${SEASON}.R
        cat taylor_header.h > $TARGET
        #cat taylor_headergom.h > $TARGET
        sed 's/'INTERVALO'/'24'/g' $TARGET > ${TARGET}.p
        sed 's/'SEASON'/'${SEASON}'/g' ${TARGET}.p > $TARGET
        rm ${TARGET}.p
        #for INTERVALO in 02 24 47 79 91 06 61 48 96 72 120
        #for INTERVALO in 06 61 120
        #for INTERVALO in 48 72
        for INTERVALO in 02 91
        do
		for STATION in `ls $DIRECTORIO_ESTACIONES`
		do


				sed 's/'INTERVALO'/'${INTERVALO}'/g' readStationTaylor.template > readStation.pre
				sed 's/'SEASON'/'${SEASON}'/g' readStation.pre > readStation.pre2
				sed 's/'STATION'/'${STATION}'/g' readStation.pre2 > readStation.pre
                                #sed 's/'SHAPE'/'17'/g' readStation.pre > readStation.pre2
                                case ${STATION} in
                                17522)
                                    sed 's/'SHAPE'/'15'/g' readStation.pre > readStation.pre2
                                    ;;
                                17615)
                                    sed 's/'SHAPE'/'16'/g' readStation.pre > readStation.pre2
                                    ;;
                                17624)
                                    sed 's/'SHAPE'/'17'/g' readStation.pre > readStation.pre2
                                    ;;
                                19545)
                                    sed 's/'SHAPE'/'18'/g' readStation.pre > readStation.pre2
                                    ;;
                                21037)
                                    sed 's/'SHAPE'/'19'/g' readStation.pre > readStation.pre2
                                    ;;
                                23758)
                                    sed 's/'SHAPE'/'15'/g' readStation.pre > readStation.pre2
                                    ;;
                                24780)
                                    sed 's/'SHAPE'/'16'/g' readStation.pre > readStation.pre2
                                    ;;
                                11129)
                                    sed 's/'SHAPE'/'15'/g' readStation.pre > readStation.pre2
                                    ;;
                                19881)
                                    sed 's/'SHAPE'/'16'/g' readStation.pre > readStation.pre2
                                    ;;
                                29907)
                                    sed 's/'SHAPE'/'17'/g' readStation.pre > readStation.pre2
                                    ;;
                                44732)
                                    sed 's/'SHAPE'/'18'/g' readStation.pre > readStation.pre2
                                    ;;
                                45878)
                                    sed 's/'SHAPE'/'19'/g' readStation.pre > readStation.pre2
                                    ;;
                                73509)
                                    sed 's/'SHAPE'/'15'/g' readStation.pre > readStation.pre2
                                    ;;
                                75448)
                                    sed 's/'SHAPE'/'16'/g' readStation.pre > readStation.pre2
                                    ;;
                                esac
                                
                                case ${INTERVALO} in
                                02)
                                    sed 's/'COLOR'/'red'/g' readStation.pre2 > readStation.pre
                                    ;;
                                24)
                                    sed 's/'COLOR'/'blue'/g' readStation.pre2 > readStation.pre
                                    ;;
                                47)
                                    sed 's/'COLOR'/'blueviolet'/g' readStation.pre2 > readStation.pre
                                    ;;
                                79)
                                    sed 's/'COLOR'/'burlywood'/g' readStation.pre2 > readStation.pre
                                    ;;
                                91)
                                    sed 's/'COLOR'/'orange'/g' readStation.pre2 > readStation.pre
                                    ;;
                                06)
                                    sed 's/'COLOR'/'gray'/g' readStation.pre2 > readStation.pre
                                    ;;
                                61)
                                    sed 's/'COLOR'/'forestgreen'/g' readStation.pre2 > readStation.pre
                                    ;;
                                48)
                                    sed 's/'COLOR'/'hotpink'/g' readStation.pre2 > readStation.pre
                                    ;;
                                96)
                                    sed 's/'COLOR'/'orange'/g' readStation.pre2 > readStation.pre
                                    ;;
                                72)
                                    sed 's/'COLOR'/'seagreen1'/g' readStation.pre2 > readStation.pre
                                    ;;
                                120)
                                    sed 's/'COLOR'/'sienna'/g' readStation.pre2 > readStation.pre
                                    ;;
                                esac
				cat readStation.pre >> $TARGET
				rm readStation.pre readStation.pre2
		
		done
	done
	cat taylor_tail.txt >> $TARGET
done

echo "THE SCRIPTS ARE READY, FIND THEM IN ReadStation/taylor"
echo "I WILL NOW ATTEMPT TO RUN THE SCRIPTS USING R CMD BATCH, PLEASE WAIT!!. THIS OPERATION COULD TAKE A FEW MINUTES"
rm *.Rout

echo "Here, have a random quote while you wait"
cowsay -f "$(ls /usr/share/cows/ | sort -R | head -1)" "$(fortune -s)"

find ./readStation/taylor -name "*.R" -exec R CMD BATCH {} \;

mkdir -p plots/out
mkdir -p plots/taylor

mv *.Rout plots/out

cd plots/taylor

for FILE in `ls`
do
	convert ${FILE} -fuzz 1% -trim +repage ${FILE}b
done

rm *.jpg

rename .jpgb .jpg *
figlet DONE

