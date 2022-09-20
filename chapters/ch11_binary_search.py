import math
from typing import List


# Problem 1 - Order-agnostic Binary Search
def binary_search(arr: List[int], key: int) -> int:
    start, end = 0, len(arr) - 1

    is_ascending = arr[start] <= arr[end]

    while start <= end:
        middle = (start + end) // 2

        if key == arr[middle]:
            return middle

        if is_ascending:
            if key < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if key > arr[middle]:
                end = middle - 1
            else:
                start = middle + 1

    return -1


# Problem 2 - Ceiling of a Number
def ceiling_of_a_number(arr: List[int], key: int) -> int:
    n = len(arr)
    start, end = 0, len(arr) - 1

    if key > arr[end]:
        return -1  # No ceiling

    while start <= end:
        middle = (start + end) // 2

        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else:
            return middle

    return start


# Problem 3 - Next Letter
def next_letter(arr: List[int], key: int) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end) // 2

        if key < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    # Loop runs until start = end + 1
    return arr[start % len(arr)]


# Problem 4 - Number Range
def find_range(arr: List[int], key: int) -> List[int]:
    min_index = range_binary_search(arr, key, False)
    if min_index == -1:
        return [-1, -1]
    return [min_index, range_binary_search(arr, key, True)]


def range_binary_search(arr: List[int], key: int, find_max_index: bool) -> int:
    key_index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end) // 2

        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else:
            key_index = middle
            if find_max_index:
                start = middle + 1
            else:
                end = middle - 1

    return key_index


# Problem 5 - Search in a Sorted Infinite Array
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


# TODO
def infinite_array():
    return


# Problem 6 - Minimum Difference Element
def search_min_diff_element(arr: List[int], key: int) -> int:
    n = len(arr)
    start, end = 0, n - 1

    if key <= arr[start]:
        return arr[start]

    if key >= arr[end]:
        return arr[end]

    while start <= end:
        middle = (start + end) // 2

        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else:
            return arr[middle]

    # If key hasn't been found, start = end + 1
    start_num = arr[start]  # The larger number
    end_num = arr[end]  # The smaller number

    if (start_num - key) > (key - end_num):
        return end_num
    return start_num


# Problem 7 - Bitonic Array Maximum
def bitonic_binary_search(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start < end:
        middle = (start + end) // 2

        if arr[middle] > arr[middle + 1]:
            end = middle
        else:
            start = middle + 1

    return arr[start]


# Problem Challenge 1 - Search Bitonic Array
def search_bitonic_array(arr: List[int], key: int) -> int:
    max_index = bitonic_binary_search_index(arr)
    index_ascending_search = binary_search_index(arr, key, 0, max_index)
    if arr[index_ascending_search] == key:
        return index_ascending_search
    return binary_search_index(arr, key, max_index + 1, len(arr) - 1)


def bitonic_binary_search_index(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start < end:
        middle = (start + end) // 2

        if arr[middle] > arr[middle + 1]:
            end = middle
        else:
            start = middle + 1

    return start


def binary_search_index(arr: List[int], key: int, start: int, end: int) -> int:
    is_ascending = arr[start] < arr[end]

    while start <= end:
        middle = (start + end) // 2

        if key == arr[middle]:
            return middle

        if is_ascending:
            if key < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if key > arr[middle]:
                end = middle - 1
            else:
                start = middle + 1

    return -1


# Problem Challenge 2 - Search in Rotated Array
def search_rotated_array(arr: List[int], key: int) -> int:

    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if key == arr[middle]:
            return middle

        # Since the sorted ascending list is rotated, there will now
        #   be a sorted side and an unsorted side remaining

        # Sorted side on LHS
        if arr[start] <= arr[middle]:
            if key >= arr[start] and key < arr[middle]:
                # Key is in the first half of the array (sorted)
                end = middle - 1
            else:
                # Key is in the second half of the array (unsorted)
                start = middle + 1

        # Sorted side on RHS
        elif arr[start] > arr[middle]:
            if key <= arr[end] and key > arr[middle]:
                # Key is in the second half of the array (sorted)
                start = middle + 1
            else:
                # Key is in the first half of the array (unsorted)
                end = middle - 1

    return -1


# Problem Challenge 3 - Rotation Count
def rotation_count(arr: List[int]) -> int:
    # Array is sorted in ascending order and rotated k times
    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        # Need to return the index of the max value in the array
        if middle < end and arr[middle] > arr[middle + 1]:
            # If middle number is larger than the next number
            return middle + 1  # Add one to convert 0 based index to num of rotations
        elif middle > start and arr[middle] < arr[middle - 1]:
            # If the previous number was larger than the middle number
            return middle

        if arr[start] > arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return 0
