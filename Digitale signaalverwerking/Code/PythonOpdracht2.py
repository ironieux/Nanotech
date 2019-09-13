#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:39:57 2019

@author: beli
"""

# -*- coding: utf-8 -*-
"""
Opdracht 2 van Digitale Signaalbewerking
    a: stepresponse voor a=1 en 1/2
    b: absoverdracht over frequentie voor deze twee
    c: faseoverdracht over frequentie voor deze twee
"""
import scipy.signal as scig
import matplotlib.pyplot as plt
import numpy as np

#opdracht A constanten
a = 1
num = [0, 1]
den = [1, -a]
len_ = 10
dt = 1

#plotten van opdracht A
plt.figure(0)
plt.subplot(321)
n,y = scig.dimpulse((num,den,dt),n=len_)
plt.stem(n,y[0])
plt.grid()
plt.xlabel('n' )
plt.ylabel('h[n]')
plt.title('Impulse Response voor a=1')

#opdracht B constanten
omega = np.arange(-np.pi,np.pi,0.05)

#plotten van opdracht B
plt.subplot(323)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)
plt.plot(w/np.pi,np.abs(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('|H(omega)|')
plt.title('Absolute Transfer voor a=1')


#plotten van opdracht C
plt.subplot(325)
plt.plot(w/np.pi,np.angle(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('Fase H(omega)')
plt.title('Transfer Fase voor a=1')

#a veranderen
a = 1/2
num = [0, 1]
den = [1, -a]
len_ = 10
dt = 1

#plotten van opdracht A
plt.figure(0)
plt.subplot(322)
n,y = scig.dimpulse((num,den,dt),n=len_)
plt.stem(n,y[0])
plt.grid()
plt.xlabel('n' )
plt.ylabel('h[n]')
plt.title('Impulse Response voor a=1/2')

#opdracht B constanten
omega = np.arange(-np.pi,np.pi,0.05)

#plotten van opdracht B
plt.subplot(324)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)
plt.plot(w/np.pi,np.abs(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('|H(omega)|')
plt.title('Absolute Transfer voor a=1/2')


#plotten van opdracht C
plt.subplot(326)
plt.plot(w/np.pi,np.angle(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('Fase H(omega)')
plt.title('Transfer Fase voor a=1/2')

plt.tight_layout()