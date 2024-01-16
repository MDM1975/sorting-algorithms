def partition(array, leftmost_index, rightmost_index) -> int:
    # Set the pivot as the rightmost element in the subarray
    pivot = array[rightmost_index]

    # Initialize previous_index as one less than leftmost_index to help in swapping elements during partitioning
    previous_index = leftmost_index - 1

    # Traverse over the subarray from leftmost_index to rightmost_index
    for currentIndex in range(leftmost_index, rightmost_index):
        # If the current element is smaller than or equal to the pivot, increment previous_index and swap elements
        if array[currentIndex] <= pivot:
            previous_index += 1
            array[previous_index], array[currentIndex] = array[currentIndex], array[previous_index]

    # After the loop completes, place the pivot in its sorted position by swapping it with the element next to previous_index
    array[previous_index + 1], array[rightmost_index] = array[rightmost_index], array[previous_index + 1]

    # Return the pivots position, which is now at previous_index + 1
    return previous_index + 1


def quick_sort(array, leftmost_index, rightmost_index) -> None:
    # Only proceed with sorting if the subarray contains more than one element
    if leftmost_index < rightmost_index:
        # Partition the array such that all elements smaller than the pivot are to its left, and larger ones are to its right, then get the pivots final index
        partition_index = partition(array, leftmost_index, rightmost_index)

        # Recursively sort the left and right partitions of the array
        quick_sort(array, leftmost_index, partition_index - 1)
        quick_sort(array, partition_index + 1, rightmost_index)
