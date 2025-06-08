
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

arduinoData = serial.Serial("com3", 115200, timeout=1)
time.sleep(1)

gyroX_vals = []
gyroY_vals = []
gyroZ_vals = []

time_vals = []

start_time = time.time()

#Axis Setup
fig, ax = plt.subplots(figsize=(10,6))


csvfile = open("data.csv", "w", newline="")
writer = csv.writer(csvfile)
writer.writerow(["Time(s)", "Gyro X", "Gyro Y", "GyroZ"])



def update(i):
    try:
        if arduinoData.in_waiting:
            line = arduinoData.readline().decode('utf-8').strip()
            split_data = line.split(',')

            if len(split_data) >= 3:
                gyroX = float(split_data[0])
                gyroY = float(split_data[1])
                gyroZ = float(split_data[2])
                t = time.time() - start_time
                writer.writerow([t,gyroX,gyroY,gyroZ])


                gyroX_vals.append(gyroX)
                gyroY_vals.append(gyroY)
                gyroZ_vals.append(gyroZ)
                time_vals.append(t)

                max_points = 200
                

                ax.clear()
                ax.plot(time_vals[-max_points:], gyroX_vals[-max_points:], label='Gyro X')
                ax.plot(time_vals[-max_points:], gyroY_vals[-max_points:], label='Gyro Y')
                ax.plot(time_vals[-max_points:], gyroZ_vals[-max_points:], label='Gyro Z')
                ax.set_title('Angular Velocity Data')
                ax.set_xlabel('Time (s)')
                ax.set_ylabel('°/s')
                ax.grid(True)
                ax.legend(loc='upper right')

    except Exception as e:
        print(f"Error: {e}")




ani = animation.FuncAnimation(fig, update, interval=50)
plt.tight_layout()
plt.show()

csvfile.close()

