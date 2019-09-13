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
num = [1, 1]
den = [1, 0]
len_ = 10
dt = 1

#plotten van opdracht A
plt.figure(0)
plt.subplot(311)
n,y = scig.dimpulse((num,den,dt),n=len_)
plt.stem(n,y[0])
plt.grid()
plt.xlabel('n' )
plt.ylabel('h[n]')
plt.title('Impulse Response')

#opdracht B constanten
omega = np.arange(-np.pi,np.pi,0.05)

#plotten van opdracht B
plt.subplot(312)
w,H = scig.freqz(num,a=den,worN=omega,whole=False)
plt.plot(w/np.pi,np.abs(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('|H(omega)|')
plt.title('Absolute Transfer')


#plotten van opdracht C
plt.subplot(313)
plt.plot(w/np.pi,np.angle(H))
plt.grid()
plt.xlabel('Omega in pi rad' )
plt.ylabel('Fase H(omega)')
plt.title('Transfer Fase')

plt.tight_layout()