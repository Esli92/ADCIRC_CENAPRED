from scipy import signal
from scipy import fftpack
import matplotlib as mpl

import sys
import csv
import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

##TEST##
#fs = 1.0/3600
#nfft = 12
#f, t, Sxx = signal.spectrogram(adcirc_series,fs=fs)
#plt.pcolormesh(t, f, Sxx)
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()

#Aplying window
time = observ_series.index.astype('int64')/1.0e9
data = observ_series.values
window = signal.blackman(len(data))
data_window = data*window
    
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(observ_series.index, data, label="original")
ax.plot(observ_series.index, data_window, label="windowed")
ax.set_ylabel("elevation", fontsize=14)
ax.legend(loc=0)

data_fft = fftpack.fft(data)
f = fftpack.fftfreq(len(data), time[1]-time[0])

mask = f > 0
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0.000001, 0.00004)
ax.axvline(1./86400, color='r', lw=0.5)
ax.axvline(0.5/86400, color='r', lw=0.5)
ax.axvline(2/86400, color='r', lw=0.5)
ax.plot(f[mask], np.log(abs(data_fft[mask])), lw=2)
ax.set_ylabel("$\log|F|$", fontsize=14)
ax.set_xlabel("frequency (Hz)", fontsize=14)
