# -*- coding: utf-8 -*-
"""
Post-processing of WEST L and H modes

J.Hillairet
03/09/2018

ICRH Antenna radial position in WEST : 2890-3060 (170mm). 
LPA radial position in WEST : 2880-3080 (200mm)
LH Antenna radial position in WEST : 2910-3060 (150mm)

"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

# There is three profiles 
# for three Averaged Line Density (LAD)
R1_H, ne1_H = np.loadtxt('Ne_prof_WEST_Hmode_01_LAD6_Rsep_293.txt', skiprows=1, unpack=True)
R2_H, ne2_H = np.loadtxt('Ne_prof_WEST_Hmode_01_LAD9_Rsep_293.txt', skiprows=1, unpack=True)
R3_H, ne3_H = np.loadtxt('Ne_prof_WEST_Hmode_01_LAD12_Rsep_293.txt', skiprows=1, unpack=True)

# These profile are defined vs the radial position (in metre)
# In HFSS, the plasma profiles should start a x=0, so we reverse the abscisse
# from a given radius
def x(R, R_x0=2.93):
    return - R1_H + R_x0

plt.subplots()
plt.plot(x(R1_H), ne1_H)
plt.plot(x(R2_H), ne2_H)
plt.plot(x(R3_H), ne3_H)

# reverse the array in order to have increasing values of x for HFSS compatibility
np.savetxt('HFSS_density_profile_LAD6.txt', np.flipud(np.array([x(R1_H), ne1_H]).T))

# export ascii files profiles for HFSS



# 
#
#
#figure(1)
#plot(R1_H, ne1_H, R2_H, ne2_H, R3_H, ne3_H, lw=2)
#xlabel('R [m]')
#ylabel('$n_e$ [$m^{-3}$]')
#grid(True)
#legend(('$\overline{n}_e=6.10^{19} m^{-2}$', '$\overline{n}_e=9.10^{19} m^{-2}$', '$\overline{n}_e=12.10^{19} m^{-2}$'))
#title('WEST H-mode Density profile')
#axvline(x=2.93, ymin=0, ymax=2e20, linestyle='--', color='k') # separatrix
#
## ICRH limiter radial location 
##gca().add_patch(Rectangle((2.890, 0), 0.170, 1.5e20, facecolor='r', alpha=0.2)) # (x, y), width, height
#
## Proposed Antenna Limiter Radial Location
#axvline(x=2.95, ymin=0, ymax=2e20, linestyle='-.', color='k') 
#axvline(x=2.975, ymin=0, ymax=2e20, linestyle='-.', color='k') 
#axvline(x=3.00, ymin=0, ymax=2e20, linestyle='-.', color='k') 
#
#
#
##
## L-mode
##
#R1_L, ne1_L = np.loadtxt('Ne_prof_WEST_Lmode_02_LAD2_4_Rsep_293.txt', skiprows=1, unpack=True)
#R2_L, ne2_L = np.loadtxt('Ne_prof_WEST_Lmode_02_LAD5_4_Rsep_293.txt', skiprows=1, unpack=True)
#R3_L, ne3_L = np.loadtxt('Ne_prof_WEST_Lmode_02_LAD8_4_Rsep_293.txt', skiprows=1, unpack=True)
#
#fig2 = figure(2)
#plot(R1_L, ne1_L, R2_L, ne2_L, R3_L, ne3_L, lw=2)
#xlabel('R [m]')
#ylabel('$n_e$ [$m^{-3}$]')
#grid(True)
#legend(('$\overline{n}_e=2.10^{19} m^{-2}$', '$\overline{n}_e=5.10^{19} m^{-2}$', '$\overline{n}_e=8.10^{19} m^{-2}$'))
#title('WEST L-mode Density profile')
#
## ICRH limiter radial location 
#gca().add_patch(Rectangle((2.890, 0), 0.170, 1.5e20, facecolor='r', alpha=0.2)) # (x, y), width, height
#
#axvline(x=2.93, ymin=0, ymax=2e20, linestyle='--', color='k') # sepratrix
#
#
## The profiles are exported for TOPICA evaluation, 
## and corresponds to the larger antenna-separatrix distance; 
## Then Daniele take care of the other two positions removing 2.5cm and 5cm from the low density side of the profile.
#R_limiter = 3.0 # maximum radial location
## Find the index in the arrays corresponding to R=R_limiter
#idx=np.where(R1_H == R_limiter)
#R_export = R1_H[:idx[0][0]+1]
#ne_LAD6  = ne1_H[:idx[0][0]+1]
#ne_LAD9  = ne2_H[:idx[0][0]+1]
#ne_LAD12 = ne3_H[:idx[0][0]+1]
# 
#figure(3)
#plot(R_export, ne_LAD6, R_export, ne_LAD9, R_export, ne_LAD12)
#
#np.savetxt('TOPICA_WEST_H-mode_ne_LAD6_Rsep_2.93m.txt', np.c_[R_export, ne_LAD6], 
#           header=''' WEST H-mode density profile - 20/06/2014 \n Line Average Density = 6e19 m^-2 \n R [m] \t ne [m-3]''' )
#np.savetxt('TOPICA_WEST_H-mode_ne_LAD9_Rsep_2.93m.txt', np.c_[R_export, ne_LAD9], 
#           header=''' WEST H-mode density profile - 20/06/2014 \n Line Average Density = 9e19 m^-2 \n R [m] \t ne [m-3]''' )
#np.savetxt('TOPICA_WEST_H-mode_ne_LAD12_Rsep_2.93m.txt', np.c_[R_export, ne_LAD12], 
#           header=''' WEST H-mode density profile - 20/06/2014 \n Line Average Density = 12e19 m^-2 \n R [m] \t ne [m-3]''' )
#
#
## Te profile
#import scipy as sp
## H-mode Te profile from CRONOS
#data = sio.loadmat('Te_WEST_MPHIMNHH_HR_eq_data.mat')
#R_Te = data['RR']
#Te = data['Te'].transpose()
#
#figure(5)
#plot(R_Te, Te)
## Take the same value than the min to fill the SOL up to R=3.0 m
#R_Te = np.append(R_Te, 3)
#Te = np.append(Te, np.min(Te))
#
#plot(R_Te, Te)
#
#Te_resample = np.interp(R_export, R_Te, Te)
#np.savetxt('TOPICA_WEST_H-mode_Te.txt', np.c_[R_export, Te_resample], 
#           header=''' WEST H-mode temperature profile - 20/06/2014 \n  R [m] \t Te [eV]''' )