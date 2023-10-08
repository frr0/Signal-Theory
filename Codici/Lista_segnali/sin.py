#%%
import numpy as np
import matplotlib.pyplot as plt

# Creazione di un array di valori x da -2*pi a 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calcolo dei valori di sin(x) e cos(x)
sin_x = np.sin(x + np.pi/2)
sin_x1 = np.sin(1/2 * x + np.pi/2)
cos_x = np.cos(x)

# Creazione del grafico
plt.figure(figsize=(8, 4))  # Imposta le dimensioni della figura

# Plot di sin(x) in blu e cos(x) in rosso
plt.plot(x, sin_x, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, sin_x1, label='sin streched', color='green', linewidth=2)
plt.plot(x, cos_x, label='cos(x)', color='red', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico di sin(x) e cos(x)')
plt.grid(True)
plt.legend()

plt.show()

# %%
