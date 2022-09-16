from typing import List


# Problem 1 - Cyclic Sort
def cyclic_sort(arr: List[int]) -> List[int]:
    i = 0

    # Aim is to compare the number at the ith position with the number at the position based on this number.
    while i < len(arr):
        j = arr[i] - 1  # Expected number
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the numbers
        else:
            i += 1

    return arr


# Problem 2 - Find the Missing Number
def missing_number(arr: List[int]) -> int:
    i, n = 0, len(arr)

    while i < n:
        j = arr[i]  # Expected number
        if j < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the numbers
        else:
            i += 1

    for i in range(n):
        if i != arr[i]:
            return i

    return n


# Problem 3 - Find all Missing Numbers
def n_missing_numbers(arr: List[int]) -> List[int]:
    i, n = 0, len(arr)

    while i < n:
        j = arr[i] - 1  # Expected number
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the numbers
        else:
            i += 1

    missing_numbers = []

    for i in range(n):
        if i + 1 != arr[i]:
            missing_numbers.append(i + 1)

    return missing_numbers


# Problem 4 - Find the Duplicate Number
def find_duplicate_number(arr: List[int]) -> int:
    i, n = 0, len(arr)

    while i < n:
        if arr[i] != i + 1:
            j = arr[i] - 1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                return arr[i]
        else:
            i += 1

    return -1


# Problem 5 - Find all duplicate numbers
def test_find_all_duplicate_numbers(arr: List[int]):
    i, n = 0, len(arr)

    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    duplicate_numbers = []

    for i in range(n):
        if i != arr[i] - 1:
            duplicate_numbers.append(arr[i])

    return duplicate_numbers
