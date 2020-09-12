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

class IndividualBuilder:

    @staticmethod
    def from_chance(root, scale, phrase_length):
        ind = Individual()
        # 3 octaves of the scale
        ind.root = root
        ind.scale = scale.copy()
        ind.phrase_length = phrase_length
        ind.possible_notes = [root+j+i for j in [-12, 0, 12] for i in scale]
        ind.possible_durations = [WN, DHN, HN, DQN, QN, DEN, EN, DSN, SN]
        ind.possible_dynamic = [FF, F, MF, MP, P, PP]

        # initializing empty notes probabilities matrix
        ind.note_genes = [[0 for m in range(len(ind.possible_notes))] for m in range(phrase_length)]
        # initializing random notes probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 10000) for m in range(len(ind.possible_notes))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(ind.possible_notes)):
                ind.note_genes[i][j] = random_probabilities[j]


        # initializing empty duration probabilities matrix
        ind.duration_genes = [[0 for m in range(len(ind.possible_durations))] for m in range(phrase_length)]
        # initializing random duration probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 10000) for m in range(len(ind.possible_durations))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(ind.possible_durations)):
                ind.duration_genes[i][j] = random_probabilities[j]


        # initializing empty dynamics probabilities matrix
        ind.dynamic_genes = [[0 for m in range(len(ind.possible_dynamic))] for m in range(phrase_length)]
        # initializing random dynamics probabilities matrix
        for i in range(phrase_length):

            # n = len(possible_notes) random numbers such that their sum is == 1
            # generate n random numbers, divide each by their sum
            random_probabilities = [random.randint(0, 10000) for m in range(len(ind.possible_dynamic))]
            total = sum(random_probabilities)
            random_probabilities = [m/total for m in random_probabilities]

            for j in range(len(ind.possible_dynamic)):
                ind.dynamic_genes[i][j] = random_probabilities[j]

        return ind

    @staticmethod
    def from_individuals(individual1, individual2):

        if not individual1.root  == individual2.root:
            return None
        if not individual1.scale == individual2.scale:
            return None
        if not individual1.phrase_length == individual2.phrase_length:
            return None

        ind = Individual()
        ind.root = individual1.root
        ind.scale = individual1.scale.copy()
        ind.phrase_length = individual1.phrase_length
        ind.possible_notes = individual1.possible_notes.copy()
        ind.possible_durations = individual1.possible_durations.copy()
        ind.possible_dynamic = individual1.possible_dynamic.copy()

        ind.note_genes = []
        ind.duration_genes = []
        ind.dynamic_genes = []

        for i in range(len(individual1.note_genes)):
            ind.note_genes.append(Individual._sum_genes(individual1.note_genes[i], individual2.note_genes[i]))

        for i in range(len(individual1.duration_genes)):
            ind.duration_genes.append(Individual._sum_genes(individual1.duration_genes[i], individual2.duration_genes[i]))

        for i in range(len(individual1.dynamic_genes)):
            ind.dynamic_genes.append(Individual._sum_genes(individual1.dynamic_genes[i], individual2.dynamic_genes[i]))

        return ind

class Individual:

    """
        initializes individuals genes

        Parameters:
            root: int (0-127) represents the root note
            scale: list of int represents the absolute intervals from the root
            phrase_length: int represents how many notes should be in the phrase
    """
    def __init__(self):
        self.root = None
        self.scale = None
        self.phrase_length = None
        self.possible_notes = None
        self.possible_durations = None
        self.possible_dynamic = None
        self.note_genes = None
        self.duration_genes = None
        self.dynamic_genes = None

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

        note_matrix_string = Individual._matrix_to_string(self.note_genes)
        duration_matrix_string = Individual._matrix_to_string(self.duration_genes)
        dynamic_matrix_string = Individual._matrix_to_string(self.dynamic_genes)

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

        self.note_genes = Individual._string_to_matrix(note_matrix_string)
        self.duration_genes = Individual._string_to_matrix(duration_matrix_string)
        self.dynamic_genes = Individual._string_to_matrix(dynamic_matrix_string)

    """
        takes 2 gene arrays and returns a new array with higher probabilities where both given arrays have higher 
        probabilities
        Parameters:
             gene_array_1, gene_array_1: arrays of floats, they represent a distribution (sum(array)==1)
    """
    @staticmethod
    def _sum_genes(gene_array_1, gene_array_2):
        new_gene_array = []

        for i in range(len(gene_array_1)):
            if gene_array_1[i] + gene_array_2[i] >= max(max(gene_array_1), max(gene_array_2)):
                new_gene_array.append(gene_array_1[i] + gene_array_2[i])
            else:
                new_gene_array.append(min(gene_array_1[i], gene_array_2[i]))

        total = sum(new_gene_array)

        for i in range(len(new_gene_array)):
            new_gene_array[i] = new_gene_array[i]/total

        return new_gene_array

    @staticmethod
    def _matrix_to_string(matrix):

        string = "["
        for i in range(len(matrix)):
            string += "["
            for j in range(len(matrix[0])):
                string += "{},".format(matrix[i][j])
            string += "],"
        string += "]"

        return string

    @staticmethod
    def _string_to_matrix(string):
        string = string[2:-5]
        rows = string.split(',],[')
        matrix = [[0 for m in range(len(rows[0].split(',')))] for m in range(len(rows))]
        for i in range(len(rows)):
            numbers = rows[i].split(',')
            for j in range(len(numbers)):
                matrix[i][j] = numbers[j]

        return matrix