import serial

port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
port.write('on')
print(port.readline())
port.close()
