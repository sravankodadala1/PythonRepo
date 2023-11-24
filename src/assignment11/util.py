import numpy


def process_array(input_array):
    numpy.set_printoptions(sign=' ') 
    floor_result = numpy.floor(input_array)
    ceil_result = numpy.ceil(input_array)
    rint_result = numpy.rint(input_array)

    return floor_result, ceil_result, rint_result


