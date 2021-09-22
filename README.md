# reset_arduino
reset arduino via serial

reset_arduino.py: send reset code to arduino via serial

usage: python3 reset_arduino.py "/dev/tty.usbmodem1463401" 9600

reset_arduino0.py:  send reset code to arduino via serial and read serial after 1sec

usage: python3 reset_arduino0.py "/dev/tty.usbmodem1463401" 9600

reset_arduino_testdriver.ino: test driver for eset_arduino0.py, serial speed 9600

ref:

python - Wait on Arduino auto-reset using pySerial - Stack Overflow
https://stackoverflow.com/questions/21073086/wait-on-arduino-auto-reset-using-pyserial
