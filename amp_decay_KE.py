
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

def exp_decay(t, KE0, b):
    return KE0 * np.exp(-b * t)

#fit curve
params, covriance = curve_fit(exp_decay, t, KE, p0=(.5,.1))

KE0_fit, b_fit = params

print(f"Fitted initial KE: {KE0_fit:.4f}")
print(f"Fitted decay rate (b): {b_fit:.4f}")

#Plot data and fit
plt.scatter(t, KE, label="Measured KE peaks")
t_fit = np.linspace(min(t), max(t), 100)
plt.plot(t_fit, exp_decay(t_fit, *params), 'r-', label="Fitted Exponential Decay")

plt.xlabel("Time(s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Pendulum KE Peaks and Exponential Decay Fit")
plt.legend()
plt.grid(True)
plt.show()


