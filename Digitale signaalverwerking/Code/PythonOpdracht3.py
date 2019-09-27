#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:30:24 2019

@author: beli
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scig

Amp = 1 #volt
omega = 1000 #rad/s
tau = 0.001

tijd = np.linspace(0,0.01,500)

v_x = Amp * np.sin( omega * tijd )
v_y = Amp * omega * np.cos( omega * tijd ) * tau

#vraag a
plt.figure(0)
plt.plot(tijd, v_x, label = 'v_x')
plt.plot(tijd, v_y, label = 'v_y')
plt.legend()

num = [-1*tau,0]
den = [0,1]

#vraag b
plt.figure(1)
w,H = scig.freqs(num,a=den)
plt.subplot(211)
plt.plot(w,np.abs(H))
plt.grid()
plt.subplot(212)
plt.plot(w,np.angle(H))
plt.grid()

#vraag c
k = 0.001

num = [-k,k]
den = [1,0]
len_ = 10
dt = 1

plt.figure(2)
n,y = scig.dimpulse((num,den,dt),n=len_)
plt.subplot(311)
plt.stem(n,y[0])
plt.grid()

omega = np.arange(-np.pi,np.pi,0.05)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)

plt.subplot(312)
plt.plot(w/np.pi,np.abs(H))
plt.grid()

plt.subplot(313)
plt.plot(w/np.pi,np.angle(H)/np.pi)
plt.grid()
plt.xlabel(r'$\Omega / 2\pi$')
plt.ylabel(r'Fase $\psi$ [$\mathrm{\omega / 2\pi}$]')