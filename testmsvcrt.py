#
# @(!--#) @(#) testmsvcrt.py, version 001, 07-january-2019
#
# test harness to test/experiment with msvcrt module functions
#
#
#

##############################################################################

#
# imports
#

import sys
import os
import argparse
import time
import serial
import serial.tools.list_ports
import msvcrt

##############################################################################

#
# globals
#

##############################################################################


def main():
    global progame

    ### parser = argparse.ArgumentParser()
        
    ### parser.add_argument('port',       help='COMn port name (e.g. COM1)')
    ### parser.add_argument('--speed',    help='baud rate',                           default=DEFAULT_SPEED)
    ### parser.add_argument('--ptimeout', help='port timeout in seconds (float)',     default=DEFAULT_PORT_TIMEOUT)
    ### parser.add_argument('--ktimeout', help='keyboard timeout in seconds (float)', default=DEFAULT_KEYBOARD_TIMEOUT)

    ### args = parser.parse_args()
    
    while True:
        while msvcrt.kbhit():
            c = msvcrt.getch()
            
            ### msvcrt.putch(c)
            
            print(type(c))
            print(c)
            
            cval = int(c[0])
            print(cval)
            
            time.sleep(0.5)

    ### ba[0] = 65
    ### msvcrt.putch(ba)        
    ### time.sleep(1.0)
        

##############################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file
