#!/usr/bin/python3
import array, fcntl
from time import sleep
import send_emergency_land
import RPi.GPIO as GPIO
import time
import send_emergency_land

#LCD4DPI_GET_KEYS = -2147202303
_IOC_NRBITS = 8
_IOC_TYPEBITS = 8
_IOC_SIZEBITS = 14
_IOC_DIRBITS = 2
_IOC_DIRMASK = (1 << _IOC_DIRBITS) - 1
_IOC_NRMASK = (1 << _IOC_NRBITS) - 1
_IOC_TYPEMASK = (1 << _IOC_TYPEBITS ) - 1
_IOC_NRSHIFT = 0
_IOC_TYPESHIFT = _IOC_NRSHIFT+_IOC_NRBITS
_IOC_SIZESHIFT = _IOC_TYPESHIFT+_IOC_TYPEBITS
_IOC_DIRSHIFT = _IOC_SIZESHIFT+_IOC_SIZEBITS
_IOC_NONE = 0
_IOC_WRITE = 1
_IOC_READ = 2


eland_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(eland_pin, GPIO.IN)


def _IOC(dir, type, nr, size):
# print 'dirshift {}, typeshift {}, nrshift {}, sizeshift {}'.format(_IOC_DIRSHIFT, IOC_TYPESHIFT, _IOC_NRSHIFT, _IOC_SIZESHIFT)
    ioc = (dir << _IOC_DIRSHIFT ) | (type << _IOC_TYPESHIFT ) | (nr << _IOC_NRSHIFT ) | (size << _IOC_SIZESHIFT)
    if ioc > 2147483647: ioc -= 4294967296
    return ioc

#def _IO(type, nr):
#   return _IOC(_IOC_NONE, type, nr, 0)

def _IOR(type,nr,size):
    return _IOC(_IOC_READ, type, nr, size)

#def _IOW(type,nr,size):
#   return _IOC(_IOC_WRITE, type, nr, sizeof(size))

def main():
    LCD4DPI_GET_KEYS = _IOR(ord('K'), 1, 4)
    buf = array.array('h',[0])

    uri = "radio://0/80/2M"
    print(uri)

    with open('/dev/fb1', 'r+') as fd:
        while True:

            fcntl.ioctl(fd, LCD4DPI_GET_KEYS, buf, 1) # execute ioctl call to read the keys
            keys = buf[0]
            time.sleep(0.2)

            if(GPIO.input(eland_pin)==GPIO.LOW):
                print("activated emergency landing!")
                send_emergency_land.main(uri)
                time.sleep(2)

            if not keys & 0b00001:
                print ("KEY1: SET")
            if not keys & 0b00010:
                print ("KEY2: +10")
            if not keys & 0b00100:
                print ("KEY3: -10")
            if not keys & 0b01000:
                print ("KEY4: -DISCONNECT")
            if not keys & 0b10000:
                print ("KEY5")

            if keys != 0b11111:
                print("000")
            if keys == 0b01110: # exit if top and bottom pressed
                break
            sleep(0.1)

if __name__ == "__main__":
    main()