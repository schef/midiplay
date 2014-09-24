# -*- coding: utf-8 -*-
# midiplay functions
"""

Collection of midiplay functions for handling MIDI I/O.

"""

import pickle
import time
import rtmidi
from rtmidi.midiutil import open_midiport
import sys

acceptNotes = [128, 129, 130, 131, 144, 145, 146, 147]

def list2file(myList, myFile):    # write list to a file
    """
    list2file converts a list[ [timestamp, [statusByte, dataByte]], ...] to a file.
    """
    with open(myFile, 'wb') as f:
        pickle.dump(myList, f)
    print ("Saved to ", myFile)
    #for x in myList:
    #    print (x)


def file2list(myFile): # read from file and load to list
    """
    file2list converts a file back to list[ [timestamp, [statusByte, dataByte]], ...].
    """
    try:
        with open(myFile, 'rb') as f:
            myList = pickle.load(f)
        return(myList)
    except IOError:
        print("An error occured trying to read the file.")

def list2stdout(myList, tempo=1): #print list to stdout
    """
    list2stdout prints a list[ [timestamp, [statusByte, dataByte]], ...] to stdout.
    """
    try:
        for i in range(len(myList)):
            time.sleep(myList[i][0]*tempo)
            print (myList[i][1])
    except KeyboardInterrupt:
        print('Song aborted by you.')

def list2midiout(self, myList, tempo=1): #send message from list to midiout
    """
    list2midiout sends contents of list[ [timestamp, [statusByte, dataByte]], ...] to midiout.
    """
    try:
        for i in range(len(myList)):
            time.sleep(myList[i][0]*tempo)
            self.send_message(myList[i][1])
            print(myList[i][1])
        #TODO:ugasi diodu
        panic(self)
        print("Song ended!")
        return(0)
    except KeyboardInterrupt:
        print('Song aborted by you.')
        print('Sending panic!')
        panic(self)
        return(0)

def panic(self):
    """
    Status Bytes: 176-191
    Control Number: 123 [Channel Mode Message] All Notes Off
    Value: 0
    """
    for i in range(176, 192):
        self.send_message([i, 123, 0])

def midiin2list(client_name, port_name):
    while client_name.get_message():
        pass
    myList = []
    print('Recording started.')
    try:
        timer = time.time()
        while True:
            msg = client_name.get_message()
            if msg:
                message, deltatime = msg 
                timer += deltatime
                #print("[%s] @%0.6f %r" % (port_name, timer, message))
                if message[0] in acceptNotes:
                    myList.append([deltatime, message])
                    print(message)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('Recording stoped')
    return(myList)
