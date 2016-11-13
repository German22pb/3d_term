import serial
ser = serial.Serial('COM11', 9600)
while True :
    msg = ser.readline()
    msgStr = str(msg)
    result = msgStr[2: -5]
    print(result)
    file = open('temp.dt', 'w')
    file.write(result)
    file.close()

