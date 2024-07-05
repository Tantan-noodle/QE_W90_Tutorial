#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:25:14 2024

@author: tommy
"""
#Phonon band
import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=500,figsize=(4,4))

cminv2mev = 0.124

#plot1
#ax[0].set_title("$Ba_2CuO_{3.4}$ Phonon bandstructure (w/o SOC)")
#data = np.loadtxt("ThFeAsN.freq.gp")
data = np.loadtxt("ThFeAsN.freq.gp")
nbands = data.shape[1] - 1
for i in range(nbands):
  plt.plot(data[:, 0], data[:, i+1]*cminv2mev, linewidth=1, alpha=1.0, color='b')
  
data = np.loadtxt("ThFeAsN_scf663.freq.gp")
nbands = data.shape[1] - 1
for i in range(nbands):
  plt.plot(data[:, 0], data[:, i+1]*cminv2mev, linewidth=1, alpha=1.0, color='r', linestyle='--')  


plt.axvline(x=data[0, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[50, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[100, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[150, 0], linewidth=0.5, color='k', alpha=0.5)
plt.xticks(ticks= [data[0, 0], data[50, 0], data[100, 0], data[150, 0]], \
           labels=['$\Gamma$', 'X', 'M', '$\Gamma$'],fontsize=15)
plt.ylabel("Phonon Frequency (meV)",fontsize=15)
plt.title("ThFeAsN Phonon bandstructure")
plt.xlim(data[0, 0], data[150, 0])
plt.ylim(0,85)
plt.plot(0,0, color='b', label='DFT-PBE')
plt.plot(0,0, linestyle='--', color='r', label='DFT-PBE+U')
plt.legend(loc = 'upper left')
plt.tight_layout()
#plt.savefig('phonon_band.png')
plt.savefig('phonon_band_scf663.png')