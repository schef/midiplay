#!/usr/bin/env python

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *

log = logging.getLogger('test_midiout')

logging.basicConfig(level=logging.DEBUG)

port = sys.argv[1] if len(sys.argv) > 1 else None
try:
    midiout, port_name = open_midiport(port, type_ = "output", use_virtual=True)
except (EOFError, KeyboardInterrupt):
    sys.exit()

note_on = [NOTE_ON, 60, 112] # channel 1, middle C, velocity 112
note_off = [NOTE_OFF, 60, 0]

time.sleep(5)
print("Sending NoteOn event.")
midiout.send_message(note_on)
time.sleep(1)
print("Sending NoteOff event.")
midiout.send_message(note_off)

del midiout
print("Exit.")
