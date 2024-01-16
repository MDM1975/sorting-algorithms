def shell_sort(array) -> None:
    # Get the size of the array
    size = len(array)
    # Set the gap size to half the size of the array
    gap_size = size // 2

    # Iterate over the array until the gap size is 0
    while gap_size > 0:
        # Set the current position to the gap size
        current_position = gap_size

        # Iterate over the array starting at the gap position
        while current_position < size:
            # Set the comparison position to the current position minus the gap size
            comparison_position = current_position - gap_size

            # Iterate over the array starting at the comparison position
            while comparison_position >= 0:
                # If the element at the comparison position is less than the element at the comparison position plus the gap size, break
                if array[comparison_position + gap_size] > array[comparison_position]:
                    break
                else:
                    # Swap the elements
                    array[comparison_position + gap_size], array[comparison_position] = array[comparison_position], array[comparison_position + gap_size]

                # Decrement the comparison position by the gap size
                comparison_position -= gap_size

            # Increment the current position by the gap size
            current_position += 1

        # Divide the gap size by 2
        gap_size //= 2
