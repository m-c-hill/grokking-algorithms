from typing import List


def merge_sort(arr: List[int]):

    if len(arr) > 1:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left arr index
        j = 0  # right arr index
        k = 0  # merged arr index
        while i < len(left_arr) and j < len(right_arr):
            # compare left most elements of sorted lists
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr
