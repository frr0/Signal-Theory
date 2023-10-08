#%%
import numpy as np
import matplotlib.pyplot as plt

# Parametri del segnale
frequencies = [1.0, 2.0, 3.0]  # Frequenze del segnale
amplitudes = [1.0, 0.5, 0.8]    # Amplitudini del segnale

# Creazione del dominio del tempo
t = np.linspace(0, 10, 1000)

# Creazione del segnale complesso
signal = np.zeros_like(t, dtype=complex)

for freq, amp in zip(frequencies, amplitudes):
    signal += amp * np.exp(1j * 2 * np.pi * freq * t)

# Creazione della figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot del segnale complesso
ax.plot(t, np.real(signal), np.imag(signal), label='Segnale complesso', linewidth=2)

# Impostazioni per la visualizzazione 3D
ax.grid(True)
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('Tempo')
ax.set_ylabel('Parte Reale')
ax.set_zlabel('Parte Immaginaria')
ax.legend()

plt.show()

# %%
