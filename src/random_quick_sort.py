import random


def partition(array, leftmost_index, rightmost_index) -> int:
    # Establish the pivot as the rightmost element in the subarray
    pivot = array[rightmost_index]
    # Initialize previous_index as one less than leftmost_index to facilitate element swapping during partitioning
    previous_index = leftmost_index - 1

    # Traverse over the subarray from leftmost_index to rightmost_index
    for current_index in range(leftmost_index, rightmost_index):
        # If the current element is less than or equal to the pivot, increment previous_index and swap its element with current_index element
        if array[current_index] <= pivot:
            previous_index += 1
            array[previous_index], array[current_index] = array[current_index], array[previous_index]

    # After the traversal, place the pivot in its correct sorted position by swapping it with the element next to previous_index
    array[previous_index + 1], array[rightmost_index] = array[rightmost_index], array[previous_index + 1]
    # Return the final position of the pivot, which is previous_index + 1
    return previous_index + 1


def randomized_partition(array, leftmost_index, rightmost_index) -> int:
    # Select a random pivot index between leftmost_index and rightmost_index, inclusive
    random_index = random.randint(leftmost_index, rightmost_index)
    # Swap the randomly selected pivot with the rightmost element of the subarray, which will be the new pivot
    array[random_index], array[leftmost_index] = array[rightmost_index], array[random_index]
    # Perform the standard partitioning process on this subarray and return the pivots final position
    return partition(array, leftmost_index, rightmost_index)


def randomized_quicksort(array, leftmost_index, rightmost_index) -> None:
    # Only proceed with sorting if the subarray contains more than one element
    if leftmost_index < rightmost_index:
        # Partition the array around a randomly selected pivot.
        # All elements smaller than the pivot are moved to its left, and larger ones to its right.
        partition_index = randomized_partition(array, leftmost_index, rightmost_index)
        # Recursively sort the partitions to the left and right of the pivot
        randomized_quicksort(array, leftmost_index, partition_index - 1)
        randomized_quicksort(array, partition_index + 1, rightmost_index)
