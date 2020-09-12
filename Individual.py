"""
This class follows the approach:
The genetic information is relative to the probabilities of picking each note from a predetermined scale
 ith predetermined root

Basically it will be a Matrix m x n, with m the number of notes in the musical phrase and n the number
of notes in the scale.

A value Matrix[i, j] will be the probability that the i-th note is the j-th note in the scale of the root note
"""

from music import *
import random

class Individual:

    """
        initializes individuals genes

        Parameters:
            root: int (0-127) represents the root note
            scale: list of int represents the absolute intervals from the root
            phrase_length: int represents how many notes should be in the phrase
    """
    def __init__(self, root, scale, phrase_length):
        # 3 octaves of the scale
        self.root = root
        self.phrase_length = phrase_length
        self.possible_notes = [root+j+i for j in [-12, 0, 12] for i in scale]
        self.possible_durations = [WN, DHN, HN, DQN, QN, DEN, EN, DSN, SN]
        self.possible_dynamic = [FF, F, MF, MP, P, PP]

        # initializing empty notes probabilities matrix
        self.note_genes = [[0 for m in range(len(self.possible_notes))] for m in range(phrase_length)]
        # initializing random notes probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for m in range(len(self.possible_notes))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(self.possible_notes)):
                self.note_genes[i][j] = random_probabilities[j]


        # initializing empty duration probabilities matrix
        self.duration_genes = [[0 for m in range(len(self.possible_durations))] for m in range(phrase_length)]
        # initializing random duration probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for m in range(len(self.possible_durations))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(self.possible_durations)):
                self.duration_genes[i][j] = random_probabilities[j]


        # initializing empty dynamics probabilities matrix
        self.dynamic_genes = [[0 for m in range(len(self.possible_dynamic))] for m in range(phrase_length)]
        # initializing random dynamics probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 100) for m in range(len(self.possible_dynamic))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(self.possible_dynamic)):
                self.dynamic_genes[i][j] = random_probabilities[j]

    """
        returns individual generated following its genes
    """
    def generate(self):

        notes = []
        durations = []
        dynamics = []

        for i in range(self.phrase_length):
            pitch = random.choices(self.possible_notes, self.note_genes[i])
            duration = random.choices(self.possible_durations, self.duration_genes[i])
            dynamic = random.choices(self.possible_dynamic, self.dynamic_genes[i])

            notes.append(pitch[0])
            durations.append(duration[0])
            dynamics.append(dynamic[0])

        return notes, durations, dynamics



    """
        saves genes in .txt file
        Parameters:
            filename: string name of the file used to save the matrixes of probabilities 
    """
    def save_genes(self, filename):

        note_matrix_string = self.__matrix_to_string(self.note_genes)
        duration_matrix_string = self.__matrix_to_string(self.duration_genes)
        dynamic_matrix_string = self.__matrix_to_string(self.dynamic_genes)

        with open(filename, "w") as output_file:
            output_file.write(note_matrix_string)
            output_file.write("\n")
            output_file.write(duration_matrix_string)
            output_file.write("\n")
            output_file.write(dynamic_matrix_string)
    """
        reads genes saved in .txt file
        Parameters:
            filename: string name of the file used to save the matrixes of probabilities 
    """
    def read_genes(self, filename):
        with open(filename, "r") as input_file:
            note_matrix_string = input_file.readline()
            duration_matrix_string = input_file.readline()
            dynamic_matrix_string = input_file.readline()

        self.note_genes = self.__string_to_matrix(note_matrix_string)
        self.duration_genes = self.__string_to_matrix(duration_matrix_string)
        self.dynamic_genes = self.__string_to_matrix(dynamic_matrix_string)


    def __matrix_to_string(self, matrix):

        string = "["
        for i in range(len(matrix)):
            string += "["
            for j in range(len(matrix[0])):
                string += "{},".format(matrix[i][j])
            string += "],"
        string += "]"

        return string

    def __string_to_matrix(self, string):
        string = string[2:-5]
        rows = string.split(',],[')
        matrix = [[0 for m in range(len(rows[0].split(',')))] for m in range(len(rows))]
        for i in range(len(rows)):
            numbers = rows[i].split(',')
            for j in range(len(numbers)):
                matrix[i][j] = numbers[j]

        return matrix