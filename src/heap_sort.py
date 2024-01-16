def left(index):
    # Compute and return the index of the left child for a binary heap.
    return (2 * index) + 1


def right(index):
    # Compute and return the index of the right child for a binary heap.
    return (2 * index) + 2


def swap(array, first_index, second_index):
    # Swap the elements of array at the positions first_index and second_index.
    array[first_index], array[second_index] = array[second_index], array[first_index]


def max_heapify(array, heap_size, root_index):
    # Maintain the heap property for the array. If the root element is smaller than its children,
    # it is swapped with the largest child and the function is called recursively.
    largest = root_index
    left_index = left(root_index)
    right_index = right(root_index)

    # If left child exists and is greater than root
    if left_index <= heap_size and array[left_index] > array[largest]:
        largest = left_index

    # If right child exists and is greater than root
    if right_index <= heap_size and array[right_index] > array[largest]:
        largest = right_index

    # If root is not the largest, swap it with the largest and recursively heapify the affected sub-tree
    if largest != root_index:
        swap(array, root_index, largest)
        max_heapify(array, heap_size, largest)


def build_max_heap(array):
    # Construct a max heap from the input array by calling max_heapify on each parent node, starting from the bottom.
    heap_size = len(array) - 1
    # Start from the last parent node, and go up to the root node
    for i in range(heap_size // 2, -1, -1):
        max_heapify(array, heap_size, i)


def heap_sort(array):
    # Implement heap sort by building a max heap and then repeatedly extracting the maximum element.
    build_max_heap(array)
    # The heap size starts from the last index of the array
    heap_size = len(array) - 1
    # Go up to the second last element of the array
    for i in range(heap_size, 0, -1):
        # Move the current largest element to its correct position
        swap(array, 0, i)
        # Reduce the heap size since the largest element is now sorted
        heap_size -= 1
        # Heapify the root element since it violates the heap property
        max_heapify(array, heap_size, 0)
    return array
