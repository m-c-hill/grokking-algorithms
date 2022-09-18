import pytest

from chapters.ch02_two_pointers import *

# ==============================================
#  Problems
# ==============================================


# Problem 1 - Pair with Target Sum
@pytest.mark.parametrize(
    "arr,k,expected", [([1, 2, 3, 4, 6], 6, [1, 3]), ([2, 5, 9, 11], 11, [0, 2])]
)
def test_find_pair_sum(arr, k, expected):
    res = find_pair_sum(arr, k)
    assert res == expected


# Problem 2 - Remove Duplicates
@pytest.mark.parametrize(
    "arr,expected", [([2, 3, 3, 3, 6, 9, 9], 4), ([2, 2, 2, 11], 2)]
)
def test_remove_duplicates(arr, expected):
    res = remove_duplicates(arr)
    assert res == expected


# Problem 3 - Squaring a Sorted Array
@pytest.mark.parametrize(
    "arr,expected",
    [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]), ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9])],
)
def test_squaring_sorted_array(arr, expected):
    res = squaring_sorted_array(arr)
    assert res == expected


# Problem 4 - Triplet Sum to Zero
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([-3, 0, 1, 2, -1, 1, -2], [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]),
        ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]]),
    ],
)
def test_triplet_sum_to_zero(arr, expected):
    res = triplet_sum_to_zero(arr)
    assert res == expected


# Problem 5 - Triplet Sum Close to Target
@pytest.mark.parametrize(
    "arr,target,expected",
    [([-2, 0, 1, 2], 2, 1), ([-3, -1, 1, 2], 1, 0), ([1, 0, 1, 1], 100, 3)],
)
def test_triplet_sum_close_to_target(arr, target, expected):
    res = triplet_sum_close_to_target(arr, target)
    assert res == expected


# Problem 6 - Triplets With Smallest Sum
@pytest.mark.parametrize(
    "arr,target,expected", [([-1, 0, 2, 3], 3, 2), ([-1, 4, 2, 1, 3], 5, 4)]
)
def test_triplets_with_smaller_sum(arr, target, expected):
    res = triplets_with_smaller_sum(arr, target)
    assert res == expected


# Problem 7 - Subarrays with Product Less than a Target
@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([2, 5, 3, 10], 30, [[2], [5], [2, 5], [3], [5, 3], [10]]),
        ([8, 2, 6, 5], 50, [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]),
    ],
)
def test_subarrays_with_product_less_than_target(arr, target, expected):
    res = subarrays_with_product_less_than_target(arr, target)
    assert res == expected


# Problem 8 - Dutch National Flag Problem
@pytest.mark.parametrize(
    "arr,expected",
    [([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]), ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2])],
)
def test_dutch_flag_sort(arr, expected):
    res = dutch_flag_sort(arr)
    assert res == expected


# ==============================================
#  Problem Challenges
# ==============================================

# # Problem Challenge 1
# @pytest.mark.parametrize(
#     "arr,k,expected",
#     [
#         ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
#         ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]]),
#     ],
# )
# def test_search_quadruplets(arr, k, expected):
#     res = search_quadruplets(arr, k)
#     assert res == expected


# # Problem Challenge 2
# @pytest.mark.parametrize(
#     "str1,str2,expected",
#     [
#         ("xy#z", "xzz#", True),
#         ("xy#z", "xyz#", False),
#         ("xp#", "xyz##", True),
#         ("xywrrmp", "xywrrmu#p", True),
#     ],
# )
# def test_backspace_compare(str1, str2, expected):
#     res = backspace_compare(str1, str2)
#     assert res == expected

# # Problem Challenge 3
# @pytest.mark.parametrize(
#     "arr,expected",
#     [
#         ([1, 2, 5, 3, 7, 10, 9, 12], 5),
#         ([1, 3, 2, 0, -1, 7, 10], 5),
#         ([1, 2, 3], 0),
#         ([3, 2, 1], 3),
#     ],
# )
# def test_shortest_window_sort(arr, expected):
#     res = shortest_window_sort(arr)
#     assert res == expected
