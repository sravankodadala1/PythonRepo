import numpy
 
def np_min_max(array):
    ar = numpy.array(array)
    return max(numpy.min(ar, axis=1))
