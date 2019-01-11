#
# @(!--#) @(#) serialterm.py, version 006, 09-january-2019
#
# a simple serial terminal emulator (and I *REALLY* mean simple!)
#
# Platform is Windows only for two reasons:
#   (1) it uses msvcrt console I/O keyboard functions
#   (2) on UNIX/Linux use cu or tip or something else instead
#
# Links:
#
#    https://docs.python.org/3/howto/argparse.html
#    https://pyserial.readthedocs.io/en/latest/
#    https://docs.python.org/3.7/library/msvcrt.html
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

DEFAULT_SPEED            = 115200
DEFAULT_PORT_TIMEOUT     = 0.01
DEFAULT_KEYBOARD_TIMEOUT = 0.01
DEFAULT_ESCAPE_CHAR      = '~'

BUFFER_SIZE = 128

##############################################################################

def listcomports():
    ports = serial.tools.list_ports.comports()
    
    comports = []
    
    for lpi in ports:
        comport = lpi.device
        
        if len(comport) < 4:
            continue
        
        if len(comport) > 6:
            continue

        if comport[0:3] != 'COM':
            continue
        
        if not comport[3:].isdigit():
            continue
        
        comports.append(comport)
        
    if len(comports) == 0:
        print('No COMn serial ports found')
    elif len(comports) == 1:
        print('{} is the only COMn style serial port'.format(comports[0]))
    else:
        print('Available COMn style serial ports are:')
        for i in range(4,7):
            for c in comports:
                if len(c) == i:
                    print('    {}'.format(c))   
            
    return

##############################################################################

def processescape(c):
    print('')
    print('-------------------------')
    print('Locally processing an escape character')
    print(type(c))
    print(c)
    print('-------------------------')
    
    return

##############################################################################

def serialterm(ser, keyboardtimeout, capturefilehandle, captureflag, escape):
    ba = bytearray(1)
    
    escapechar    = bytearray(1)
    escapechar[0] = ord(escape)
    
    periodchar    = bytearray(1)
    periodchar[0] = ord('.')
    
    captureon    = bytearray(1)
    captureon[0] = ord('c')

    captureoff    = bytearray(1)
    captureoff[0] = ord('C')

    while True:
        # read from the port and display any characters
        while True:
            received = ser.read(BUFFER_SIZE)
            
            if len(received) == 0:
                break
            
            for c in received:
                ba[0] = c
                msvcrt.putch(ba)
                
            if capturefilehandle != None:
                if captureflag:
                    capturefilehandle.write(received)
                    capturefilehandle.flush()
            
        # read characters
        while msvcrt.kbhit():
            c = msvcrt.getch()
            
            if c == escapechar:
                nextc = msvcrt.getch()
                
                if nextc == escapechar:
                    ser.write(nextc)
                elif nextc == periodchar:
                    print('')
                    print('Exiting as user has typed the {}{} sequence'.format(chr(escapechar[0]), chr(periodchar[0])))
                    return
                elif nextc == captureon:
                    captureflag = True
                elif nextc == captureoff:
                    captureflag = False
                    if capturefilehandle != None:
                        capturefilehandle.flush()
                else:
                    processescape(c)
            else:
                ser.write(c)
                time.sleep(keyboardtimeout)

##############################################################################

def main():
    global progame

    parser = argparse.ArgumentParser()
        
    parser.add_argument('port',       help='COMn port name (e.g. "COM1") or "list" to show available ports')
    parser.add_argument('--speed',    help='baud rate',                           default=DEFAULT_SPEED)
    parser.add_argument('--capture',  help='file name to capture output',         nargs=1)
    parser.add_argument('--defer',    help='defer capture output',                action='store_true')
    parser.add_argument('--escape',   help='escape character',                    default=DEFAULT_ESCAPE_CHAR)
    parser.add_argument('--ptimeout', help='port timeout in seconds (float)',     default=DEFAULT_PORT_TIMEOUT)
    parser.add_argument('--ktimeout', help='keyboard timeout in seconds (float)', default=DEFAULT_KEYBOARD_TIMEOUT)

    args = parser.parse_args()
    
    port = args.port
    
    if port.lower() == 'list':
        listcomports()
        sys.exit(1)
    
    speed = int(args.speed)

    porttimeout = float(args.ptimeout)

    keyboardtimeout = float(args.ptimeout)
    
    try:
        ser = serial.Serial(port.upper(), speed, timeout=porttimeout)
    except serial.serialutil.SerialException:
        print('{}: problem opening COM port "{}"'.format(progname, port), file=sys.stderr)
        sys.exit(1)

    capturefilehandle = None

    if args.capture:
        if len(args.capture) == 1:
            try:
                capturefilehandle = open(args.capture[0], 'wb')
            except IOError:
                print('{}: problem opening capture file "{}" for writing'.format(progname, args.capture[0]), file=sys.stderr)
                sys.exit(1)
    
    if args.defer:
        captureflag = False
    else:
        captureflag = True
    
    escape = args.escape[0]
                    
    serialterm(ser, keyboardtimeout, capturefilehandle, captureflag, escape)
    
    if capturefilehandle != None:
        capturefilehandle.flush()
        capturefilehandle.close()
        
    return 0

##############################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file
