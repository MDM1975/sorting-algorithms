import random


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


data = [random.randint(i, 10_000) for i in range(10)]

print(f"Unsorted array: {data}") # [1537, 2219, 5248, 6870, 5668, 6880, 4428, 9529, 8232, 1189]

insertion_sort(data)

print(f"Sorted array: {data}") ## [1189, 1537, 2219, 4428, 5248, 5668, 6870, 6880, 8232, 9529]
