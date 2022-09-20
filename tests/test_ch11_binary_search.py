import pytest

from chapters.ch11_binary_search import *


# Problem 1: Order-agnostic Binary Search
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([4, 6, 10], 10, 2),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([10, 6, 4], 10, 0),
        ([10, 6, 4], 4, 2),
    ],
)
def test_binary_search_agnostic_order(arr, key, expected):
    result = binary_search(arr, key)
    assert result == expected


# Problem 2: Ceiling of a Number
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([4, 6, 10], 6, 1),
        ([1, 3, 8, 10, 15], 12, 4),
        ([4, 6, 10], 17, -1),
        ([4, 6, 10], -1, 0),
    ],
)
def test_ceiling_of_a_number(arr, key, expected):
    result = ceiling_of_a_number(arr, key)
    assert result == expected


# Problem 3: Next Letter
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        (["a", "c", "f", "h"], "f", "h"),
        (["a", "c", "f", "h"], "b", "c"),
        (["a", "c", "f", "h"], "m", "a"),
        (["a", "c", "f", "h"], "h", "a"),
    ],
)
def test_next_letter(arr, key, expected):
    result = next_letter(arr, key)
    assert result == expected


# Problem 4: Number Range
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([4, 6, 6, 6, 9], 6, [1, 3]),
        ([1, 3, 8, 10, 15], 10, [3, 3]),
        ([1, 3, 8, 10, 15], 12, [-1, -1]),
    ],
)
def test_number_range(arr, key, expected):
    result = find_range(arr, key)
    assert result == expected


# Problem 5: Search in a Sorted Infinite Array
@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 16, 6),
        ([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 11, -1),
        ([1, 3, 8, 10, 15], 15, 4),
        ([1, 3, 8, 10, 15], 200, -1),
    ],
)
def test_infinite_array(arr, key, expected):
    result = infinite_array(arr, key)
    assert result == expected


# Problem 6: Minimum Difference Element
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([4, 6, 10], 7, 6),
        ([4, 6, 10], 4, 4),
        ([1, 3, 8, 10, 15], 12, 10),
        ([4, 6, 10], 17, 10),
    ],
)
def test_search_min_diff_element(arr, key, expected):
    result = search_min_diff_element(arr, key)
    assert result == expected


# Problem 7: Maximum Value in Bitonic Array
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 3, 8, 12, 4, 2], 12),
        ([3, 8, 3, 1], 8),
        ([1, 3, 8, 12], 12),
        ([10, 9, 8], 10),
    ],
)
def test_bitonic_binary_search(arr, expected):
    result = bitonic_binary_search(arr)
    assert result == expected


# Problem Challenge 1: Search Bitonic Array
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([1, 3, 8, 4, 3], 4, 3),
        ([3, 8, 3, 1], 8, 1),
        ([1, 3, 8, 12], 12, 3),
        ([10, 9, 8], 10, 0),
    ],
)
def test_search_bitonic_array(arr, key, expected):
    result = search_bitonic_array(arr, key)
    assert result == expected


# Problem Challege 2: Search in Rotated Array
@pytest.mark.parametrize(
    "arr,key,expected",
    [
        ([10, 15, 1, 3, 8], 15, 1),
        ([4, 5, 7, 9, 10, -1, 2], 10, 4),
    ],
)
def test_search_rotated_array(arr, key, expected):
    result = search_rotated_array(arr, key)
    assert result == expected


# Problem Challenge 3: Rotation Count
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([10, 15, 1, 3, 8], 2),
        ([4, 5, 7, 9, 10, -1, 2], 5),
        ([1, 3, 8, 10], 0),
    ],
)
def test_rotation_count(arr, expected):
    result = rotation_count(arr)
    assert result == expected
