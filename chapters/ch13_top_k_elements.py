import dis
from heapq import *
from typing import List

from data_structures.point import Point


# Problem 1 - Top 'K' Numbers
def find_k_largest_nums(arr: List[int], k: int) -> List[int]:
    min_heap = []

    for i in range(k):
        heappush(min_heap, arr[i])

    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, arr[i])

    return min_heap


# Problem 2 - Kth Smallest Number
def find_kth_smallest_num(arr: List[int], k: int) -> int:
    max_heap = []

    for i in range(k):
        heappush(max_heap, -arr[i])

    for i in range(k, len(arr)):
        if -arr[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -arr[i])

    return -max_heap[0]


# Problem 3 - 'K' Closest Points to the Origin
def find_k_closest_points_to_origin(points: List[Point], k: int) -> List[Point]:
    max_heap = []

    # Push initial k points to the heap
    for i in range(k):
        heappush(max_heap, points[i])

    # Cycle through the remaining points and push
    for i in range(k, len(points)):
        # Max heap, so root value is furthest from the origin in the heap
        if points[i].distance_from_origin < max_heap[0].distance_from_origin:
            heappop(max_heap)
            heappush(max_heap, points[i])

    return max_heap


# Problem 4 - Connect Ropes
def connect_ropes(ropes: List[int]):
    min_heap = []

    for i in ropes:
        heappush(min_heap, ropes[i])

    result, temp = 0, 0

    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)

    return result


# Problem 5 - Top 'K' Frequent Numbers
def find_top_k_freq_numbers(arr: List[int], k: int) -> List[int]:
    frequency_map = {}
    for num in arr:
        if num not in frequency_map:
            frequency_map[num] = 0
        frequency_map[num] += 1

    min_heap = []

    frequency_tuples = list(frequency_map.items())

    for i in range(k):
        heappush(min_heap, frequency_tuples[i])

    for i in range(k, len(frequency_tuples)):
        min_frequency = min_heap[0][1]
        current_frequeny = frequency_tuples[i][1]

        if current_frequeny > min_frequency:
            heappop(min_heap)
            heappush(min_heap, frequency_tuples[i])

    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[0])

    return top_numbers


# Problem 6 - Frequency Sort
def frequency_sort(s: str) -> str:
    frequency_map = {}
    for c in s:
        if c not in frequency_map:
            frequency_map[c] = 0
        frequency_map[c] += 1

    max_heap = []
    for char, frequency in frequency_map.items():
        heappush(max_heap, (-frequency, char))

    sorted_string = []

    while max_heap:
        frequency, char = heappop(max_heap)
        for _ in range(-frequency):
            sorted_string.append(char)

    return "".join(sorted_string)


# Problem 7 - Kth Largest Number in a Stream
class KthLargestNumberInStream:
    pass


# Problem 8 - 'K' Closest Numbers
def find_closest_elements(arr: List[int], k: int, x: int):
    "Find k closest elements to x in the array"
    index = binary_search(arr, x)
    low, high = index - k, index + k

    low = max(low, 0)  # low cannot be less than zero
    high = min(
        high, len(arr) - 1
    )  # high cannot be greater than the length of the array

    min_heap = []

    # Now just add the numbers than are k index either side of the closest value
    for i in range(low, high + 1):
        heappush(min_heap, (abs(arr[i] - k), arr[i]))

    results = []
    for _ in range(k):
        results.append(heappop(min_heap)[1])

    results.sort()
    return results


def binary_search(arr: List[int], target: int) -> int:
    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    # If we get this far, start = end + 1
    start_num = arr[start]
    end_num = arr[end]

    if abs(start_num - target) < abs(end_num - target):
        return start
    return end


# Problem 9 - Maximum Distinct Elements
def max_distinct_elements(arr: List[int], k: int):
    distinct_count = 0
    frequency_map = {}

    for c in arr:
        if c not in frequency_map:
            frequency_map[c] = 0
        frequency_map[c] += 1

    min_heap = []
    for (num, frequency) in frequency_map.items():
        if frequency == 1:
            distinct_count += 1
        elif frequency > 1:
            heappush(min_heap, (frequency, num))

    # Attempt to delete elements to create distinct elements. Use k to track
    #   the number of deletions.
    while min_heap and k > 0:
        frequency, num = heappop(min_heap)

        # Delete (frequency - 1) elements to make element distinct
        n_deletions = frequency - 1
        k -= n_deletions

        if k >= 0:
            distinct_count += 1

    # After this loop, if k is still greater than 0, we haven't made enough deletions.
    #   Therefore, need to remove some of the distinct elements.

    if k > 0:
        distinct_count -= k

    return distinct_count


# Problem 10 - Sum of Elements
def sum_of_elements(arr: List[int], k1: int, k2: int) -> int:
    min_heap = []

    for num in arr:
        heappush(min_heap, num)

    for _ in range(k1):
        heappop(min_heap)

    result = 0
    for _ in range(k2 - k1 - 1):
        result += heappop(min_heap)

    return result


# Problem 11 - Rearrange String
def rearrange_string():
    return


# Problem Challenge 1: Rearrange String K Distance Apart
def rearrange_string_k_distance_apart():
    return


# Problem Challenge 2: Scheduling Tasks
def scheduling_tasks():
    return


# Problem Challenge 3: Frequency Stack
def frequency_stack():
    return
