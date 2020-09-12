import matplotlib.pyplot as plt
from individual import Individual, IndividualBuilder
from music import *

def plot_genes_matrix(matrix, x, title):
    rows = len(matrix)
    fig, axs = plt.subplots(rows, sharex=True)
    fig.suptitle(title)
    for i in range(len(axs)):
        axs[i].plot(x, matrix[i])
    plt.show()

def plot_genes(i):
    plot_genes_matrix(i.note_genes, i.possible_notes, 'Note genes')
    # plot_genes_matrix(i.duration_genes, i.possible_durations, 'Duration genes')
    # plot_genes_matrix(i.dynamic_genes, i.possible_dynamic, 'Dynamics genes')

i1 = IndividualBuilder().from_chance(C5, MAJOR_SCALE, 8)
i2 = IndividualBuilder().from_chance(C5, MAJOR_SCALE, 8)
i3 = IndividualBuilder().from_individuals(i1, i2)
plot_genes(i1)
plot_genes(i2)
plot_genes(i3)
