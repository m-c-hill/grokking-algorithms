import pytest

from chapters.ch13_top_k_elements import *
from data_structures.point import Point


# Problem 1 - Top 'K' Numbers
@pytest.mark.parametrize(
    "arr,k,expected",
    [([3, 1, 5, 12, 2, 11], 3, [5, 12, 11]), ([5, 12, 11, -1, 12], 3, [11, 12, 12])],
)
def test_top_k_largest_numbers(arr, k, expected):
    res = find_k_largest_nums(arr, k)
    assert res == expected


# Problem 2 - Kth Smallest Number
@pytest.mark.parametrize(
    "arr,k,expected",
    [([1, 5, 12, 2, 11, 5], 3, 5), ([1, 5, 12, 2, 11, 5], 4, 5)],
)
def test_top_k_largest_numbers(arr, k, expected):
    res = find_kth_smallest_num(arr, k)
    assert res == expected


# Problem 3 - 'K' Closest Points to the Origin
@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([Point(1, 2), Point(1, 3)], 1, [Point(1, 2)]),
        ([Point(1, 3), Point(3, 4), Point(2, -1)], 2, [Point(1, 3), Point(2, -1)]),
    ],
)
def test_find_k_closest_points_to_origin(arr, k, expected):
    res = find_k_closest_points_to_origin(arr, k)
    assert res == expected


# Problem 4 - Connect Ropes
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 3, 11, 5], 33),
        ([3, 4, 5, 6], 36),
    ],
)
def test_connect_ropes(arr, expected):
    res = connect_ropes(arr)
    assert res == expected


# Problem 5 - Top 'K' Frequent Numbers
@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([1, 3, 5, 12, 11, 12, 11], 2, [11, 12]),
        ([5, 12, 11, 3, 11], 2, [11, 12]),
    ],
)
def test_find_top_k_freq_numbers(arr, k, expected):
    res = find_top_k_freq_numbers(arr, k)
    assert res == expected
