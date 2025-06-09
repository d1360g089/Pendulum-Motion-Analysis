
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

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
L = r
I = m * r**2
g = 9.81  # gravity

# Angular velocity function
def omega(t):
    return B * np.exp(-gamma * t) * np.cos(omega_d * t + phase_shift)

# Compute ω(t) and integrate to get θ(t)
v = omega(t)
theta = cumulative_trapezoid(v, t, initial=0)

# Compute energies
KE = 0.5 * I * v**2
PE = m * g * L * (1 - np.cos(theta))
ME = KE + PE

# --- PEAK EXTRACTION ---

# Find peaks in ME
peak_indices, _ = find_peaks(ME)
t_peaks = t[peak_indices]
ME_peaks = ME[peak_indices]

# --- EXPONENTIAL FIT TO PEAKS ---

def exp_decay(t, E0, lambd):
    return E0 * np.exp(-lambd * t)

# Fit to peak values
params, _ = curve_fit(exp_decay, t_peaks, ME_peaks, p0=[np.max(ME_peaks), 0.1])
E0_fit, lambda_fit = params
fit_curve = exp_decay(t, E0_fit, lambda_fit)

# --- PLOTTING ---

plt.figure(figsize=(10, 5))

plt.scatter(t_peaks, ME_peaks, color='orange', label='Extracted Peaks')
plt.plot(t, fit_curve, '--', color='crimson',
label=f'Exponential Fit to Peaks: $E_0 e^{{-{lambda_fit:.4f}t}}$')
plt.title("Mechanical Energy vs Time with Exponential Decay Fit to Peaks")
plt.xlabel("Time (s)")
plt.ylabel("Mechanical Energy (J)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()