def partition(array, leftmost_index, rightmost_index) -> int:
    # Set pivot as the rightmost element of the subarray
    pivot = array[rightmost_index]

    # Initialize the previous index to one less than the leftmost_index, to help in swapping elements
    previous_index = leftmost_index - 1

    # Iterate over the subarray from leftmost_index to rightmost_index
    for current_index in range(leftmost_index, rightmost_index):
        # If the current element is less than or equal to the pivot, increment the previous_index and swap the elements
        if array[current_index] <= pivot:
            previous_index += 1
            array[previous_index], array[current_index] = array[current_index], array[previous_index]

    # After iteration, place the pivot in its sorted position by swapping it with the element next to previous_index
    array[previous_index + 1], array[rightmost_index] = array[rightmost_index], array[previous_index + 1]

    # Return the pivot's position
    return previous_index + 1


def median_of_three_partition(array, leftmost_index, rightmost_index) -> int:
    # Determine the median index of the leftmost, rightmost, and middle elements of the array
    median_index = get_median_index(array, leftmost_index, rightmost_index)

    # Move the median to the rightmost_index position, and use it as pivot for the partition function
    array[median_index], array[rightmost_index] = array[rightmost_index], array[median_index]

    # Call partition function and return the pivot's final position
    return partition(array, leftmost_index, rightmost_index)


def get_median_index(array, leftmost_index, rightmost_index) -> int:
    # Calculate the index of the middle element
    middle_index = (leftmost_index + rightmost_index) // 2

    # Store the values of the leftmost, middle, and rightmost elements
    leftmost_value = array[leftmost_index]
    middle_value = array[middle_index]
    rightmost_value = array[rightmost_index]

    # Determine and return the index of the median value amongst leftmost_value, middle_value, and rightmost_value
    if (leftmost_value <= middle_value <= rightmost_value) or (rightmost_value <= middle_value <= leftmost_value):
        return middle_index
    if (middle_value <= leftmost_value <= rightmost_value) or (rightmost_value <= leftmost_value <= middle_value):
        return leftmost_index
    else:
        return rightmost_index


def median_of_three_sort(array, leftmost_index, rightmost_index) -> None:
    # Proceed with the sort only if the subarray has more than one element
    if leftmost_index < rightmost_index:
        # Get the partition index using the median of three method, then recursively sort the left and right subarrays
        partition_index = median_of_three_partition(array, leftmost_index, rightmost_index)
        median_of_three_sort(array, leftmost_index, partition_index - 1)
        median_of_three_sort(array, partition_index + 1, rightmost_index)
