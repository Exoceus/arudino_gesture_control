import time  # Required to use delay functions
import pyautogui
import serial  # Serial imported for Serial communication

# Create Serial port object called arduinoSerialData
ArduinoSerial = serial.Serial('com3', 9600)
time.sleep(2)  # wait for 2 seconds for the communication to get established


while 1:
    # read the serial data and print it as line
    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'Play' in incoming:
        print(incoming)
        pyautogui.press("playpause")

    if 'Pause' in incoming:
        print(incoming)
        pyautogui.press("playpause")

    incoming = ""
