def counting_sort(array, max_value) -> list:
    # Create a list of zeroes with a length equal to the maximum value in the input list
    count_array = [0 for _ in range(max_value + 1)]
    # Create a list of zeroes with a length equal to the length of the input list
    sorted_array = [0 for _ in range(len(array))]

    # Iterate over the input list and increment the count of each number by one
    for j in range(len(array)):
        # Increment the count of the current number by one
        count_array[array[j]] = count_array[array[j]] + 1

    # Modify the count array such that each element at each index stores the sum of previous counts
    for i in range(1, max_value + 1):
        # Add the current count with the previous count
        count_array[i] = count_array[i] + count_array[i - 1]

    # Iterate over the input list in reverse order
    for j in range(len(array) - 1, -1, -1):
        # Decrement the count of the current number by one
        sorted_array[count_array[array[j]] - 1] = array[j]
        # Decrement the count of the current number by one
        count_array[array[j]] = count_array[array[j]] - 1

    # Return the sorted list
    return sorted_array
