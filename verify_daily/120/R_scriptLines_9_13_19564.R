#Load required libraries
library(verification)

#------- ESTACION 19564 -----------------------------------------------------------------------------------------------------------------------------
#--------RESOLUCION 0pRESOLUTION ----------------------------------------------------------------------------------------------------------------------
DAT_RESOLUTION_SEASON_19564 <- read.table("../dataFiles/pares/120h/ObsFct_Pairs_19564_13_9_15.txt",sep = ",", header = TRUE, fill = FALSE)
OBS_RESOLUTION_SEASON_19564 <- DAT_RESOLUTION_SEASON_19564$OBSERVACION
FCT_RESOLUTION_SEASON_19564 <- DAT_RESOLUTION_SEASON_19564$PRONOSTICO

#---------Estadisticas de verificacion-------------------------------------
MOD_RESOLUTION_SEASON_19564 <- verify(OBS_RESOLUTION_SEASON_19564,FCT_RESOLUTION_SEASON_19564, frcst.type = "cont", obs.type = "cont")

summary(MOD_RESOLUTION_SEASON_19564)
