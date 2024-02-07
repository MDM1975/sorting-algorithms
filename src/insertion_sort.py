def insertion_sort(array) -> None:
    # Iterate over the array, starting from the second element
    for i in range(1, len(array)):
        # Save the current element for comparison
        current_number = array[i]

        # Initialize the pointer for the preceding element's index
        previous_index = i - 1

        # Traverse backwards from the current element, swapping as necessary
        # Continue until the start of the list is reached or until finding an element smaller than the current number
        while previous_index >= 0 and array[previous_index] > current_number:
            # Shift the larger number to the right
            array[previous_index + 1] = array[previous_index]

            # Move the pointer for comparison to the next preceding element
            previous_index -= 1

        # Having found the correct position, insert the current number
        array[previous_index + 1] = current_number
