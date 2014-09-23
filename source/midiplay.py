# -*- coding: utf-8 -*-
# midiplay functions
"""

Collection of midiplay functions for handling MIDI I/O.

"""

import pickle

def list2file(myList, myFile):    # write list to a file
    """
    list2file converts a list[ [timestamp, [statusByte, dataByte]], ...] to a file.
    """
    with open(myFile, 'wb') as f:
        pickle.dump(myList, f)
    #for x in myList:
    #    print (x)


def file2list(myFile): # read from file and load to list
    """
    file2list converts a file back to list[ [timestamp, [statusByte, dataByte]], ...].
    """
    with open(myFile, 'rb') as f:
        myList = pickle.load(f)
    return(myList)

