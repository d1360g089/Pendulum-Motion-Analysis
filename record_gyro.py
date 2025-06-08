

import matplotlib.pyplot as plt
import csv

time_vals = []
gyroX_vals = []
gyroY_vals =[]
gyroZ_vals = []

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        time_vals.append(float(row[0]))
        gyroX_vals.append(float(row[1]))
        gyroY_vals.append(float(row[2]))
        gyroZ_vals.append(float(row[3]))
    
    plt.figure(figsize=(10,6))
    plt.plot(time_vals, gyroX_vals, label="Gyro X")
    plt.plot(time_vals, gyroY_vals, label="Gyro Y")
    plt.plot(time_vals, gyroZ_vals, label="Gyro Z")
    plt.title("Angular Velocity (from CSV)")
    plt.xlabel("Time(sec)")
    plt.ylabel("°/s")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()