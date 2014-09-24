#!/usr/bin/env python
#
#
"""main program"""

import midiplay
import logging
import sys
import time
import signal, os

import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *

log = logging.getLogger('test_midiout')

logging.basicConfig(level=logging.DEBUG)

signal_rec = 0
signal_play = 0

def rec_handler(signum, frame):
    print('rec signal', signum)
    global signal_rec
    global signal_play
    if signal_play:
        print ("WARNING! still playing")
    else:
        if signal_rec == 0:
            signal_rec = 1
            #TODO:upali diodu
            pjesma = midiplay.midiin2list(midiin, 'in')
            midiplay.list2file(pjesma, 'novapjesma.txt')
        elif signal_rec == 1:
            signal_rec = 0
            #TODO:ugasi diodu
            raise KeyboardInterrupt

def play_handler(signum, frame):
    print('play signal', signum)
    global signal_play
    global siganl_rec
    #TODO:load pjesma on startup
    try:
        pjesma
    except NameError:
        pjesma = midiplay.file2list('novapjesma.txt')
    if signal_rec:
        print ("WARNING! still recording")
    else:
        if signal_play == 0:
            signal_play = 1
            #TODO:upali diodu
            signal_play = midiplay.list2midiout(midiout, pjesma)
            #print("islo je")
        elif signal_play == 1:
            signal_play = 0
            raise KeyboardInterrupt

signal.signal(signal.SIGRTMIN, rec_handler)
signal.signal(signal.SIGRTMAX, play_handler)

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        #print na STDOUT
        if set(message) ==  set(play):
            print ("PLAY button pushed")
            os.kill(os.getpid(), 64)
        elif set(message) == set(rec):
            print ("REC button pushed")
            os.kill(os.getpid(), 34)
        #print("@%0.6f %r" % (deltatime, message))

play = [148, 36, 100]
rec = [148, 37, 100]

port = sys.argv[1] if len(sys.argv) > 1 else None
try:
    midiout, port_name_out = open_midiport(port, type_ = "output", use_virtual=True, client_name='midiplay', port_name='out')
    midiin, port_name_in = open_midiport(port, use_virtual=True, client_name='midiplay', port_name='in')
    midicall, port_name_call = open_midiport(port, use_virtual = True, client_name='midiplay', port_name='callback')
except (EOFError, KeyboardInterrupt):
    sys.exit()

#pjesma = midiplay.file2list('midiNotes.txt')


midicall.set_callback(MidiInputHandler(port_name_call))

try:
#    new_song = midiplay.midiin2list(midiin,port_name_in)
    print ("Ready, Waiting...")
    while True:
        #print("signal_play", signal_play )
        #print("signal_rec", signal_rec)
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
finally:
    print("\nSignal Interrupt Recieved, Program Exit Successful")
    midiout.close_port()
    del midiout
    midiin.close_port()
    del midiin
    midicall.close_port()
    del midicall
