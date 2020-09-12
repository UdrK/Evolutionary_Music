from individual import Individual, IndividualBuilder
from music import *
from midiutil import MIDIFile
import pathlib
import subprocess

i = IndividualBuilder().from_chance(C5, MAJOR_SCALE, 8)
notes, durations, dynamics = i.generate()
i.save_genes("individual-genes.txt")

track = 0
channel = 0
time = 0   # In beats
tempo = 240  # In BPM

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track automatically created)
MyMIDI.addTempo(track, time, tempo)

for i in range(len(notes)):
    MyMIDI.addNote(track, channel, notes[i], time, durations[i], 127)
    time = time + 1

save_file = 'mid-output.mid'

with open("../outputs/{}".format(save_file), "wb") as output_file:
    MyMIDI.writeFile(output_file)

subprocess.call("C:/fluidsynth-x64/FluidR3_GM/play.bat {}{}".format(pathlib.Path().absolute().parent, "/outputs/{}".format(save_file)))

x = input('Program can continue after typing quit to exit fluidsynth ')
print(x)
