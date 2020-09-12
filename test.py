from music import *
from midiutil import MIDIFile
import subprocess

degrees  = [C4, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = [0.25,0.25,0.25,2,0.25,0.25,0.25,2]  # In beats
tempo    = 120  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI.addTempo(track,time, tempo)

for i in range(len(degrees)):
    MyMIDI.addNote(track, channel, degrees[i], time, duration[i], volume)
    time = time + 1

with open("mid-output.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

subprocess.call(["C:/fluidsynth-x64/FluidR3_GM/play.bat"])

x = input('Program can continue after typing quit to exit fluidsynth ')
print(x)
