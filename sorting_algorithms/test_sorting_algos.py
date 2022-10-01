import pytest

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

@pytest.fixture
def unsorted_array():
    return [5, 6, 3, 2, 6, 6, 4, 1, 3, 6, 3, 8, 9]

@pytest.fixture
def sorted_array():
    return [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 8, 9]

def test_bubble_sort(unsorted_array, sorted_array):
    assert bubble_sort(unsorted_array) == sorted_array

def test_insertion_sort(unsorted_array, sorted_array):
    assert insertion_sort(unsorted_array) == sorted_array

