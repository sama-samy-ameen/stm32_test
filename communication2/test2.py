import serial, time
port = '/dev/ttyACM0' #port in your laptop
baud =115200
#sending 8 specific numbers for thrusters
ser =serial.Serial(port,baud)
for i in range(10):
	ser.write(b'\n')
	time.sleep(1)

ser.close()
