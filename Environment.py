from Individual import Individual
from music import *

i = Individual(C5, MAJOR_SCALE, 8)
melody = i.generate()
Play.midi(melody)
