import sys,serial,time

arduino = serial.Serial(sys.argv[1],
                     baudrate=sys.argv[2],
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=1,
                     xonxoff=0,
                     rtscts=0
                     )
# Toggle DTR to reset Arduino
arduino.setDTR(False)
time.sleep(1)
# toss any data already received, see
# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
arduino.flushInput()
arduino.setDTR(True)

with arduino:
    while True:
        print(arduino.readline())
