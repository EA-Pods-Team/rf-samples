import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


N = 100
DT = 5e-9

T = N*DT

(t,step) = np.linspace(0,T, num=N, endpoint=False, retstep=True)
print(f'Step: {step}')

#this janky step gets rid of some rounding issues I have
t = t - DT/100


pri = 100e-9
f = 1.0 / pri
print(f'Frequency: {f}')
wave = signal.square(2*np.pi * f * t)

plt.plot(t,wave)
plt.show()