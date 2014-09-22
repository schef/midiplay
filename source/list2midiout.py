#!/usr/bin/env python
#
# test_midiout.py
#
"""Shows how to open an output port and send MIDI events."""

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *

log = logging.getLogger('test_midiout')

logging.basicConfig(level=logging.DEBUG)

midiNotes = [
             [0.0, [159, 52, 100]],
             [0.20660499999999998, [143, 52, 0]],
             [0.13863999999999999, [159, 53, 100]],
             [0.22694699999999998, [143, 53, 0]],
             [0.178113, [159, 55, 100]],
             [2, [143, 55, 0]],
             [3, [159, 57, 100]],
             [0.197328, [143, 57, 0]],
             [0.12386599999999999, [159, 55, 100]],
             [0.162526, [143, 55, 0]],
             [0.11900799999999999, [159, 53, 100]],
             [0.172646, [143, 53, 0]],
             [0.178134, [159, 52, 100]],
             [0.167618, [143, 52, 0]]
            ]

port = sys.argv[1] if len(sys.argv) > 1 else None
try:
    midiout, port_name = open_midiport(port, type_ = "output", use_virtual=True)
except (EOFError, KeyboardInterrupt):
    sys.exit()

note_on = [NOTE_ON, 60, 112] # channel 1, middle C, velocity 112
note_off = [NOTE_OFF, 60, 0]

#time.sleep(5)
print("Sending NoteOn event.")
for i in range(len(midiNotes)):
    time.sleep(midiNotes[i][0])
    print (midiNotes[i][1])
    midiout.send_message(midiNotes[i][1])
#time.sleep(1)
#print("Sending NoteOff event.")
#midiout.send_message(note_off)

del midiout
print("Exit.")
