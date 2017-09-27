#Verification for each station, all year

#This program for R takes verification-observation pair files from WRF forecasts and uses the verification R package to get statistics and plots. 
#Programmer Oscar Jurado (ojurado@ciencias.unam.mx)
#Creation date: 11-Sep-2016

#------------------Requisites------------------------------------------------------------
#WRF/observations pairs made with mkPairs.sh program.
#The input file should be in ../../24h/0p5/RESOLUTION/
#verification and plotrix packages must be instEMAed.  


#-----------------Version---------------------------------------------------------------
#v1.0 11/Sep/16 Program is created
#v2.0 Nov/16 Added Taylor diagrams with plotrix, improved labels on conditional quantile, translated to spanish

#----------------Known issues-----------------------------------------------------------
#for custom conditional_quantiles axis labels to work, the function must be modified to remove xlab and ylab.

#-----------------Local directories----------------------------------------------------- 


#-----------------BEGIN PROGRAM--------------------------------------------------------

#Load required libraries
library(verification)
library(plotrix)

#source("conditional_quantile_esp.R")
# RESOLUCION 0.5
#------- ESTACION ACO -----------------------------------------------------------------------------------------------------------------------------
DAT_5_ALL_ACO <- read.table("../dataFiles/pares/INTERVALO/monthlyPairs/17521_mSEASON.txt",sep = ",", header = TRUE, fill = FALSE)
OBS_5_ALL_ACO <- DAT_5_ALL_ACO$OBSERVACION
FCT_5_ALL_ACO <- DAT_5_ALL_ACO$PRONOSTICO

jpeg(file = "./plots/taylor/TAYLOR_INTERVALO_mSEASON.jpg", width=1800,height=1500,units="px",quality=90,pointsize=33)

taylor.diagram(OBS_5_ALL_ACO,FCT_5_ALL_ACO,add=FALSE,col="red",pch=19,pos.cor=FALSE,
               show.gamma=TRUE,ngamma=4,
               main=" ",gamma.col=3,sd.arcs=1,ref.sd=TRUE,sd.method="sample",
               grad.corr.lines=c(0.2,0.4,0.6,0.8,0.9,0.99),
               pcex=1,cex.axis=1,normalize=TRUE)

lpos<-1.1*(sd(OBS_5_ALL_ACO)/sd(OBS_5_ALL_ACO))
lposy<-lpos+0.4
