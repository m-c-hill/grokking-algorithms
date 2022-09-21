import math
from heapq import *
from typing import List

from data_structures.node import ListNode


# Problem 1 - Merge K Sorted Lists
def merge_k_sorted_list(lists: ListNode) -> ListNode:
    min_heap = []

    # Put the first element of each list in the min heap
    for l in lists:
        if l is not None:
            heappush(min_heap, l)

    result_head = None
    while min_heap:
        smallest_node = heappop(min_heap)

        if result_head is None:
            result_tail = smallest_node
            result_head = result_tail
        else:
            result_tail.next = smallest_node
            result_tail = result_tail.next

        if smallest_node.next is not None:
            heappush(min_heap, smallest_node.next)

    return result_head


# Problem 2 - Kth Smallest Number in M Sorted Lists
def kth_smallest_number_in_m_sorted_lists(lists: List[List[int]], k: int) -> int:
    min_heap = []

    for l in lists:
        # Push a tuple containing the first (smallest) value in the list and the list itself.
        heappush(min_heap, (l[0], l))

    result_count = 0
    result_number = -1
    while min_heap:
        result_number, l = heappop(min_heap)
        result_count += 1

        if result_count == k:
            break

        if len(l) > 1:
            heappush(min_heap, (l[1], l[1:]))

    return result_number


# Problem 3 - Kth Smallest Number in a Sorted Matrix
def kth_smallest_number_in_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    min_heap = []

    # Don't need to  push anymore than k elements into the heap since matrix
    #   has sorted rows and sorted columns.
    for i in range(min(k, len(matrix))):
        # Push a tuple containing the first (smallest) value in the list and the list itself.
        heappush(min_heap, (matrix[i][0], matrix[i]))

    result_count = 0
    result_number = -1
    while min_heap:
        result_number, row = heappop(min_heap)
        result_count += 1

        if result_count == k:
            break

        if len(row) > 1:
            heappush(min_heap, (row[1], row[1:]))

    return result_number


# Problem 4 - Smallest Number Range
def smallest_number_range(lists: List[List[int]]) -> List[int]:
    min_heap = []
    max_num_in_heap = -math.inf

    # Add min num of each list to a min heap
    for l in lists:
        heappush(min_heap, (l[0], l))
        max_num_in_heap = max(l[0], max_num_in_heap)

    range_start, range_end = 0, math.inf
    while len(min_heap) == len(lists):
        num, l = heappop(min_heap)
        current_range = range_end - range_start
        new_range = max_num_in_heap - num

        if new_range < current_range:
            range_start = num
            range_end = max_num_in_heap

        if len(l) > 1:
            heappush(l[1], l[1:])
            max_num_in_heap = max(max_num_in_heap, l[1])

    return [range_start, range_end]


# Problem Challenge 1 - K Pairs with Largest Sums
def find_pairs_with_largest_sums(
    arr1: List[int], arr2: List[int], k: int
) -> List[List[int]]:
    min_heap = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):

            # Initially add k pairs
            if len(min_heap) < k:
                heappush(min_heap, (arr1[i] + arr2[j], arr1[i], arr2[j]))

            else:
                # The arrays are sorted in descending order. So, if we reach
                #   a pair whose sum is less than the min sum in the heap,
                #   we can break. There will not be a pair with a greater sum
                #   if we continued.
                min_sum = min_heap[0][0]
                if arr1[i] + arr2[j] < min_sum:
                    break
                else:
                    # Otherwise, remove the current min and replace
                    heappop(min_heap)
                    heappush(min_heap, (arr1[i] + arr2[i], arr1[i], arr2[j]))

    results = []
    for (sum, num1, num2) in min_heap:
        results.append([num1, num2])

    return results
