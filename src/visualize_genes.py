"""
This module contains functions to visualize random_individual's genes
"""

import matplotlib.pyplot as plt

def plot_genes_matrix(matrix, x, title):

    labels = []
    for i in range(len(matrix[0])):
        labels.append("{}-th note".format(i+1))

    for i in range(len(matrix)):
        plt.plot(x, matrix[i], label=labels[i])

    plt.title = title
    plt.legend()
    plt.xticks(x)
    plt.show()

def plot_genes(i):
    plot_genes_matrix(i.note_genes, i.possible_notes, 'Note genes')
    plot_genes_matrix(i.duration_genes, i.possible_durations, 'Duration genes')
