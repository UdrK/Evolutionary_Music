from individual import Individual, IndividualBuilder
from music import *
from midiutil import MIDIFile
import pathlib
import subprocess


def play_generated(notes, durations, dynamics, save_file):
    track = 0
    channel = 0
    time = 0  # In beats
    tempo = 240  # In BPM

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track automatically created)
    MyMIDI.addTempo(track, time, tempo)

    for i in range(len(notes)):
        MyMIDI.addNote(track, channel, notes[i], time, durations[i], 127)   # dynamics should go in place of 127
        time = time + 1

    with open("../outputs/{}".format(save_file), "wb") as output_file:
        MyMIDI.writeFile(output_file)

    subprocess.call("C:/fluidsynth-x64/FluidR3_GM/play.bat {}{}".format(pathlib.Path().absolute().parent, "/outputs/{}".format(save_file)))


def save_generated(notes, duration, save_file):
    with open("../outputs/{}".format(save_file), "w") as output_file:
        for i in range(len(notes)):
            output_file.write(' {}_{} '.format(notes[i], duration[i]))


individuals = []

root = C5
scale = MAJOR_SCALE
phrase_length = 8

for i in range(8):
    ind = IndividualBuilder.from_chance(root, scale, phrase_length)
    individuals.append({
        'individual': ind,
        'score': None
    })

save_file = 0
stop = 'y'
while stop == 'y':
    for i in range(len(individuals)):
        notes, durations, dynamics = individuals[i]['individual'].generate()
        play_generated(notes, durations, dynamics, 'output_midi_{}.mid'.format(save_file))
        save_generated(notes, durations, 'output_notes_{}.txt'.format(save_file))
        save_file += 1
        score = input('Assign a score to this composition: ')
        individuals[i]['score'] = score

    individuals = sorted(individuals, key=lambda a: a['score'], reverse=True)

    new_individuals = []
    j = 0
    for i in range(0, len(individuals), 2):
        if i < len(individuals)//2:
            new_individuals.append({
                'individual': IndividualBuilder.from_individuals(individuals[i]['individual'], individuals[i+1]['individual']),
                'score': -1
            })
        else:
            if j < len(new_individuals):
                individuals[i] = new_individuals[j]
                j += 1
            else:
                individuals[i] = IndividualBuilder.from_chance(root, scale, phrase_length)

    stop = input('Keep going? ')

individuals = sorted(individuals, key=lambda a: a['score'], reverse=True)
for i in range(len(individuals)):
    individuals[i]['individual'].save_genes('outputs/genes_{}.txt'.format(i))
