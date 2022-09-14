import pytest

from chapters.ch01_sliding_window import *

# ==============================================
#  Problems
# ==============================================


# Problem 1 - Maximum Sum of Size 'K' Subarray
def test_max_sum_of_size_k_sub_array():
    arr = [2, 1, 5, 1, 3, 2]
    res = max_sum_of_size_k_sub_array(arr, 3)
    assert res == 9


# Problem 2 - Smallest Subarray with a Greater Sum
@pytest.mark.parametrize(
    "arr,s,expected",
    [([2, 1, 5, 2, 3, 2], 7, 2), ([2, 1, 5, 2, 8], 7, 1), ([3, 4, 1, 1, 6], 8, 3)],
)
def test_smallest_subarray_with_greatest_sum(arr, s, expected):
    res = smallest_subarray_with_greatest_sum(arr, s)
    assert res == expected


# Problem 3 - Longest Substring with K Distinct Characters
@pytest.mark.parametrize(
    "s,k,expected", [("araaci", 2, 4), ("araaci", 1, 2), ("cbbebi", 3, 5)]
)
def test_longest_substring_with_k_distinct_characters(s, k, expected):
    res = longest_substring_with_k_distinct_characters(s, k)
    assert res == expected


# Problem 4 - Fruits into Baskets
@pytest.mark.parametrize(
    "fruit,expected",
    [(["A", "B", "C", "A", "C"], 3), (["A", "B", "C", "B", "B", "C"], 5)],
)
def test_fruit_in_baskets(fruit, expected):
    res = fruit_in_baskets(fruit)
    assert res == expected


# Problem 5 - Longest Substring with Distinct Characters
@pytest.mark.parametrize("s,expected", [("aabccbb", 3), ("abbbb", 2), ("abccde", 3)])
def test_longest_substring_with_distinct_characters(s, expected):
    res = longest_substring_with_distinct_characters(s)
    assert res == expected


# Problem 6 - Longest Substring with Same Letters after Replacement
@pytest.mark.parametrize(
    "s,k,expected", [("aabccbb", 2, 5), ("abbcb", 1, 4), ("abccde", 1, 3)]
)
def test_find_longest_substring_after_replacement(s, k, expected):
    res = find_longest_substring_after_replacement(s, k)
    assert res == expected


# Problem 7 - Longest Subarray with Ones after Replacement
@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
        ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9),
    ],
)
def test_find_longest_substring_after_one_replacement(arr, k, expected):
    res = find_longest_substring_with_ones_after_replacement(arr, k)
    assert res == expected


# ==============================================
#  Problem Challenges
# ==============================================


# Problem Challenge 1 - Permutation in a String
@pytest.mark.parametrize(
    "string,pattern,expected",
    [
        ("oidbcaf", "abc", True),
        ("odicf", "dc", False),
        ("bcdxabcdy", "bcdyabcdx", True),
        ("aaacb", "abc", True),
    ],
)
def test_permutation_in_a_string(string, pattern, expected):
    res = permutation_in_a_string(string, pattern)
    assert res == expected


# Problem Challenge 2 - String Anagrams
@pytest.mark.parametrize(
    "string,pattern,expected", [("ppqp", "pq", [1, 2]), ("abbcabc", "abc", [2, 3, 4])]
)
def test_string_anagrams(string, pattern, expected):
    res = string_anagrams(string, pattern)
    assert res == expected


# Problem Challenge 3 - Smallest Window containing Substring
@pytest.mark.parametrize(
    "string,pattern,expected",
    [
        ("aabdec", "abc", "abdec"),
        ("aabdec", "abac", "aabdec"),
        ("abdbca", "abc", "bca"),
        ("adcad", "abc", ""),
    ],
)
def test_smallest_window_containing_substring(string, pattern, expected):
    res = smallest_window_containing_substring(string, pattern)
    assert res == expected


# Problem Challenge 4 - Words Concatenation
@pytest.mark.parametrize(
    "string,words,expected",
    [
        ("catfoxcat", ["cat", "fox"], [0, 3]),
        ("catcatfoxfox", ["cat", "fox"], [3]),
    ],
)
def test_words_concatenation(string, words, expected):
    res = words_concatenation(string, words)
    assert res == expected
