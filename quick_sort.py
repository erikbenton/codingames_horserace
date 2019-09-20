def swap(input_list, index_one, index_two):
    tmp = input_list[index_one]
    input_list[index_one] = input_list[index_two]
    input_list[index_two] = tmp
    return input_list


def partition(input_list, left_index, right_index):
    # Pick a pivot point
    pivot = input_list[right_index]
    left = left_index - 1
    for right in range(left_index, right_index):
        val = input_list[right]
        if val <= pivot:
            left += 1
            swap(input_list, left, right)
    # Put pivot in correct index (left + 1) once done
    swap(input_list, left + 1, right_index)
    return left + 1


def quick_sort(input_list, left_index, right_index):
    # Check array size
    if (right_index - left_index) < 2:
        if (right_index - left_index) == 1:
            if input_list[left_index] > input_list[right_index]:
                swap(input_list, right_index, left_index)
        return input_list
    # Partition the array and get the pivot's nex index
    pivot_index = partition(input_list, left_index, right_index)
    # Sort the left side of the array
    quick_sort(input_list, left_index, pivot_index - 1)
    # Sort the right side of the array
    quick_sort(input_list, pivot_index + 1, right_index)
    return input_list


a = [3, 5, 1, 6, 7, 2, 5, 8, 5, 7]
quick_sort(a, 0, len(a) - 1)
print(str(a))
