import math
from typing import List

# =====================
#  Problems
# =====================


# Problem 1 - Maximum Sum of Size 'K' Subarray
def max_sum_of_size_k_sub_array(arr: List[int], k: int) -> int:
    """Find the maximum sum of a size k subarray for array arr"""
    window_start = 0
    current_window_sum = 0
    max_window_sum = 0

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        if window_end >= k - 1:
            max_window_sum = max(current_window_sum, max_window_sum)
            current_window_sum -= arr[window_start]
            window_start += 1

    return max_window_sum


# Problem 2 - Smallest Subarray with a Greater Sum
def smallest_subarray_with_greatest_sum(arr: List[int], target_sum: int) -> int:
    """Find the smallest subarray with a sum greater than or equal to the target sum"""
    window_start = 0
    min_subarry_length = math.inf
    current_window_sum = 0

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        while current_window_sum >= target_sum:
            current_window_length = window_end - window_start + 1
            min_subarry_length = min(min_subarry_length, current_window_length)
            current_window_sum -= arr[window_start]
            window_start += 1

    if min_subarry_length == math.inf:
        return 0
    return min_subarry_length


# Problem 3 - Longest Substring with K Distinct Characters
def longest_substring_with_k_distinct_characters(s: str, k_distinct: int) -> int:
    """Find the longest substring with k distinct characters in a string, s"""
    window_start = 0
    max_substring_length = 0
    character_count = {}

    for window_end in range(len(s)):
        current_character = s[window_end]
        if current_character not in character_count:
            character_count[current_character] = 0
        character_count[current_character] += 1

        while len(character_count) > k_distinct:
            start_character = s[window_start]
            character_count[start_character] -= 1
            if character_count[start_character] == 0:
                del character_count[start_character]
            window_start += 1

        current_window_length = window_end - window_start + 1
        max_substring_length = max(current_window_length, max_substring_length)

    return max_substring_length


# Problem 4 - Fruits into Baskets
def fruit_in_baskets(fruit_trees: List[str]) -> int:
    """Maximise the amount of fruit picked from a line of trees into two baskets"""

    NUMBER_OF_BASKETS = 2

    window_start = 0
    current_fruit_count = 0
    max_total_fruit = 0
    fruit_counter = {}

    for window_end in range(len(fruit_trees)):
        current_fruit = fruit_trees[window_end]
        if current_fruit not in fruit_counter:
            fruit_counter[current_fruit] = 0
        fruit_counter[current_fruit] += 1
        current_fruit_count += 1

        while len(fruit_counter) > NUMBER_OF_BASKETS:
            start_fruit = fruit_trees[window_start]
            fruit_counter[start_fruit] -= 1
            current_fruit_count -= 1
            if fruit_counter[start_fruit] == 0:
                del fruit_counter[start_fruit]
            window_start += 1

        max_total_fruit = max(max_total_fruit, current_fruit_count)

    return max_total_fruit


# Problem 5 - Longest Substring with Distinct Characters
def longest_substring_with_distinct_characters(s: str) -> int:
    window_start = 0
    max_substring_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        current_char = s[window_end]

        # If the character exists in the map, shrink the window from the left
        if current_char in char_index_map:
            window_start = max(char_index_map[current_char] + 1, window_start)

        char_index_map[current_char] = window_end
        window_length = window_end - window_start + 1
        max_substring_length = max(max_substring_length, window_length)

    return max_substring_length


# Problem 6 - Longest Substring with Same Letters after Replacement
def find_longest_substring_after_replacement(s: str, k: int) -> int:
    window_start = 0
    max_substring_length = 0
    max_repeating_char_count = 0
    char_frequency_map = {}

    for window_end in range(len(s)):
        current_char = s[window_end]
        if current_char not in char_frequency_map:
            char_frequency_map[current_char] = 0
        char_frequency_map[current_char] += 1

        max_repeating_char_count = max(
            max_repeating_char_count, char_frequency_map[current_char]
        )

        window_length = window_end - window_start + 1
        valid_substring: bool = window_length - max_repeating_char_count <= k

        if not valid_substring:
            left_char = s[window_start]
            char_frequency_map[left_char] -= 1
            if char_frequency_map[left_char] == 0:
                del char_frequency_map[left_char]
            window_start += 1

        new_window_length = window_end - window_start + 1
        max_substring_length = max(max_substring_length, new_window_length)

    return max_substring_length


# Problem 7 - Longest Subarray with Ones after Replacement
def find_longest_substring_with_ones_after_replacement(arr: List[int], k: int) -> int:
    window_start = 0
    max_subarray_length = 0
    max_ones_count = 0

    for window_end in range(len(arr)):
        current_char = arr[window_end]
        if current_char == 1:
            max_ones_count += 1

        window_length = (window_end + 1) - window_start
        valid_subarray: bool = window_length - max_ones_count <= k

        if not valid_subarray:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        window_length = (window_end + 1) - window_start
        max_subarray_length = max(max_subarray_length, window_length)

    return max_subarray_length


# =====================
#  Problem Challenges
# =====================

# Problem Challenge 1 - Permutation in a String
def permutation_in_a_string():
    pass


# Problem Challenge 2 - String Anagrams
def string_anagrams():
    pass


# Problem Challenge 3 - Smallest Window containing Substring
def smallest_window_containing_substring():
    pass


# Problem Challenge 4 - Words Concatenation
def words_concatenation():
    pass
