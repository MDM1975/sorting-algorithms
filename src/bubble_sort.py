def swap(array, first_index, second_index) -> None:
    # Swap the elements at the given indices
    array[first_index], array[second_index] = array[second_index], array[first_index]


def bubble_sort(array) -> None:
    for current_pass in range(len(array)):
        # Start from the end of the array and work backwards
        for current_index in range(len(array) - 1, current_pass, -1):
            # If the current element is less than the previous one, swap them
            if array[current_index] < array[current_index - 1]:
                swap(array, current_index, current_index - 1)
