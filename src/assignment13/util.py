import numpy

def linear_algebra(matrix):
    numpy.set_printoptions(legacy='1.13')
    return numpy.linalg.det(matrix)
