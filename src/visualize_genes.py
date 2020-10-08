"""
This module contains functions to visualize random_individual's genes
"""

import matplotlib.pyplot as plt

def plot_genes_matrix(matrix, x, title, labels=None):
    edge = max(max(matrix[0]), max(matrix[0]))
    edge = edge + 0.5 * edge
    edge = [edge]*len(x)
    matrix.append(edge)
    if labels:
        labels.append('edge')


    sum = []
    for i in range(len(x)):
        sum.append(matrix[0][i]+matrix[1][i])
    matrix.append(sum)
    if labels:
        labels.append('i1+i2')

    for i in range(len(matrix)):
        if labels:
            plt.plot(x, matrix[i], label=labels[i])
        else:
            plt.plot(x, matrix[i])

    plt.legend()
    plt.xticks(x)
    plt.show()

def plot_first_gene_from_individuals(i1, i2, i3):

    matrix = []
    x = i1.possible_notes
    matrix.append(i1.note_genes[0])
    matrix.append(i2.note_genes[0])
    matrix.append(i3.note_genes[0])
    labels = ['i1', 'i2', 'i3']
    plot_genes_matrix(matrix, x, 'Note genes', labels)

def plot_genes(i):
    plot_genes_matrix(i.note_genes, i.possible_notes, 'Note genes')
    plot_genes_matrix(i.duration_genes, i.possible_durations, 'Duration genes')
