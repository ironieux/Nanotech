# -*- coding: utf-8 -*-
"""
Opdracht 1 van Digitale Signaalbewerking
    a: stepresponse
    b: absoverdracht over frequentie
    c: faseoverdracht over frequentie
"""
import scipy.signal as scig
import matplotlib.pyplot as plt
import numpy as np

#opdracht A constanten
num = [1,1]
den = [1,0]
len_ = 10
dt = 1
omega = np.arange(-np.pi,np.pi,0.05)

#plotten van opdracht A
plt.figure(0)
t,y = scig.dimpulse((num,den,dt),n=len_)
plt.stem(t,y[0])
plt.grid()
plt.xlabel('n' )
plt.ylabel('h(n)')

#opdracht B constanten
omega = np.arange(-np.pi,np.pi,0.05)

#plotten van opdracht B
plt.figure(1)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)
plt.plot(w/np.pi,np.abs(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('|H(omega)|')

#plotten van opdracht C
plt.figure(2)
plt.plot(w,np.angle(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('Fase H(omega)')