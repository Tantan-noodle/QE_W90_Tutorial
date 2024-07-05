#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:10:08 2024

@author: tommy
"""
#Electronic band
import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=500,figsize=(4,4))
data = np.loadtxt("ThFeAsN_bands.dat.gnu")
N = np.sum(data[:,0]==0)
tmp = np.array_split(data, N)

Ef = 13.1690

print('# of bands:  ', N)
#for i in range(N):
#for i in range(32,42):
for i in range(31,43):
  plt.plot(tmp[i][:, 0], tmp[i][:, 1]-Ef, linewidth=1, alpha=1.0, color='b')
  print('Indices of bands:  ', i+1)
  

DIS_FROZ_MAX = 2.0
DIS_FROZ_MIN = -1.5
DIS_WIN_MAX = 2.6
DIS_WIN_MIN = -1.9
plt.axhline(DIS_FROZ_MAX,linestyle='--',color='limegreen',label='Inner energy window')  
plt.axhline(DIS_FROZ_MIN,linestyle='--',color='limegreen')    
plt.axhline(DIS_WIN_MAX,linestyle='--',color='darkgreen',label='Outer energy window')   
plt.axhline(DIS_WIN_MIN,linestyle='--',color='darkgreen')   
print('DIS_FROZ_MAX:  ', DIS_FROZ_MAX+Ef)
print('DIS_FROZ_MIN:  ', DIS_FROZ_MIN+Ef)
print('DIS_WIN_MAX:  ', DIS_WIN_MAX+Ef)
print('DIS_WIN_MIN:  ', DIS_WIN_MIN+Ef)

plt.ylim(-2.3,3.2)  
plt.xlim(data[0,0],data[-1,0])
plt.ylabel("E-E$_{f}$ (eV)",fontsize=15)
plt.title("ThFeAsN Electronic bandstructure")
plt.axvline(x=data[0, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[50, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[100, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[150, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[200, 0], linewidth=0.5, color='k', alpha=0.5)
plt.xticks(ticks= [data[0, 0], data[50, 0], data[100, 0], data[150, 0], data[200, 0]], \
           labels=['$\Gamma$', 'X', 'M', '$\Gamma$', 'Z'],fontsize=15)
plt.hlines(0,data[0,0],data[-1,0],linestyles='dotted',colors="k")


#Wannier band
data_wan = np.loadtxt("ThFeAsN_band_wan.dat")
N = np.sum(data_wan[:,0]==0)
tmp_wan = np.array_split(data_wan, N)
x_r = data[200, 0]/np.max(tmp_wan[0][:, 0])
#for i in range(N):
#  plt.plot(tmp_wan[i][:, 0]*x_r, tmp_wan[i][:, 1]-Ef, linewidth=1, alpha=1.0, color='r', linestyle="dashdot")

#EPW-Wannier band
data_epw = np.loadtxt("ThFeAsN_band_epw.dat")
N = np.sum(data_epw[:,0]==0)
tmp_epw = np.array_split(data_epw, N)
x_r = data[200, 0]/np.max(tmp_epw[0][:, 0])
for i in range(N):
  plt.plot(tmp_epw[i][:, 0]*x_r, tmp_epw[i][:, 1]-Ef, linewidth=2, alpha=1.0, color='r', linestyle=":")

plt.plot(0,0, color='b', label='DFT-PBE')
plt.plot(0,0, ':', linewidth=2, color='r', label='EPW-Wannier')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.savefig('electronic_band.png')


