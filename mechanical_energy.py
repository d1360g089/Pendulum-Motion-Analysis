

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Time array
t = np.linspace(16, 45, 500)

# Damped velocity function parameters
B = 253.8
gamma = 0.0902
omega_d = 3.7
phase_shift = -59.2

# Physical constants
m = 0.05  # mass (kg)
r = 0.508  # length (m)
L = r  # distance from pivot to center of mass
I = m * (r**2)  # moment of inertia
g = 9.81  # gravitational acceleration (m/s^2)

# Angular velocity function ω(t)
def omega(t):
    return B * np.exp(-gamma * t) * np.cos(omega_d * t + phase_shift)

# Compute ω(t) and integrate to get θ(t)
v = omega(t)
theta = cumulative_trapezoid(v, t, initial=0)

# Compute kinetic energy
KE = 0.5 * I * v**2

# Compute potential energy
PE = m * g * L * (1 - np.cos(theta))

# Compute total mechanical energy
ME = KE + PE

# Plot total mechanical energy
plt.figure(figsize=(10, 5))
plt.plot(t, ME, label='Mechanical Energy (Joules)', color='mediumblue')
plt.title("Total Mechanical Energy vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Mechanical Energy (J)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()