"""
This code simply sends 1 emergency land command to the crazyflie
"""

import cflib.crtp as crtp
from cflib.crtp.crtpstack import CRTPPacket
import sys
import time

EMERGENCY_LAND_CMD = 4
CF_URI_INDEX = 1

crtp.init_drivers()

def print_link_quality(link_quality):
    print("link quality:",link_quality)

def print_error(error_msg):
    print("error msg:",error_msg)

def main():
    if len(sys.argv) == 1:
        print('you must give the uri of the crazyflie as an argument')
        return
    
    link = crtp.get_link_driver(sys.argv[CF_URI_INDEX])

    assert link is not None
    
    pk = CRTPPacket(0xFF, [0x03, 0x04, 0,0,0,0,0,0,0])
    
    link.send_packet(pk)
    print("emergency land command sent")
    pk_recv = link.receive_packet(0.1)

    assert pk_recv is not None

    link.close()

if __name__ == "__main__":
    main()