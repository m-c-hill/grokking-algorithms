import pytest

from chapters.ch10_subsets import *


# Problem 1 - Subsets of a Distinct Set
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 3], [[], [1], [3], [1, 3]]),
        ([1, 5, 3], [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]),
    ],
)
def test_find_subsets(arr, expected):
    res = find_subsets(arr)
    assert res == expected


# Problem 2 - Subsets with Duplicates
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 3, 3], [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]),
        (
            [1, 5, 3, 3],
            [
                [],
                [1],
                [3],
                [1, 3],
                [3, 3],
                [1, 3, 3],
                [5],
                [1, 5],
                [3, 5],
                [1, 3, 5],
                [3, 3, 5],
                [1, 3, 3, 5],
            ],
        ),
    ],
)
def test_find_subsets_with_duplicates(arr, expected):
    res = find_subsets_with_duplicates(arr)
    assert res == expected


# Problem 3 - Permutations
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]),
        ([1, 3, 5], [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]),
    ],
)
def test_permutations(arr, expected):
    res = find_permutations(arr)
    assert res == expected


# Problem 4 - String Permutations by Changing Case
@pytest.mark.parametrize(
    "str1,expected",
    [
        ("ad52", ["ad52", "Ad52", "aD52", "AD52"]),
        ("ab7c", ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]),
    ],
)
def test_case_permutations(str1, expected):
    res = case_permutations(str1)
    assert res == expected


# Problem 5 - Balanced Parenthesis
@pytest.mark.parametrize(
    "N,expected",
    [(2, ["(())", "()()"]), (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])],
)
def test_balanced_parenthesis(N, expected):
    res = balanced_parenthesis(N)
    assert res == expected


# Problem 6 - Unique Generalized Abbreviations
@pytest.mark.parametrize(
    "str1,expected",
    [
        ("BAT", ["BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"]),
        (
            "code",
            [
                "code",
                "cod1",
                "co1e",
                "co2",
                "c1de",
                "c1d1",
                "c2e",
                "c3",
                "1ode",
                "1od1",
                "1o1e",
                "1o2",
                "2de",
                "2d1",
                "3e",
                "4",
            ],
        ),
    ],
)
def test_abbreviations(str1, expected):
    res = abbreviations(str1)
    assert res == expected
