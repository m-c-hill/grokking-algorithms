# Grokking Algorithms

Algorithm exercises following Design Guru's [Grokking the Coding Interview: Patterns for Coding Questions course](https://designgurus.org/course/grokking-the-coding-interview).

## Chapters

### [Chapter 1 - Sliding Window](chapters/ch01_sliding_window.py)

**Completed:** 7 / 11

- Used when looking to find/calculate a value among all sub-arrays within an array.
- For example:
  - Find max sum sub-array of size k
  - Find longest substring with k distinct characters
  - Find smallerst sub-array with sum greater than x
- General approach: Initialise the _window start_ at index 0, then loop through a range equal to the array length, representing the _window end_. The window start is incremented when a certain condition is or isn't met.

#### Problem 1 - Maximum Sum of Size 'K' Subarray ✅

Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size ‘k’.

Example: `arr = [2, 1, 5, 1, 3, 2], k=3 -> Output = 9`

#### Problem 2 - Smallest Subarray with a Greater Sum ✅

Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Example: `arr = [2, 1, 5, 2, 3, 2], S=7 -> Output = 2`

#### Problem 3 - Longest Substring with K Distinct Characters ✅

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example: `str = "araaci", k=2 -> Output = 4`

#### Problem 4 - Fruits into Baskets ✅

A farm has a single row of fruit trees. With two baskets, your goal is to pick as many fruits as possible to be placed in baskets.

The farm has following restrictions:

1. Each basket can have only one type of fruit (with no limit to the number of fruit).
2. Start with any tree, but you can't skip a tree once you have started.
3. Pick exactly one fruit from every tree until you cannot. For example, stop when you have to pick from a third fruit type.

Example: `Fruit=['A', 'B', 'C', 'A', 'C'] -> Output = 3`

#### Problem 5 - Longest Substring with Distinct Characters ✅

Given a string, find the length of the longest substring, which has all distinct characters.

Example: `String="aabccbb" -> Output = 3`

#### Problem 6 - Longest Substring with Same Letters after Replacement ✅

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example: `String="aabccbb", k=2 -> Output = 5`

#### Problem 7 - Longest Subarray with Ones after Replacement ✅

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example: `Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2 -> Output = 6`

#### Problem Challenge 1 - Permutation in a String ❌

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example: `String="oidbcaf", Pattern="abc" -> Output = True`

#### Problem Challenge 2 - String Anagrams ❌

Given a string and a pattern, find all anagrams of the pattern in the given string.

Example: `Input: String="ppqp", Pattern="pq" -> Output = [2, 3, 4]`

#### Problem Challenge 3 - Smallest Window containing Substring ❌

Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example: `String="aabdec", Pattern="abc" -> Output = "abdec"`

#### Problem Challenge 4 - Words Concatenation ❌

Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example: `String="catfoxcat", Words=["cat", "fox"] -> Output = [0, 3]`

---

### [Chapter 2 - Two Pointers](chapters/ch02_two_pointers.py)

**Completed:** 1 / 11

- Used on _sorted arrays_ to find a set of elements which fulfil certain constraints.
- In general, two pointers are either:
  - initiated at the extreme ends of the array and are incremented toward the centre,
  - initiated in the centre of the array to then moved outwards,
  - initiated at the start of the array and then move to the right.

#### Problem 1 - Pair with Target Sum ✅

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example: `arr = [1, 2, 3, 4, 6], target=6 -> Output = [1, 3]`

#### Problem 2 - Remove Duplicates ✅

Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once.

The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example: `arr = [2, 3, 3, 3, 6, 9, 9] -> Output = 4`

#### Problem 3 - Squaring a Sorted Array ✅

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example: `arr = [-2, -1, 0, 2, 3] -> Output = [0, 1, 4, 4, 9]`

#### Problem 4 - Triplet Sum to Zero ✅

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example: `arr = [-3, 0, 1, 2, -1, 1, -2] -> Output = [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]`

#### Problem 5 - Triplet Sum Close to Target ✅

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example: `arr = [-2, 0, 1, 2], target = 2 -> Output = 1`

#### Problem 6 - Triplets With Smaller Sum ✅

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that `arr[i] + arr[j] + arr[k] < target` where `i`, `j`, and `k` are three different indices. Write a function to return the count of such triplets.

Example: `arr = [-1, 0, 2, 3], target = 3 -> Output = 2`

#### Problem 7 - Subarrays with Product Less than a Target ✅

Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Example: `arr = [2, 5, 3, 10], target = 30 -> Output = [[2], [5], [2, 5], [3], [5, 3], [10]]`

#### Problem 8 - Dutch National Flag Problem (Dutch Flag Sort) ✅

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

Example: `arr = [1, 0, 2, 1, 0] -> Output = [0, 0, 1, 1, 2]`

#### Problem Challenge 1: Quadruple Sum to Target ❌

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example: `arr = [4, 1, 2, -1, 1, -3], target = 1 -> Output = [-3, -1, 1, 4], [-3, 1, 1, 2]`

#### Problem Challenge 2: Comparing Strings containing Backspaces ❌

Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example: `str1 = "xy#z", str2 = "xzz#" -> Output = True`

#### Problem Challenge 3: Minimum Window Sort ❌

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example: `arr = [1, 2, 5, 3, 7, 10, 9, 12] -> Output = 5`

---

### [Chapter 3 - Fast and Slow ](chapters/ch03_fast_and_slow_pointers.py)

**Completed:** 6 / 7

- Two pointers move through an arrray or linked list at different speeds.
- By moving at different speeds, the algorithm proves that two pointers are bound to meet.
- If a linked list does not have a cycle, the fast pointer will reach the end before the slow pointer. The slow pointer never catches up.
- If there **is** a cycle, the pointers will meet. Just before they meet, either:
  - the fast pointer is one step behind the slow pointer
  - the fast pointer is one two steps behind the slow pointer.
- All distances between pointers reduces to one of these two scenarios.

General method:

- Initialise _f_ and _s_ at head of the list.
- Move f forward two, s forward one.
- If f == s, return true.
- If f is null, return false.

#### Problem 1 - LinkedList Cycle ✅

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

#### Problem 2 - Start of LinkedList Cycle ✅

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

Source: https://www.youtube.com/watch?v=86_tqjlcgNs

#### Problem 3 - Happy Numbers ✅

A number is a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number 1.

For example, 23 is a happy number since:

2<sup>2</sup> + 3<sup>2</sup> = 4 + 9 = 13
1<sup>2</sup> + 3<sup>2</sup> = 1 + 9 = 10
1<sup>2</sup> + 0<sup>2</sup> = 1 + 0 = 1

#### Problem 4 - Middle of Linked List ✅

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

#### Problem Challenge 1: Palindrome LinkedList ✅

Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

#### Problem Challenge 2: Rearrange a LinkedList ✅

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.

#### Problem Challenge 3: Cycle in a Circular Array ❌

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

- If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
- If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

---

### [Chapter 4 - Merge Intervals ](chapters/ch04_merge_intervals.py)

**Completed:** 0 / 7

- Technique to deal with overlapping intervals. This allows us to find overlaps or to merge intervals if they overlap.
- Given intervals `a` and `b`, there will be six different ways these two intervals can relate to each other:
  - `a` and `b` do no overlap, `b` ends after `a`
  - `a` and `b` overlap, `b` ends after `a`
  - `a` completely overlaps `b`
  - `a` and `b` overlap, `a` ends after `b`
  - `b` completely overlaps `a`
  - `a` and `b` do not overlap, `a` ends after `b`

#### Problem 1 - Merge Intervals

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,4], [2,5], [7,9]] -> Output = [[1,5], [7,9]]`

#### Problem 2 - Insert Interval

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,3], [5,7], [8,12]], new interval = [4,6] -> Output = [[1,3], [4,7], [8,12]]`

#### Problem 3 - Intervals Intersection

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example: `arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]] -> Output = [2, 3], [5, 6], [7, 7]`

#### Problem 4 - Conflicting Appointments

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example: `appointments = [[1,4], [2,5], [7,9]] -> Output = false`

#### Challenge Problem 1 - Problem Challenge 1: Minimum Meeting Rooms

Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example: `meetings = [[1,4], [2,5], [7,9]] -> Output = 2`

#### Challenge Problem 2 - Maximum CPU Load

We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example: `jobs = [[1,4,3], [2,5,4], [7,9,6]] -> Output = 7`

#### Challenge Problem 3 - Problem Challenge 3: Employee Free Time

For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example: `Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]] -> Output: [3,5]`
