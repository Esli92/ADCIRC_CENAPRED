#getFort63TimeSeries
#This program takes output file "fort.63.nc" from an ADCIRC simulation and generates time series for the desired node.
#Programmer Oscar Jurado (ojurado@ciencias.unam.mx)
#Creation date: 11-September-2017

#------------------Requisites------------------------------------------------------------
#fort.64.nc output from ADCIRC. 
# netCDF4 for python MUST be installed. 


#-----------------Version---------------------------------------------------------------
#v1.0 11/Oct/16 Program is created


#----------------Known issues-----------------------------------------------------------


#-----------------Local directories----------------------------------------------------- 


#----------------Dependencies used-----------------------------------------------------
import netCDF4 as nc
import numpy
import numpy.ma as ma
#import matplotlib.pyplot as plt
#-----------------BEGIN PROGRAM--------------------------------------------------------

#We start by loading the ncfile, with reading permissions to avoid changing anything.

ncfile = nc.Dataset("/LUSTRE/ID/validacion_ADCIRC/2015/10/pom/pom-2015-10-31-120h-fort.63.nc","r",format="NETCDF4")

#We can now get the variables needed, u10, v10 and MSLP.

time = ncfile["time"]
zeta = ncfile["zeta"]
lat = ncfile["y"]
lon = ncfile["x"]

#We also store the dimensions of the variables needed:

n_tim = len(ncfile.dimensions["time"])
#n_tim = 1
n_nodes = len(ncfile.dimensions["node"])

#These variables will be netcdf4 type variables, so we'll need to do slicing before using them. 

#Declare the nodes to get a time series from (list)

nodes = [25350,23758,24780,21593,19545,19564,17522,17615,17624,21037,18734]

times = time[:]-432000
dates = nc.num2date(time[:]-432000,units=time.units,calendar='standard')
#Start loop for each node
for node in nodes:
    zeta_node = zeta[:,node-1]
    #Print the file
    filename = '/LUSTRE/ID/ADCIRC/TimeSeries2015/10/TimeSeries_pom_m_10_d_31_120h_{}_node.txt'.format(node)
    o_file = open(filename,'w')
    for tim in range(n_tim):
        if zeta_node[tim] is ma.masked:
            line = '{:%Y,%m,%d,%H,%M,%S}, 0.0\n'.format(dates[tim])
        else:
            line = '{:%Y,%m,%d,%H,%M,%S},{:06.15f}\n'.format(dates[tim],zeta_node[tim])
        o_file.write(line)
        
    o_file.close()

##########OPTIONAL SECTION:###############
#Plot the time series

#plt.plot(times,zeta_node)
#plt.xlabel('Time')
#plt.ylabel('Sea level elevation (m)')
#plt.title('ADCIRC node {} Time Series'.format(node))
#plt.show()

