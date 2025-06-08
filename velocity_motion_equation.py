
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(16, 45, 500)

B = 253.8
gamma = 0.0902
omega_d = 3.7
phase_shift = -59.2

# Velocity Differential Equation
def omega(t):
    return B * np.exp(-gamma * t) * np.cos(omega_d*t + phase_shift)

v = omega(t)

plt.figure(figsize=(10, 5))
plt.plot(t, v, label='Fitted Velocity Model', color='blue')
plt.title("Modeled Angular Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s or rad/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()