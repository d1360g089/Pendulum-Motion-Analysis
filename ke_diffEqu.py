
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(16, 45, 500)

#Velocity Constants
B = 253.8
gamma = .0902
omega_d = 3.7
phase_shift = -59.2

# Physical constants
m = 0.05 #kg
r = 0.508 #meters
I = m * (r**2)

def omega(t):
    return B * np.exp(-gamma * t) * np.cos(omega_d *t + phase_shift)

v = omega(t)
KE = 0.5 * I * v**2 #joules


plt.figure(figsize=(10, 5))
plt.plot(t, KE, label='Kinetic Energy (Joules)', color='darkorange')
plt.title("Kinetic Energy vs Time (Real Units)")
plt.xlabel("Time (s)")
plt.ylabel("Kinetic Energy (J)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

