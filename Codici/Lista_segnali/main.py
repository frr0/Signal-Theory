#%%
import numpy as np
import matplotlib.pyplot as plt

def HPi(T, t):
    y = np.where((t < T/2) & (t > -T/2), 1, 0)
    y = y + 0.5 * ((t == -T/2) | (t == T/2)).astype(float)
    return y

t = np.arange(-2, 2, 0.01)
signal = HPi(1, t)

plt.figure()
plt.plot(t, signal, 'r', linewidth=2)
plt.grid(True)
plt.axis([-2, 2, -0.2, 2.0])
plt.show()
print('fatto')
# %%
