import numpy as np


def swap(input_list, index_one, index_two):
    tmp = input_list[index_one]
    input_list[index_one] = input_list[index_two]
    input_list[index_two] = tmp
    return input_list

# Check array size
    # If array length < 3:
        # If array length == 2:
            # if array[0] > array[1]
                # swap(array, 0, 1)
        # return array
# Pick a pivot point
# Partition the array
    # Go through the array and compare each value to the pivot point
        # If it is < pivot, put in array left
        # If it is >= pivot, put in array right
    # quick_sort left
    # quick_sort right