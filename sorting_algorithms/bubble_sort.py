from typing import List

# Complexity: O(n^2)


def bubble_sort(arr: List[int]):
    for j in range(len(arr) - 1):
        already_sorted = True
        for i in range((len(arr) - 1) - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                already_sorted = False

    return arr
