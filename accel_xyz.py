
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Serial Connection
arduinoData = serial.Serial("com3", 115200, timeout=1)
time.sleep(1)

# list to store data 
accX_vals = []
accY_vals = []
accZ_vals = []



time_vals = []

start_time = time.time()

# Axis Setup
fig, ax1 = plt.subplots(figsize=(10,6))

def update(i):

    try:
        if arduinoData.in_waiting:
            line = arduinoData.readline().decode('utf-8').strip()
            split_data = line.split(',')

            if len(split_data) >= 3:
                accX = float(split_data[0])
                accY = float(split_data[1])
                accZ = float(split_data[2])
                t = time.time() - start_time

                accX_vals.append(accX)
                accY_vals.append(accY)
                accZ_vals.append(accZ)
                time_vals.append(t)

                max_points = 200
                accX_vals[:] = accX_vals[-max_points:]
                accY_vals[:] = accY_vals[-max_points:]
                accZ_vals[:] = accZ_vals[-max_points:]
                time_vals[:] = time_vals[-max_points:]

                ax1.clear()
                ax1.plot(time_vals, accX_vals, label='Acc X')
                ax1.plot(time_vals, accY_vals, label='Acc Y')
                ax1.plot(time_vals, accZ_vals, label='Acc Z')
                ax1.set_title('Accelerometer Data')
                ax1.set_xlabel('Time (s)')
                ax1.set_ylabel('m/s²')
                ax1.grid(True)
                ax1.legend(loc='upper right')

    except Exception as e:
        print(f"Error: {e}")


ani = animation.FuncAnimation(fig, update, interval=50)
plt.tight_layout()
plt.show()




