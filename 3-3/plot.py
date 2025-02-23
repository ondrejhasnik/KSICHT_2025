import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k
N = 1000

N_A_values = np.arange(1, N, 1)

S_values = k * (N * np.log(N) - N_A_values * np.log(N_A_values) - (N - N_A_values) * np.log(N - N_A_values))

max_idx = np.argmax(S_values)
N_A_max = N_A_values[max_idx]
S_max = S_values[max_idx]

min_value = np.min(S_values)
min_indices = np.where(S_values == min_value)[0]
N_A_min_values = N_A_values[min_indices]
S_min_values = S_values[min_indices]

plt.figure(figsize=(8, 5))
plt.plot(N_A_values, S_values, label='Entropie S vs. N_A', color='b')
plt.scatter(N_A_max, S_max, color='r', zorder=3, label=f'Maximum: N_A={N_A_max}')
for N_A_min, S_min in zip(N_A_min_values, S_min_values):
    plt.scatter(N_A_min, S_min, color='g', zorder=3, label=f'Minimum: N_A={N_A_min}')
plt.xlabel('$N_A$')
plt.ylabel('$S$ [J/K]')
plt.title('Závislost entropie na $N_A$')
plt.legend()
plt.grid()
plt.show()
