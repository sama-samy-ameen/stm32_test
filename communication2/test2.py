import serial, time
port = '/dev/ttyACM0' #port in your laptop
baud =115200
#sending 8 specific numbers for thrusters
ser =serial.Serial(port,baud)
while True:
	print('sent:\n')
	ser.write(b'150,0,200,-200,100,150,60,0\n')
	print('recieved from stm:\n')
	print(ser.readline().decode().strip()
	time.sleep(1)
