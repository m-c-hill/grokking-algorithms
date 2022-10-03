# Sorting Algorithms

## Applications

Sorting useful for a number of applications:
- *Searching* - searching for an item in a list is faster when the list is sorted.
- *Selection* - selecting items from a list based on their relationship to the rest of the items is easier with sorted data.
- *Duplicates* - finding duplicates faster when list is sorted.
- *Distribution* - analyzing the frequency distribution of items on a list is very fast if the list is sorted.

## Python's Built in Sort

`sorted` wiill sort items in a list in-place. It uses the Timsort algorithm which is a hybrid sorting algorithm, derived from merge sort and insertion sort.

```bash
>>> array = [8, 2, 6, 4, 5]
>>> sorted(array)

[2, 4, 5, 6, 8]
```

## Sorting Algorithms

### Bubble Sort

- With every new pass through the list, the largest element in the list “bubbles up” toward its correct position.
- Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.
- Compare elements at i and i+1, and swap if num[i] > num[i+1]
- Complexity of `O(n^2)`

### Insertion Sort
- Iteratively work through each item in the list. The insertion sort partitions the array into a sorted and unsorted section as it works through each item, with the sorted section on the left and unsorted on the right.
- Examine each item and compare it to the items on its left (the unsorted section). Insert the item in the correct position in the array by continuing to swap the item with its neigbours until it is no longer smaller than its left neighbour.
- Complexity of `O(n^2)`


### Merge Sort

- Divide and conquer algorithm (breaks down problem into multiple subproblems to solve recursively).
- Method:
  - Split array in half
  - Call merge sort on each half
  - Merge both sorted halves into one sorted array
- Complexity of `O(n * log(n))`

### Quicksort

- Another divide and conquer algorithm.
- Method:
  - Choose pivot element
  - Store elements less than the pivot element in left subarray, and those greater in the right subarray
  - Call quicksort recursively on the left and right subarrays until array sizes are 1.
- Complexity of `O(n * log(n))` in best case, `O(n^2)` in worst case


### Timsort

###