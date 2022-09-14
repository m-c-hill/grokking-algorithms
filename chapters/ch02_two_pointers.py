import math
from collections import deque
from typing import List

# =====================
#  Problems
# =====================

# Problem 1 - Pair with Target Sum
def find_pair_sum(arr: List[int], target: int) -> list:
    l = 0
    r = len(arr) - 1

    while l < r:
        current_sum = arr[l] + arr[r]

        if current_sum < target:
            l += 1
        elif current_sum > target:
            r -= 1

        if current_sum == target:
            return [l, r]

    return [-1, -1]


# Problem 2 - Remove Duplicates
def remove_duplicates(arr: List[int]) -> int:
    p = 0  # The index of the current number be assessed
    next_non_duplicate = 1  # Position at which the next non-duplicate should be placed

    while p < len(arr):
        if arr[p] != arr[next_non_duplicate - 1]:
            arr[next_non_duplicate] = arr[p]
            next_non_duplicate += 1
        p += 1

    return next_non_duplicate


# Problem 3 - Squaring a Sorted Array
def squaring_sorted_array(arr: List[int]) -> list:
    """Calculates the square values of the elements in the input arr and returns an ordered array of results"""
    n = len(arr)
    squared_arr = [0 for _ in arr]

    # Pointers are initiated at the extremes of the array, so the LARGEST square values are calculated first
    l = 0
    r = n - 1

    squared_arr_index = n - 1

    while squared_arr_index >= 0:
        l_squared = arr[l] * arr[l]
        r_squared = arr[r] * arr[r]

        if l_squared >= r_squared:
            squared_arr[squared_arr_index] = l_squared
            l += 1
        else:
            squared_arr[squared_arr_index] = r_squared
            r -= 1

        squared_arr_index -= 1

    return squared_arr


# Problem 4 - Triplet Sum to Zero
def triplet_sum_to_zero(arr: List[int]) -> list:
    """Find all unique triplets within an array which sum to zero"""
    arr.sort()
    triplets = []

    for i in range(len(arr) - 2):
        search_pair_with_target_sum(
            results=triplets, arr=arr, left_pointer=i + 1, target=-arr[i]
        )

    return triplets


def search_pair_with_target_sum(
    results: list, arr: List[int], left_pointer: int, target: int
) -> None:
    l = left_pointer
    r = len(arr) - 1

    while l < r:
        current_sum = arr[l] + arr[r]

        if current_sum < target:
            l += 1
        elif current_sum > target:
            r -= 1
        elif current_sum == target:
            # Update the results
            results.append([-target, arr[l], arr[r]])
            l += 1
            r -= 1

            # Skip duplicates
            while arr[l] == arr[l - 1]:
                l += 1
            while arr[r] == arr[r + 1]:
                r -= 1


# Problem 5 - Triplet Sum Close to Target
def triplet_sum_close_to_target(arr: List[int], target: int) -> list:
    arr.sort()
    smallest_difference = math.inf

    for i in range(len(arr) - 2):
        l = i + 1
        r = len(arr) - 1

        while l < r:
            target_difference = target - arr[i] - arr[l] - arr[r]

            if target_difference == 0:
                return target

            if abs(target_difference) < abs(smallest_difference):
                smallest_difference = target_difference

            if target_difference > 0:
                l += 1
            elif target_difference < 0:
                r -= 1

    return target - smallest_difference


# Problem 6 - Triplets With Smaller Sum
def triplets_with_smaller_sum(arr: List[int], target: int):
    arr.sort()
    triplet_count = 0

    for i in range(len(arr) - 2):
        l = i + 1
        r = len(arr) - 1

        while l < r:
            if arr[i] + arr[l] + arr[r] < target:
                triplet_count += r - l
                l += 1
            else:
                r -= 1

    return triplet_count


# Problem 7 - Subarrays with Product Less than a Target
def subarrays_with_product_less_than_target(arr: List[int], target: int) -> int:
    product = 1
    subarrays = []

    l = 0
    r = 0

    while r < len(arr):
        product *= arr[r]

        while product >= target and l < len(arr):
            product /= arr[l]
            l += 1

        temp_list = deque()
        for i in range(r, l - 1, -1):
            temp_list.appendleft(arr[i])
            subarrays.append(list(temp_list))

        r += 1

    return subarrays


# Problem 8 - Dutch National Flag Problem (Dutch Flag Sort)
def dutch_flag_sort(arr: List[int]):
    # Two pointers to track the 0/1 and 1/2 divides
    low, high = 0, len(arr) - 1
    i = 0

    while i <= high:

        if arr[i] == 0:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1

        elif arr[i] == 1:
            i += 1

        else:  # arr[i] == 2
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1

    return arr


# =====================
#  Problem Challenges
# =====================
