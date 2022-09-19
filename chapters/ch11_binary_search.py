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
    start, end = 0, len(arr) -1
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
    start, end = 0, len(arr) -1
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
def infinite_array():
    return


# Problem 6 - Minimum Difference Element
def search_min_diff_element():
    return


# Problem 7 - Bitonic Array Maximum
def bitonic_binary_search():
    return


# Problem Challenge 1 - Search Bitonic Array
def search_bitonic_array():
    return


# Problem Challenge 2 - Search in Rotated Array
def search_rotated_array():
    return


# Problem Challenge 3 - Rotation Count
def rotation_count():
    return
