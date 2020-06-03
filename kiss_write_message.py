#!/usr/bin/env python
"""
Reads & Prints KISS frames from a TCP Socket.

For use with programs like Dire Wolf.
"""

import aprs
import kiss2


def main():
    frame = aprs.Frame()
    frame.source = aprs.Callsign('ZR6AIC-14')
    frame.destination = aprs.Callsign('ZR6AIC-5')
    frame.path = [aprs.Callsign('WIDE1-1')]
    frame.info = '>Hello World!'

    ki = kiss2.TCPKISS(host='localhost', port=8001)
    ki.start()
    ki.write(frame.encode_ax25())


if __name__ == '__main__':
    main()

