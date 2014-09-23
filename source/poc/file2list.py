#!/usr/bin/env python
import pickle

with open("midiNotes.txt", 'rb') as f:
    midiNotes = pickle.load(f)

print("Exit.")
