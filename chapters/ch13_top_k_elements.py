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
