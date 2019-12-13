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

# variable space: PRIs, amplitudes, phase
pri = 100e-9
f = 1.0 / pri

waveFcn = lambda A, t, f, phi: A * signal.square(2 * np.pi * f * t - phi)

print(f'Frequency: {f}')

wave = waveFcn(1, t, f, 0)

plt.plot(t,wave)
plt.show()