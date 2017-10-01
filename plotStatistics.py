#mkVerifStatFiles_contData.sh
#Program that takes output of R scripts for verification, and creates a file for each station with its statistic values for each MES (like MAE,ME,MSE). 
#Programmer Oscar Jurado (ojurado@ciencias.unam.mx)
#Creation date: 25-Feb-2017

#------------------Requisites------------------------------------------------------------
#Results from verification tests with continuous data
#verify_monthly directory

#-----------------Version---------------------------------------------------------------
#v1.0 25/Feb/17 Program is created


#----------------Known issues-----------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------------BEGIN PROGRAM-----------------------------------------------------------

#First read the csv file with the series and month 
sertest = pd.read_csv('INFILE.csv',sep=',',index_col=1,header=None,names=['ESTADISTICO'],squeeze=True,parse_dates=True)


sertest.plot()
plt.ylabel('ESTADISTICO')
figstr = '../figures/stats/ts_plot_s_ESTADISTICO_node_STATION.png'
plt.savefig(figstr)
