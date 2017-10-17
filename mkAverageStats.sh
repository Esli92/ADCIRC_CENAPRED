#!/bin/bash

mkdir -p verify_monthly/avs
rm verify_monthly/avs/*

for DOMAIN in pom gom
do
    for STAT in bias corr rmse rmsedb ioa
    do
        for MES in `seq 1 12`
        do
            LINE=
            SUM=0
            for INTERVALO in 02 24 47 79 91
            do
                AVE=`awk '{if (NR!=1) {print $0}}' verify_monthly/${INTERVALO}/stats/${DOMAIN}/${STAT}_m_${MES}.txt | awk '{ sum += $2; n++ } END { if (n > 0) print sum / n; }'`
                LINE=${AVE},${LINE}
                SUM=`bc -l <<< $AVE+$SUM`
            done
            NAV=`bc -l <<< $SUM/5`
            LINE=${LINE}${NAV}
            echo $LINE >> verify_monthly/avs/ave_${STAT}_${DOMAIN}.txt
        done
    done
done
    
