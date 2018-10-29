import serial
ser = serial.Serial('COM3', 2400, timeout=0.035)
while True:
    #ch = ser.read()
    #if ch == '':
	ser.write(b'xAA')
    #    ser.flush()
    #else:
    #    print('%s ' %(ch.hex()))
    #pass
ser.close()             # close port
