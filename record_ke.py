

import matplotlib.pyplot as plt
import csv

time_vals = []
kineticY_vals = []
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        time_vals.append(float(row[0]))
        kineticY_vals.append(float(row[1]))
        
    
    plt.figure(figsize=(10,6))
    plt.plot(time_vals, kineticY_vals, label="KE_Y")
    plt.title("Kinetic Energy Data (csv)")
    plt.xlabel("Time(sec)")
    plt.ylabel("Kinetic Energy (J)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()