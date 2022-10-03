import pytest
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quicksort import quicksort

# ==============
#  Fixtures
# ==============


@pytest.fixture
def unsorted_array():
    return [5, 6, 3, 2, 6, 6, 4, 1, 3, 6, 3, 8, 9]


@pytest.fixture
def sorted_array():
    return [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 8, 9]


# ==============
#  Unit tests
# ==============


def test_bubble_sort(unsorted_array, sorted_array):
    assert bubble_sort(unsorted_array) == sorted_array


def test_insertion_sort(unsorted_array, sorted_array):
    assert insertion_sort(unsorted_array) == sorted_array


def test_merge_sort(unsorted_array, sorted_array):
    merge_sort(unsorted_array)
    assert unsorted_array == sorted_array


def test_quicksort(unsorted_array, sorted_array):
    quicksort(unsorted_array)
    assert unsorted_array == sorted_array
