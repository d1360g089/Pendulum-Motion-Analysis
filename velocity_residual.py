
import numpy as np
import matplotlib.pyplot as plt

# Original data
t_data = np.array([
    16, 17.6, 19.4, 21, 22.8, 24.5, 26.1, 29.5, 31.4, 33, 34.9, 36.5, 48, 44.8
])

A_data = np.array([
    60, 52.3, 42.3, 38.2, 34.2, 33, 32.2, 31.1, 30.8, 29.9, 28.4, 27.0, 26.4, 24.8
])

A0_fit = 79.903
b_fit = 0.0299


def amplitude_decay(t, A0, b):
    return A0 * np.exp(-b*t)

predicted = amplitude_decay(t_data, A0_fit, b_fit)

residuals = A_data - predicted

# Plot residuals
plt.figure(figsize=(8, 5))
plt.scatter(t_data, residuals, color='blue')
plt.axhline(0, color='red', linestyle='--', label="Zero Line")
plt.xlabel("Time (s)")
plt.ylabel("Residual (Actual - Predicted Amplitude)")
plt.title("Residual Plot for Angular Velocity Decay Fit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()