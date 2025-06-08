
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import serial
import time

arduinoData = serial.Serial("com3", 115200, timeout=1)
time.sleep(1)

kineticY_vals = []

time_vals = []

start_time = time.time()

#Axis Setup
fig, ax = plt.subplots(figsize=(10,6))


csvfile = open("data.csv", "w", newline="")
writer = csv.writer(csvfile)
writer.writerow(["Time(s)", "KE_Y"])

def update(i):
    try:
        if arduinoData.in_waiting:
            line = arduinoData.readline().decode('utf-8').strip()
            split_data = line.split(',')

            if len(split_data) >= 1:
                ke_Y = float(split_data[0])
                t = time.time() - start_time
                writer.writerow([f"{t:.4f}", f"{ke_Y:6}"])

                kineticY_vals.append(ke_Y)
                time_vals.append(t)

                max_points = 200
                

                ax.clear()
                ax.plot(time_vals[-max_points:], kineticY_vals[-max_points:], label="KE_Y")
                ax.set_title('Kinetic Energy Data')
                ax.set_xlabel('Time (s)')
                ax.set_ylabel('Kinetic Energy (J)')
                ax.grid(True)
                ax.legend(loc='upper right')

    except Exception as e:
        print(f"Error: {e}")




ani = animation.FuncAnimation(fig, update, interval=50)
plt.tight_layout()
plt.show()

csvfile.close()




