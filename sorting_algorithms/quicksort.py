from typing import List


def quicksort(arr: List[int]):
    return quicksort_recursion(arr, 0, len(arr) - 1)


def quicksort_recursion(arr: List[int], left: int, right: int):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort_recursion(arr, left, partition_pos - 1)
        quicksort_recursion(arr, partition_pos + 1, right)


def partition(arr: List[int], left: int, right: int) -> int:
    """
    Return the quicksort partition index for an array
    """
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
