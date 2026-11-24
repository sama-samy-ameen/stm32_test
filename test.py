import serial,random,time

usb=serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)

for i in range(50) :
	n=random.randint(0,100)
	usb.write(bytes([n]))
	if n>50:
		print("on")
	else:
		print("off")
	time.sleep(1)
