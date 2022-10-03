from typing import List

# Complexity: O(n^2)


def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        j = i - 1  # previous item
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    return arr
