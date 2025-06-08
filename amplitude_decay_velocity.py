
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


t_data = np.array([
    16, 17.6, 19.4, 21, 22.8, 24.5, 26.1, 29.5, 31.4, 33, 34.9, 36.5, 48, 44.8

])

A_data = np.array([
    60, 52.3, 42.3, 38.2, 34.2, 33, 32.2, 31.1, 30.8, 29.9, 28.4, 27.0, 26.4, 24.8
])




#Velocity Decay Function
def amplitude_decay(t, A0, b):
    return A0 * np.exp(-b * t)


params, _ = curve_fit(amplitude_decay, t_data, A_data, p0=(60, 0.01))

A0_fit, b_fit = params

t = np.linspace(15, 50, 500)
fitted_curve = amplitude_decay(t, A0_fit, b_fit)

manual_curve = A0_fit * np.exp(-0.0184 * t)


print(f"Fitted initial Velocity: {A0_fit:.4f}")
print(f"Fitted decay rate (b): {b_fit:.4f}")


plt.figure(figsize=(10,5))
plt.scatter(t_data, A_data, color="black", label='Measured Velocity Peaks')
plt.plot(t, fitted_curve, color='red',label=f"Fit: $A(t)$")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude(Velocity)(deg/s)")
plt.title("Angular Velocity Amplitude Decay Fit")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

