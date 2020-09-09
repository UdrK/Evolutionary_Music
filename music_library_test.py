from music import *

# NOTES:
# Note(pitch, duration, dynamic, panning)
# pitch -> 0 - 127
# duration -> 4.0 - 0.25
# dynyamic -> forte, fortissimo, mezzo_forte, mezzo_piano, pianissimo, silent
# panning (i'm not interested in)

# RESTS:
# Rest(duration)
# duration -> same as with notes

# PHRASES:
# Phrase(start_time, instrument, tempo)
# start_time -> float
# instrument (i'm not interested in)
# tempo -> float
# Phrase() adds the phrase at the end of the last one
# to add a note to a phrase: phr.addNote(note)
# to add notes: phr.addNoteList(pitches_list, durations_list)
# in this list REST represents a rest in the pitches_list
# to add a CHORD one should make a list of the pitches in the chord
# chord = [C4, E4, G4] and add this to the phrase in the following way:
# phr.addChord(chord, duration, dynamic, panning)


phr = Phrase()

root = C4
scale_pitches = []
scale_durations = []

for i in MAJOR_SCALE:
    scale_pitches.append(root+i)
    scale_durations.append(QN)

scale_pitches.append(root+12)
scale_durations.append(QN)
# pitches = [E4, E4, E4, C4, REST, D4, D4, D4, B3]
# durations = [ENT, ENT, ENT, HN, QN, ENT, ENT, ENT, HN]

phr.addNoteList(scale_pitches, scale_durations)
phr.setTempo(120)
Play.midi(phr)