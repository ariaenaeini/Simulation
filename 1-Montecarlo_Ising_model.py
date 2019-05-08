import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k ,h, hbar, pi

print(k)
def means (s0,T,z):
    s = np.tanh(s0*z/(T))
    print(s)
    return s

s = np.zeros(100)
z = 4
s[0] = z
T=100

for i in range (0,99):
    s[i+1]=means(s[i],T,z)

print(s)

plt.plot(s)

plt.show()

