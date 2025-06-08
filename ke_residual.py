

import numpy as np
import matplotlib.pyplot as plt

t = np.array([
    8.2, 9.93, 11.67, 13.34, 14.94, 16.61, 18.21, 19.88,
    21.55, 23.22, 24.89, 26.63, 28.44, 30.11, 31.78, 33.52,
    35.12, 36.86, 38.52, 40.26, 41.93, 43.6
])

KE = np.array([
    0.5003, 0.4098, 0.2996, 0.219, 0.1895, 0.1797, 0.1796, 0.1786,
    0.1688, 0.1601, 0.1503, 0.1394, 0.1306, 0.1197, 0.1099, 0.099,
    0.0892, 0.0805, 0.0696, 0.0598, 0.0499, 0.0478
])

KE0_fit = 0.7162
b_fit = .0671

def exp_decay(t, KE0, b):
    return KE0 * np.exp(-b * t)

KE_predicted = exp_decay(t, KE0_fit, b_fit)

residuals = KE - KE_predicted

plt.figure(figsize=(8,5))
plt.scatter(t, residuals, color='purple')
plt.axhline(0, color='red', linestyle='--', label='Zero line')
plt.xlabel("Time(s)")
plt.ylabel("Residual (Actual KE - Predicted KE)")
plt.title("Residual Plot for Exponential Fit of KE")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
