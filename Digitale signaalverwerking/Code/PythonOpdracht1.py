# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy.signal as scig
import matplotlib.pyplot as plt
import numpy as np

num = [1,1]
den = [1,0]
len_ = 10
omega = np.arange(-np.pi,np.pi,0.05)

plt.figure(0)
t,y = scig.dimpulse((num,den,0.1),n=len_)
plt.stem(t,y[0])
plt.grid()
plt.xlabel('n' )
plt.ylabel('h(n)')

plt.figure(1)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)
plt.plot(w/np.pi,np.abs(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('|H(omega)|')

plt.figure(2)
plt.plot(w,np.angle(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('Fase H(omega)')