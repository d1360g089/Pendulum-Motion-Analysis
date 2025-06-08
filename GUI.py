

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.integrate import odeint



# Differential Equation

def damped_pendulum_eq(y, t, zeta, omega0):
    theta, omega = y
    dydt = [omega, -2 * zeta * omega0 * omega - omega0**2 * theta]
    return dydt

# Simulation and plot

def simulate_and_plot(theta0, zeta, omega0, t_max, graph_type, mass):
    t = np.linspace(0, t_max, 1000)
    y0 = [theta0, 0.0]
    sol = odeint(damped_pendulum_eq, y0, t, args=(zeta, omega0))

    fig, ax = plt.subplots()

    if graph_type == "Displacement":
        ax.plot(t, sol[:, 0], label='θ(t)')
        ax.set_ylabel("Angle (rad)")

    elif graph_type == "Velocity":
        ax.plot(t, sol[:, 1], label='ω(t)')
        ax.set_ylabel("Angular Velocity (rad/s)")

    elif graph_type == "Kinetic Energy":
        KE = 0.5 * mass * (sol[:, 1]**2)
        ax.plot(t, KE, label="KE(t)")
        ax.set_ylabel("Kinetic Energy (J)")

    # Differential equation string for the title
    eq_str = r"$\ddot{\theta} + 2\zeta\omega_0\dot{\theta} + \omega_0^2\theta = 0$" + \
             f"\nWhere: $\\zeta = {zeta:.2f}$, $\\omega_0 = {omega0:.2f}$"

    ax.set_title(f"{graph_type} vs Time\n{eq_str}", fontsize=13)
    ax.set_xlabel("Time (s)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


# GUI
def run_gui():
    root = tk.Tk()
    root.title("Pendulum Motion Simulator")

    # Input Fields

    inputs = {
        "Initial Angle (rad)" : tk.DoubleVar(value=.2),
        "Damping Ratio (zeta)": tk.DoubleVar(value=.05),
        "Natural Frequency (rad/s)": tk.DoubleVar(value=2.0),
        "Mass (kg, for KE only)": tk.DoubleVar(value=1.0),
        "Duration (s)": tk.DoubleVar(value=20.0),
    }

    for i, (label, var) in enumerate(inputs.items()):
        ttk.Label(root, text=label).grid(row=i, column=0, sticky='w')
        ttk.Entry(root, textvariable=var).grid(row=i, column=1)

    graph_type = tk.StringVar(value="Displacement")
    ttk.Label(root, text="Graph Type").grid(row=len(inputs), column=0, sticky='w')
    ttk.Combobox(root, textvariable=graph_type, values=["Displacement", "Velocity", "Kinetic Energy"]).grid(row=len(inputs), column=1)

    def on_submit():
        theta0 = inputs["Initial Angle (rad)"].get()
        zeta = inputs["Damping Ratio (zeta)"].get()
        omega0 = inputs["Natural Frequency (rad/s)"].get()
        mass = inputs["Mass (kg, for KE only)"].get()
        t_max = inputs["Duration (s)"].get()
        gt = graph_type.get()

        simulate_and_plot(theta0, zeta, omega0, t_max, gt, mass)

    ttk.Button(root, text="Simulate", command=on_submit).grid(row=len(inputs)+1, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    run_gui()