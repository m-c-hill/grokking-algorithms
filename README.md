# Grokking Algorithms

Algorithm exercises following Design Guru's [Grokking the Coding Interview: Patterns for Coding Questions course](https://designgurus.org/course/grokking-the-coding-interview).

## Chapters

### [Chapter 1 - Sliding Window](chapters/ch01_sliding_window.py)

- Used when looking to find/calculate a value among all sub-arrays within an array.
- For example:
  - Find max sum sub-array of size k
  - Find longest substring with k distinct characters
  - Find smallerst sub-array with sum greater than x
- General approach: Initialise the _window start_ at index 0, then loop through a range equal to the array length, representing the _window end_. The window start is incremented when a certain condition is or isn't met.

#### Problem 1 - Maximum Sum of Size 'K' Subarray

Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size ‘k’.

Example: `arr = [2, 1, 5, 1, 3, 2], k=3 -> Output = 9`

#### Problem 2 - Smallest Subarray with a Greater Sum

Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Example: `arr = [2, 1, 5, 2, 3, 2], S=7 -> Output = 2`

#### Problem 3 - Longest Substring with K Distinct Characters

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example: `str = "araaci", k=2 -> Output = 4`

#### Problem 4 - Fruits into Baskets

A farm has a single row of fruit trees. With two baskets, your goal is to pick as many fruits as possible to be placed in baskets.

The farm has following restrictions:

1. Each basket can have only one type of fruit (with no limit to the number of fruit).
2. Start with any tree, but you can't skip a tree once you have started.
3. Pick exactly one fruit from every tree until you cannot. For example, stop when you have to pick from a third fruit type.

Example: `Fruit=['A', 'B', 'C', 'A', 'C'] -> Output = 3`

#### Problem 5 - Longest Substring with Distinct Characters

Given a string, find the length of the longest substring, which has all distinct characters.

Example: `String="aabccbb" -> Output = 3`

#### Problem 6 - Longest Substring with Same Letters after Replacement

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example: `String="aabccbb", k=2 -> Output = 5`

#### Problem 7 - Longest Subarray with Ones after Replacement

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example: `Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2 -> Output = 6`

#### Problem Challenge 1 - Permutation in a String

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example: `String="oidbcaf", Pattern="abc" -> Output = True`

#### Problem Challenge 2 - String Anagrams

Given a string and a pattern, find all anagrams of the pattern in the given string.

Example: `Input: String="ppqp", Pattern="pq" -> Output = [2, 3, 4]`

#### Problem Challenge 3 - Smallest Window containing Substring

Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example: `String="aabdec", Pattern="abc" -> Output = "abdec"`

#### Problem Challenge 4 - Words Concatenation

Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example: `String="catfoxcat", Words=["cat", "fox"] -> Output = [0, 3]`
