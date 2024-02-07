def merge_sort(array, start_index, end_index) -> None:
    # If the array contains more than one element, proceed with the sort
    if start_index < end_index:
        # Calculate the middle index for dividing the array into two halves
        middle_index = (start_index + end_index) // 2

        # Recursively sort the left and right halves of the array
        merge_sort(array, start_index, middle_index)
        merge_sort(array, middle_index + 1, end_index)

        # Merge the sorted halves back together
        merge(array, start_index, middle_index, end_index)


def merge(array, start_index, middle_index, end_index) -> None:
    # Determine the lengths of the two subarrays to be merged
    left_arr_length = middle_index - start_index + 1
    right_arr_length = end_index - middle_index

    # Initialize empty arrays for the left and right subarrays
    left_array = []
    right_array = []

    # Populate the left subarray with the first half of the array
    for i in range(0, left_arr_length):
        left_array.append(array[start_index + i])

    # Populate the right subarray with the second half of the array
    for j in range(0, right_arr_length):
        right_array.append(array[middle_index + j + 1])

    # Append infinity to the end of each subarray to serve as a sentinel value
    left_array.append(float("inf"))
    right_array.append(float("inf"))

    # Initialize counters for the left and right subarrays
    i = 0
    j = 0

    # Iterate over the range from start_index to end_index (inclusive), merging the subarrays back together
    for k in range(start_index, end_index + 1):
        # Compare the current elements of the subarrays and insert the smaller one into the original array
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
