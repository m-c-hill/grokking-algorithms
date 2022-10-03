from typing import List


def selection_sort(arr: List):

    for i in range(0, len(arr)):
        cur_min = i
        for j in range(i, len(arr)):
            # breakpoint()
            if arr[j] < arr[cur_min]:
                cur_min = j

        arr[i], arr[cur_min] = arr[cur_min], arr[i]

    return arr

l = [4,3,2,1]
selection_sort(l)

print(l)