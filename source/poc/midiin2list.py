#!/usr/bin/env python

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiport

log = logging.getLogger('test_midiin_callback')

logging.basicConfig(level=logging.DEBUG)

midiNotes = []

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        #print na STDOUT
        #print("@%0.6f %r" % (deltatime, message))
        #float is not limited but could be to 6 zero points or less if problems will accure.
        midiNotes.append([deltatime, message])


port = sys.argv[1] if len(sys.argv) > 1 else None
try:
    midiin, port_name = open_midiport(port, use_virtual = True)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Attaching MIDI input callback handler.")
midiin.set_callback(MidiInputHandler(port_name))

print("Entering main loop. Press Control-C to exit.")
try:
    # just wait for keyboard interrupt in main thread
    while True:
        time.sleep(3)
        #print (midiNotes)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin
