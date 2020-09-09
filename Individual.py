"""
This class follows the approach:
The genetic information is relative to the probabilities of picking each note from a predetermined scale
 ith predetermined root

Basically it will be a Matrix m x n, with m the number of notes in the musical phrase and n the number
of notes in the scale.

A value Matrix[i, j] will be the probability that the i-th note is the j-th note in the scale of the root note
"""

import random

class Individual:

    """
        Parameters:
            root: int (0-127) represents the root note
            scale: list of int represents the absolute intervals from the root
            phrase_length: int represents how many notes should be in the phrase
    """
    def __init__(self, root, scale, phrase_length):
        # 3 octaves of the scale
        self.root = root
        self.possible_notes = [root+j+i for j in [-12, 0, 12] for i in scale]
        self.possible_durations = [WN, DHN, HN, DQN, QN, DEN, EN, DSN, SN]
        self.possible_dynamic = [FF, F, MF, MP, P, PP]
        print(possible_notes)

        # initializing empty notes probabilities matrix
        self.note_genes = [[0 for i in range(phrase_length)] for j in range(len(self.possible_notes))]
        # initializing random notes probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for j in range(len(self.possible_notes))]
            total = sum(random_probabilities)
            random_probabilities = [i/total for i in random_probabilities]

            for j in range(len(self.possible_notes)):
                self.note_genes[i][j] = random_probabilities[j]


        # initializing empty duration probabilities matrix
        self.duration_genes = [[0 for i in range(phrase_length)] for j in range(len(self.possible_durations))]
        # initializing random duration probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for j in range(len(self.possible_durations))]
            total = sum(random_probabilities)
            random_probabilities = [i/total for i in random_probabilities]

            for j in range(len(self.possible_durations)):
                self.duration_genes[i][j] = random_probabilities[j]


        # initializing empty dynamics probabilities matrix
        self.dynamic_genes = [[0 for i in range(phrase_length)] for j in range(len(self.possible_dynamic))]
        # initializing random dynamics probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for j in range(len(self.possible_dynamic))]
            total = sum(random_probabilities)
            random_probabilities = [i/total for i in random_probabilities]

            for j in range(len(self.possible_durations)):
                self.dynamic_genes[i][j] = random_probabilities[j]
