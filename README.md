# Sorting Algorithms

This repository is a comprehensive collection of sorting algorithm implementations in Python. The aim is to showcase the implementation of various sorting techniques and provide a deep dive into each algorithm's theoretical and practical aspects. Whether you're a student learning about sorting algorithms for the first time, a teacher looking for educational materials, or a professional brushing up on your computer science fundamentals, you'll find valuable insights here.

## Featured Algorithms

Within this project, you'll find Python implementations for the following sorting algorithms, each with its dedicated module:

- [Bubble Sort](./src/bubble_sort.py):
  - A simple comparison-based algorithm that repeatedly steps through the list compares adjacent elements and swaps them if they are in the wrong order.
- [Counting Sort](./src/counting_sort.py):
  - An integer sorting algorithm that counts the number of objects with distinct key values.
- [Heap Sort](./src/heap_sort.py):
  - A comparison-based sorting technique based on a binary heap data structure.
- [Insertion Sort](./src/insertion_sort.py):
  - A simple sorting algorithm that builds the final sorted array (or list) one item at a time.
- [Quick Sort](./src/quick_sort.py):
  - An efficient, divide-and-conquer, comparison-based sorting algorithm.
- [Median of Three QuickSort](./src/median_of_three_quicksort.py):
  - A variant of Quick Sort that chooses the pivot as the median of three elements from the array.
- [Randomized Quick Sort](./src/random_quick_sort.py):
  - An adaptation of Quick Sort where the pivot is chosen randomly.
- [Merge Sort](./src/merge_sort.py):
  - A divide and conquer algorithm that divides the input array into two halves sorts the two halves independently and then merges them.
- [Shell Sort](./src/shell_sort.py):
  - An in-place comparison sort that generalizes inserting sort to allow the exchange of far apart items.

## Algorithm Time Complexity - Big O Notation

Understanding the time complexity of each algorithm is critical to appreciating their efficiency and suitability for different datasets and applications. Here's a quick overview:

### Bubble Sort

- **Time Complexity:** $Θ(n^2)$

### Counting Sort

- **Time Complexity:** $Θ(n+k)$

### Heap Sort

- **Time Complexity:** $Θ(n \log n)$

### Insertion Sort

- **Time Complexity:** $Θ(n^2)$

### Quick Sort

- **Time Complexity:** $Θ(n \log n)$

### Median of Three QuickSort

- **Time Complexity:** $Θ(n \log n)$

### Randomized Quick Sort

- **Time Complexity:** $Θ(n \log n)$

### Merge Sort

- **Time Complexity:** $Θ(n \log n)$

### Shell Sort

- **Time Complexity:** $Θ(n(\log(n))^2)$

## Running the Code

You can run the code for any sorting algorithm by providing a sample dataset and executing the corresponding Python file. For example, to run the Bubble Sort implementation:

Provide a sample dataset in the `src/bubble_sort.py` file:

```python
def insertion_sort(array) -> None:
    # ... (implementation)


data = [random.randint(i, 10_000) for i in range(10)]

print(f"Unsorted array: {data}") # [1537, 2219, 5248, 6870, 5668, 6880, 4428, 9529, 8232, 1189]

insertion_sort(data)

print(f"Sorted array: {data}") ## [1189, 1537, 2219, 4428, 5248, 5668, 6870, 6880, 8232, 9529]
```

From the command line use the following command:

```shell
python3 src/insertion_sort.py
```

I encourage you to dive into the code, experiment with it, and see firsthand how each algorithm tackles the problem of sorting data uniquely. Happy coding!
