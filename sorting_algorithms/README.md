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
- Complexity of O(n^2)

### Insertion Sort
- Work left to right - examine each item and compare it to items on its left. Insert the item in the correct position in the array.
- The array will form sorted and unsorted partitions.


### Merge Sort

### Quicksort

### Timsort

###