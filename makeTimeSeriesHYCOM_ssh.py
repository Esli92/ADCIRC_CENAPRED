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

ncfile = nc.Dataset("../hycom/Anual3d_cut_Veracruz.nc","r",format="NETCDF4")
adfile = nc.Dataset("../hycom/casos/02_nuevoMetodoInterp/fort.64.nc","r",format="NETCDF4")
zfile = nc.Dataset("../hycom/casos/02_nuevoMetodoInterp/fort.63.nc","r",format="NETCDF4")
nosshfile = nc.Dataset("../hycom/fort.63_elev.nc","r",format="NETCDF4")

def geo_idx(dd, dd_array):
   geo_idx = (numpy.abs(dd_array - dd)).argmin()
   return geo_idx

#We can now get the variables needed, u10, v10 and MSLP.

time = ncfile["MT"]
lat = ncfile["lat"]
lon = ncfile["lon"]
u = ncfile["u"]
v = ncfile["v"]
ssh = ncfile["ssh"]

lats = lat[:]
lons = lon[:]

lat_ad = adfile["y"]
lon_ad = adfile["x"]
u_ad = adfile["u-vel"]
v_ad = adfile["v-vel"]
zeta = zfile["zeta"]
zenssh = nosshfile["zeta"]

#We also store the dimensions of the variables needed:

n_tim = len(ncfile.dimensions["MT"])
#n_tim = 1
n_nodes = len(ncfile.dimensions["lon"])

boundary_nodes = range(0,77)
b_lats = lat_ad[boundary_nodes]
b_lons = lon_ad[boundary_nodes]
#These variables will be netcdf4 type variables, so we'll need to do slicing before using them. 

#Declare the nodes to get a time series from (list)
nodes = boundary_nodes

dates = nc.num2date(time[:],units=time.units,calendar='standard')
for nd in boundary_nodes:
    filename = '../hycom/casos/02_nuevoMetodoInterp/TimeSeries_{}_node_nossh.txt'.format(nd)
    o_file = open(filename,'w')
    line = 'Datetime,ua_hycom,va_hycom,u_adcirc,v_adcirc,ssh_hycom,zeta_adcirc,zetanossh_ad,xcoord,ycoord,ad_lats,ad_lons,hy_lats,hy_lons\n'
    o_file.write(line)
    xcoord = geo_idx(b_lons[-nd],lons)
    ycoord = geo_idx(b_lats[-nd],lats)
    for tim in range(0,720):
        uh = u[tim,:,ycoord,xcoord]
        ua = uh.mean()
        vh = v[tim,:,ycoord,xcoord]
        va = vh.mean()
        sshy = ssh[tim,ycoord,xcoord]
        zeta_node = zeta[tim,nd]
        zenssh_node = zenssh[tim,nd]
        uvel_node = u_ad[tim,nd]
        vvel_node = v_ad[tim,nd]
        #Print the file
        line = '{:%Y-%m-%d %H:%M:%S},{:06.15f},{:06.15f},{:06.15f},{:06.15f},{:06.15f},{:06.15f},{:06.15f},{:d},{:d},{:06.4f},{:06.4f},{:06.4f},{:06.4f}\n'.format(dates[tim],ua,va,uvel_node,vvel_node,sshy,zeta_node,zenssh_node,xcoord,ycoord,b_lats[nd],b_lons[nd],lats[ycoord],lons[xcoord])
        o_file.write(line)
    o_file.close()
            
#times = time[:]-432000

#Start loop for each node



##########OPTIONAL SECTION:###############
#Plot the time series

#plt.plot(times,zeta_node)
#plt.xlabel('Time')
#plt.ylabel('Sea level elevation (m)')
#plt.title('ADCIRC node {} Time Series'.format(node))
#plt.show()

