#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import send_emergency_land
#import cflib.crtp

eland_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(eland_pin, GPIO.IN)

"""
# Initiate the low level drivers
cflib.crtp.init_drivers()

print('Scanning interfaces for Crazyflies...')
available = cflib.crtp.scan_interfaces()
print('Crazyflies found:')

available_count = -1
available_array = []

for i in available:
    available_count+=1
    print(available_count,":  ", i[0])
    available_array.append(i[0])
uri_choise = int(input("select your cf radio: "))
uri = str(available_array[uri_choise])
"""
uri = "radio://0/80/2M"
print(uri)

while(True):
    time.sleep(0.5)
    if(GPIO.input(eland_pin)==GPIO.LOW):
        print("activated emergency landing!")
        send_emergency_land.main(uri)
        time.sleep(3)
    else:
        print("...")
