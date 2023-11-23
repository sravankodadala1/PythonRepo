from util import process_array
 
# Taking input from the user
input_array = numpy.array(input("Enter space-separated elements of the array: ").split(), float)

# Getting results from the utility function
floor_result, ceil_result, rint_result = process_array(input_array)

# Displaying the results
print("Floor Result:", floor_result)
print("Ceil Result:", ceil_result) 
print("Rint Result:", rint_result)
