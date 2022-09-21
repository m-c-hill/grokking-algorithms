from cmath import exp

import pytest

from chapters.ch05_cyclic_sort import *


# Problem 1 - Cyclic Sort
@pytest.mark.parametrize(
    "input,expected",
    [
        ([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
        ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_cyclic_sort(input, expected):
    result = cyclic_sort(input)
    assert result == expected


# Problem 2 - Find the Missing Number
@pytest.mark.parametrize(
    "input,expected", [([4, 0, 3, 1], 2), ([8, 3, 5, 2, 4, 6, 0, 1], 7)]
)
def test_missing_number(input, expected):
    result = missing_number(input)
    assert result == expected


# Problem 3 - Find all Missing Numbers
@pytest.mark.parametrize(
    "input,expected",
    [([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]), ([2, 4, 1, 2], [3]), ([2, 3, 2, 1], [4])],
)
def test_n_missing_numbers(input, expected):
    result = n_missing_numbers(input)
    assert result == expected


# Problem 4 - Find the Duplicate Number
@pytest.mark.parametrize(
    "input,expected",
    [([1, 4, 4, 3, 2], 4), ([2, 1, 3, 3, 5, 4], 3), ([2, 4, 1, 4, 4], 4)],
)
def test_find_duplicate_number(input, expected):
    result = find_duplicate_number(input)
    assert result == expected


# Problem 5 - Find All Duplicate Numbers
@pytest.mark.parametrize(
    "input,expected", [([3, 4, 4, 5, 5], [5, 4]), ([5, 4, 7, 2, 3, 5, 3], [3, 5])]
)
def test_find_all_duplicate_numbers(input, expected):
    result = find_all_duplicate_numbers(input)
    assert result == expected


# Problem Challenge 1 - Find the Corrupt Pair
@pytest.mark.parametrize(
    "input,expected", [([3, 1, 2, 5, 2], [2, 4]), ([3, 1, 2, 3, 6, 4], [3, 5])]
)
def test_find_corrupt_numbers(input, expected):
    result = find_corrupt_numbers(input)
    assert result == expected


# Problem Challenge 2 - Find the Smallest Missing Positive Number
@pytest.mark.parametrize(
    "input,expected",
    [([-3, 1, 5, 4, 2], 3), ([3, -2, 0, 1, 2], 4), ([3, 2, 5, 1], 4), ([33, 37, 5], 1)],
)
def test_find_smallest_missing_positive_number(input, expected):
    result = find_smallest_missing_positive_number(input)
    assert result == expected


# Problem Challenge 3 - Find the First K Missing Positive Numbers
@pytest.mark.parametrize(
    "input,k,expected",
    [
        ([3, -1, 4, 5, 5], 3, [1, 2, 6]),
        ([2, 3, 4], 3, [1, 5, 6]),
        ([-2, -3, 4], 2, [1, 2]),
    ],
)
def test_find_first_k_missing_postive_numbers(input, k, expected):
    result = find_first_k_missing_postive_numbers(input, k)
    assert result == expected
