import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

T = np.array([671.84, 676.78, 682.955, 682.955, 682.955, 689.13, 689.13, 689.13, 
              695.305, 695.305, 695.305, 701.48, 701.48, 701.48, 701.48, 
              707.655, 707.655, 707.655, 707.655, 713.83, 713.83, 713.83, 713.83])
k = np.array([2.539925414, 2.860855, 3.56704, 3.227025, 4.430155, 16.22606, 7.045655, 7.621065,
              11.57047, 8.771885, 10.10579, 19.83200736, 24.098715, 20.72381649, 28.57122,
              33.12219, 27.9435, 32.1919266, 31.7511117, 48.998275, 38.117795, 55.49937978, 53.19328183])

inv_T = 1 / T
ln_k = np.log(k)

slope, intercept, r_value, p_value, std_err = linregress(inv_T, ln_k)

def regression_line(x):
    return slope * x + intercept

plt.figure(figsize=(8, 6))
plt.scatter(inv_T, ln_k, color='blue')
plt.plot(inv_T, regression_line(inv_T), label=f'y = {slope:.4f}x + {intercept:.4f}', color='red')
plt.xlabel('1/T')
plt.ylabel('ln k')
plt.title('Závislost ln k na 1/T')
plt.legend()
plt.grid()
plt.show()
