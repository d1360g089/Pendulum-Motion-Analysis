
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



t_peaks = np.array([
    16.41, 18.10, 19.84, 21.53, 23.17, 24.86,
    26.64, 28.29, 29.98, 31.67, 33.41, 35.10,
    36.79, 38.52, 40.21, 41.86, 43.59
])

A_peaks = np.array([
    15.87, 13.76, 11.7, 10.24, 8.73, 7.6,
    6.46, 5.7, 4.94, 4.24, 3.75, 3.27,
    2.89, 2.51, 2.18, 1.97, 1.81
])


def A_decay(t, A0, delta):
    return A0 * np.exp(-delta * t)

popt, _ = curve_fit(A_decay, t_peaks, A_peaks)

A0, delta = popt

t_fit = np.linspace(min(t_peaks), max(t_peaks), 500)
A_fit = A_decay(t_fit, A0, delta)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(t_peaks, A_peaks, color='red', label='Displacement Peaks')
plt.plot(t_fit, A_fit, 'b--', linewidth=2, label='A(t)')
plt.title('Displacement Amplitude Decay')
plt.xlabel('Time (s)')
plt.ylabel('Displacement Amplitude (rad)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()