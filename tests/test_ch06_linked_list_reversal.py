import pytest
from chapters.ch06_linked_list_reversal import *

from data_structures.interval import Interval


# =============================
#  Fixtures
# =============================


@pytest.fixture
def linked_list() -> Node:
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)

    return head


@pytest.fixture
def reversed_linked_list() -> Node:
    head = Node(9)
    head.next = Node(8)
    head.next.next = Node(7)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next.next = Node(1)

    return head


@pytest.fixture
def reversed_sub_list() -> Node:
    # p = 3, q = 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(6)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)

    return head


@pytest.fixture
def reversed_sub_list_k_element() -> Node:
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(7)

    return head


@pytest.fixture
def reversed_sub_list_k_element_alternating() -> Node:
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(7)

    return head


@pytest.fixture
def rotated_linked_list() -> Node:
    head = Node(7)
    head.next = Node(8)
    head.next.next = Node(9)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next.next.next = Node(6)

    return head


# =============================
#  Unit tests
# =============================


# Problem 1 - Reverse a LinkedList
def test_reverse_linked_list(linked_list, reversed_linked_list):
    res = reverse_linked_list(linked_list)
    assert res == reversed_linked_list


# Problem 2 - Reverse a Sub-list
def test_reverse_sub_list(linked_list, reversed_sub_list):
    res = reverse_sub_list(linked_list, start=3, stop=6)
    assert res == reversed_sub_list


# Problem 3 - Reverse every K-element Sub-list
def test_reverse_every_k_element_sub_list(linked_list, reversed_sub_list_k_element):
    res = reverse_every_k_element_sub_list(linked_list, k=3)
    assert res == reversed_sub_list_k_element


# Problem Challenge 1 - Reverse alternating K-element Sub-list
def test_reverse_alternating_k_element_sub_list(
    linked_list, reversed_sub_list_k_element_alternating
):
    res = reverse_every_alternating_k_element_sub_list(linked_list, k=3)
    assert res == reversed_sub_list_k_element_alternating


# Problem Challenge 2 - Rotate a LinkedList
def test_rotate_linked_list_by_k_nodes(linked_list, rotated_linked_list):
    res = rotate_linked_list_by_k_nodes(linked_list, k=3)
    assert res == rotated_linked_list
