import serial, time
port = '/dev/ttyACM0' #port in your laptop
baud =115200
#sending 9 specific numbers
ser =serial.Serial(port,baud)
for i in range(10):
	ser.write(b'-200,15,0,199,37,-5,50,64,7\n')
	time.sleep(1)

ser.close()
