import heapq
from heapq import *
from typing import List


# Problem 1 - Find the Median of a Number Stream
class MedianOfStream:
    def __init__(self):
        self.max_heap = []  # To store the first half of the numbers
        self.min_heap = []  # To store the second half of the numbers

    def __repr__(self) -> str:
        nums = []
        for num in self.max_heap:
            nums.append(-num)
        for num in self.min_heap:
            nums.append(num)
        return str(sorted(nums))

    # heapq default is a min heap. For the max heap, invert values when inserting.
    def insert_num(self, num: int):
        # Insert number
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)  # Inversting since max heap
        elif num > -self.max_heap[0]:
            heappush(self.min_heap, num)

        # Rearrange the two heaps - must ensure they are both of equal size or that max heap has one more element
        max_heap_size = len(self.max_heap)
        min_heap_size = len(self.min_heap)

        if max_heap_size > min_heap_size + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

        elif min_heap_size > max_heap_size:
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0

        return -self.max_heap[0]


# Problem 2 - Sliding Window Median
class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []  # To store the first half of the numbers
        self.min_heap = []  # To store the second half of the numbers

    def find_sliding_window_median(self, arr: List[int], window_size: int) -> List[int]:

        array_size = len(arr)
        if array_size > window_size:
            raise Exception

        results = [0.0 for num in range(array_size - window_size + 1)]

        for i in range(array_size):
            self.insert(arr[i])
            self.rebalance_heaps()

            # If there are at least window_size numbers in the sliding window:
            if (i + 1) >= window_size:
                # Calculate the median and add to the result set
                if len(self.max_heap) == len(self.min_heap):
                    results[i + 1 - window_size] = (
                        self.min_heap[0] + -self.max_heap
                    ) / 2.0
                else:
                    results[i + 1 - window_size] = self.min_heap[0] / 1.0

                # Identify the element that needs removing
                number_to_remove = arr[(i + 1) - window_size]

                if number_to_remove <= -self.max_heap[0]:
                    self.remove(self.max_heap, -number_to_remove)
                else:
                    self.remove(self.min_heap, number_to_remove)

                self.rebalance_heaps()
        return results

    def insert(self, num: int):
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)  # Inversting since max heap
        elif num > -self.max_heap[0]:
            heappush(self.min_heap, num)

    def remove(self, heap, number_to_remove):
        i = heap.index(number_to_remove)
        heap[i] = heap[-1]
        del heap[-1]

        if i < len(heap):
            heapq._siftup(heap, i)
            heapq._siftdown(heap, 0, i)

    def rebalance_heaps(self):
        max_heap_size = len(self.max_heap)
        min_heap_size = len(self.min_heap)

        if min_heap_size >= max_heap_size:
            # Push the inverted value of the max of the min heap to the max heap
            heappush(self.max_heap, -heappop(self.min_heap))
        elif max_heap_size > max_heap_size + 1:
            # Push the inverted value of the min of the max heap to the min heap
            heappush(self.min_heap, -heappop(self.max_heap))


# Problem 3 - Maximize Capital


# Problem Challenge 1: Next Interval


med = MedianOfStream()
med.insert_num(1)
med.insert_num(2)
breakpoint()
med.find_median()