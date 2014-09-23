#!/usr/bin/env python
#
"""Shows how to open an output port and send MIDI events."""

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *

import pickle

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

#outfile = open('midiNotes.txt', 'w')
#outfile.write("\n".join(midiNotes))
#for item in midiNotes:
#    outfile.write("%s\n" % item)

with open("midiNotes.txt", 'wb') as f:
    pickle.dump(midiNotes, f)

print("Exit.")
