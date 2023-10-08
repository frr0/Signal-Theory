#%%
import numpy as np
import matplotlib.pyplot as plt

# Create an array of values for t
t = np.linspace(-10, 10, 1000)

# Calculate the sinc function values
sinc_t = np.sinc(t)

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(t, sinc_t, label='sinc(t)', color='blue', linewidth=2)
plt.xlabel('t')
plt.ylabel('sinc(t)')
plt.title('Plot of sinc(t)')
plt.grid(True)
plt.legend()
plt.show()

# %%
