# Grokking Algorithms

Algorithm exercises following Design Guru's [Grokking the Coding Interview: Patterns for Coding Questions course](https://designgurus.org/course/grokking-the-coding-interview).

## [Chapter 1 - Sliding Window](chapters/ch01_sliding_window.py)

**Completed:** 7 / 11

- Used when looking to find/calculate a value among all sub-arrays within an array.
- For example:
  - Find max sum sub-array of size k
  - Find longest substring with k distinct characters
  - Find smallerst sub-array with sum greater than x
- General approach: Initialise the _window start_ at index 0, then loop through a range equal to the array length, representing the _window end_. The window start is incremented when a certain condition is or isn't met.

### Problem 1 - Maximum Sum of Size 'K' Subarray ✅

Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size ‘k’.

Example: `arr = [2, 1, 5, 1, 3, 2], k=3 -> Output = 9`

### Problem 2 - Smallest Subarray with a Greater Sum ✅

Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Example: `arr = [2, 1, 5, 2, 3, 2], S=7 -> Output = 2`

### Problem 3 - Longest Substring with K Distinct Characters ✅

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example: `str = "araaci", k=2 -> Output = 4`

### Problem 4 - Fruits into Baskets ✅

A farm has a single row of fruit trees. With two baskets, your goal is to pick as many fruits as possible to be placed in baskets.

The farm has following restrictions:

1. Each basket can have only one type of fruit (with no limit to the number of fruit).
2. Start with any tree, but you can't skip a tree once you have started.
3. Pick exactly one fruit from every tree until you cannot. For example, stop when you have to pick from a third fruit type.

Example: `Fruit=['A', 'B', 'C', 'A', 'C'] -> Output = 3`

### Problem 5 - Longest Substring with Distinct Characters ✅

Given a string, find the length of the longest substring, which has all distinct characters.

Example: `String="aabccbb" -> Output = 3`

### Problem 6 - Longest Substring with Same Letters after Replacement ✅

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example: `String="aabccbb", k=2 -> Output = 5`

### Problem 7 - Longest Subarray with Ones after Replacement ✅

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example: `Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2 -> Output = 6`

### Problem Challenge 1 - Permutation in a String ❌

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example: `String="oidbcaf", Pattern="abc" -> Output = True`

### Problem Challenge 2 - String Anagrams ❌

Given a string and a pattern, find all anagrams of the pattern in the given string.

Example: `Input: String="ppqp", Pattern="pq" -> Output = [2, 3, 4]`

### Problem Challenge 3 - Smallest Window containing Substring ❌

Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example: `String="aabdec", Pattern="abc" -> Output = "abdec"`

### Problem Challenge 4 - Words Concatenation ❌

Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example: `String="catfoxcat", Words=["cat", "fox"] -> Output = [0, 3]`

---

##[Chapter 2 - Two Pointers](chapters/ch02_two_pointers.py)

**Completed:** 1 / 11

- Used on _sorted arrays_ to find a set of elements which fulfil certain constraints.
- In general, two pointers are either:
  - initiated at the extreme ends of the array and are incremented toward the centre,
  - initiated in the centre of the array to then moved outwards,
  - initiated at the start of the array and then move to the right.

### Problem 1 - Pair with Target Sum ✅

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example: `arr = [1, 2, 3, 4, 6], target=6 -> Output = [1, 3]`

### Problem 2 - Remove Duplicates ✅

Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once.

The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example: `arr = [2, 3, 3, 3, 6, 9, 9] -> Output = 4`

### Problem 3 - Squaring a Sorted Array ✅

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example: `arr = [-2, -1, 0, 2, 3] -> Output = [0, 1, 4, 4, 9]`

### Problem 4 - Triplet Sum to Zero ✅

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example: `arr = [-3, 0, 1, 2, -1, 1, -2] -> Output = [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]`

### Problem 5 - Triplet Sum Close to Target ✅

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example: `arr = [-2, 0, 1, 2], target = 2 -> Output = 1`

### Problem 6 - Triplets With Smaller Sum ✅

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that `arr[i] + arr[j] + arr[k] < target` where `i`, `j`, and `k` are three different indices. Write a function to return the count of such triplets.

Example: `arr = [-1, 0, 2, 3], target = 3 -> Output = 2`

### Problem 7 - Subarrays with Product Less than a Target ✅

Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Example: `arr = [2, 5, 3, 10], target = 30 -> Output = [[2], [5], [2, 5], [3], [5, 3], [10]]`

### Problem 8 - Dutch National Flag Problem (Dutch Flag Sort) ✅

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

Example: `arr = [1, 0, 2, 1, 0] -> Output = [0, 0, 1, 1, 2]`

### Problem Challenge 1: Quadruple Sum to Target ❌

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example: `arr = [4, 1, 2, -1, 1, -3], target = 1 -> Output = [-3, -1, 1, 4], [-3, 1, 1, 2]`

### Problem Challenge 2: Comparing Strings containing Backspaces ❌

Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example: `str1 = "xy#z", str2 = "xzz#" -> Output = True`

### Problem Challenge 3: Minimum Window Sort ❌

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example: `arr = [1, 2, 5, 3, 7, 10, 9, 12] -> Output = 5`

---

##[Chapter 3 - Fast and Slow ](chapters/ch03_fast_and_slow_pointers.py)

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

### Problem 1 - LinkedList Cycle ✅

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

### Problem 2 - Start of LinkedList Cycle ✅

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

Source: https://www.youtube.com/watch?v=86_tqjlcgNs

### Problem 3 - Happy Numbers ✅

A number is a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number 1.

For example, 23 is a happy number since:

2<sup>2</sup> + 3<sup>2</sup> = 4 + 9 = 13
1<sup>2</sup> + 3<sup>2</sup> = 1 + 9 = 10
1<sup>2</sup> + 0<sup>2</sup> = 1 + 0 = 1

### Problem 4 - Middle of Linked List ✅

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

### Problem Challenge 1: Palindrome LinkedList ✅

Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

### Problem Challenge 2: Rearrange a LinkedList ✅

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.

### Problem Challenge 3: Cycle in a Circular Array ❌

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

- If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
- If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

---

##[Chapter 4 - Merge Intervals ](chapters/ch04_merge_intervals.py)

**Completed:** 4 / 7

- Technique to deal with overlapping intervals. This allows us to find overlaps or to merge intervals if they overlap.
- Given intervals `a` and `b`, there will be six different ways these two intervals can relate to each other:
  - `a` and `b` do no overlap, `b` ends after `a`
  - `a` and `b` overlap, `b` ends after `a`
  - `a` completely overlaps `b`
  - `a` and `b` overlap, `a` ends after `b`
  - `b` completely overlaps `a`
  - `a` and `b` do not overlap, `a` ends after `b`

### Problem 1 - Merge Intervals ✅

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,4], [2,5], [7,9]] -> Output = [[1,5], [7,9]]`

### Problem 2 - Insert Interval ✅

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,3], [5,7], [8,12]], new interval = [4,6] -> Output = [[1,3], [4,7], [8,12]]`

### Problem 3 - Intervals Intersection ✅

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example: `arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]] -> Output = [2, 3], [5, 6], [7, 7]`

### Problem 4 - Conflicting Appointments ✅

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example: `appointments = [[1,4], [2,5], [7,9]] -> Output = false`

### Challenge Problem 1 - Problem Challenge 1: Minimum Meeting Rooms ❌

Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example: `meetings = [[1,4], [2,5], [7,9]] -> Output = 2`

### Challenge Problem 2 - Maximum CPU Load ❌

We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example: `jobs = [[1,4,3], [2,5,4], [7,9,6]] -> Output = 7`

### Challenge Problem 3 - Problem Challenge 3: Employee Free Time ❌

For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example: `Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]] -> Output: [3,5]`

---

##[Chapter 5 - Cyclic Sort ](chapters/ch05_cyclic_sort.py)

**Completed:** 5 / 8

- For dealing with arrays containing numbers in a given **range**. It is a comparison sorting algorithm which sorts **in-place**.
- It is optimal in terms of the number of memory writes.
- Aim is to compare the number at the ith position with the number at the position if this number were the index.
- General method:
  - Iterate through the array
  - At each position, compare the current number to

### Problem 1 - Cyclic Sort ✅

We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example: `arr = [3, 1, 5, 4, 2] -> Output = [1, 2, 3, 4, 5]`

### Problem 2 - Find the Missing Number ✅

We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example: `arr = [4, 0, 3, 1] -> Output = 2`

### Problem 3 - Find all Missing Numbers ✅

We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example: `arr = [2, 3, 1, 8, 2, 3, 5, 1] -> Output = [4, 6, 7]`

### Problem 4 - Find the Duplicate Number ✅

We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example: `arr = [1, 4, 4, 3, 2] -> Output = 4`

### Problem 5 - Find All Duplicate Numbers ✅

We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.

Example: `arr = [3, 4, 4, 5, 5] -> Output = [4, 5]`

### Problem Challenge 1 ❌

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example: `arr = [3, 1, 2, 5, 2] -> Output = [2, 4]`

### Problem Challenge 2 ❌

Given an unsorted array containing numbers, find the smallest missing positive number in it. **Note**: Positive numbers start from '1'.

Example: `arr = [-3, 1, 5, 4, 2] -> Output = 3`

### Problem Challenge 3 ❌

Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example: `arr = [3, -1, 4, 5, 5], k = 3 -> Output = [1, 2, 6]`

---

##[Chapter 6 - In-place Linked List Reversal ](chapters/ch06_linked_list_reversal.py)

**Completed:** 5 / 5

- Linked list composed of a nodes, each having a value and a link to the next node.
- In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.
- In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem.

### Problem 1 - Reverse a LinkedList ✅

Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

### Problem 2 - Reverse a Sub-list ✅

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

### Problem 3 - Reverse every K-element Sub-list ✅

Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

### Problem Challenge 1 - Reverse alternating K-element Sub-list ✅

Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

### Problem Challenge 2 - Rotate a LinkedList ✅

Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

---

##[Chapter 7 - Tree Breadth First Search (BFS)](chapters/ch07_breadth_first_search.py)

**Completed:** 9 / 9

- **Binary Tree:** Data structure consisting of nodes. Each parent node has a left and right child.
- A **Binary Search Tree** is an ordered version of a binary tree, in which the left node value is less than the parent node, while the right node is greater than the parent node.
- In a breadth first search, you start at the root node, and then scan each node in the first level starting from the leftmost node, moving towards the right. Then you continue scanning the second level (starting from the left) and the third level, and so on until you’ve scanned all the nodes, or until you find the actual node that you were searching for.
- To do this, a queue is used. Example, representing a tree with arrays:
  - Push the root to the queue
  - Iterate through the queue until the queue is empty. With each iteration, count the elements in the queue, N.
  - Remove N nodes from the queue and push values to an array.
  - After removing each node, push both its children to the queue.
  - Continue to iterate until the queue is empty.
- Use when:
  - you know the solution is not far from the route of the tree
  -

### Problem 1 - Binary Tree Level Order Traversal ✅

Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

### Problem 2 - Reverse Level Order Traversal ✅

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

### Problem 3 - Zigzag Traversal ✅

Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

### Problem 4 - Level Averages in a Binary Tree ✅

Given a binary tree, populate an array to represent the averages of all of its levels.

### Problem 5 - Minimum Depth of a Binary Tree ✅

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

### Problem 6 - Level Order Successor ✅

Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

### Problem 7 - Connect Level Order Siblings ✅

Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

### Problem Challenge 1 - Connect All Level Order Siblings ✅

Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

### Problem Challenge 2 - Right View of a Binary Tree ✅

Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

##[Chapter 8 - Tree Depth First Search (DFS)](chapters/ch08_depth_first_search.py)

**Completed:** 5 / 7

- Alternative binary tree traversal method to breadth first search.
- In a depth first search, you start at the root, and follow one of the branches of the tree as far as possible until either the node you are looking for is found or you hit a leaf node ( a node with no children). If you hit a leaf node, then you continue the search at the nearest ancestor with unexplored children.
- The advantage of DFS over BFS is that it has much lower memory requirements as we don't need to store all the child pointers at each level (as we were doing in BFS with a queue).
- This algorithm has a time complexity of `O(h)` where `h` is the height of the tree.

**BFS vs DFS**

Depending on the data and what you are looking for, either DFS or BFS could be advantageous.

For example, given a family tree if one were looking for someone on the tree who’s still alive, then it would be safe to assume that person would be on the bottom of the tree. This means that a BFS would take a very long time to reach that last level. A DFS, however, would find the goal faster. But, if one were looking for a family member who died a very long time ago, then that person would be closer to the top of the tree. Then, a BFS would usually be faster than a DFS. So, the advantages of either vary depending on the data and what you’re looking for.

### Problem 1 - Binary Tree Path Sum ✅

Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

### Problem 2 - All Paths for a Sum ✅

Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

### Problem 3 - Sum of Path Numbers ✅

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

### Problem 4 - Path With Given Sequence ✅

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

### Problem 5 - Count Paths for a Sum ❌

Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

### Problem Challenge 1 - Tree Diameter ✅

Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

### Problem Challenge 2 - Path with Maximum Sum ❌

Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.

---

##[Chapter 9 - Two Heaps](chapters/ch09_two_heaps.py)

**Completed:** 2 / 4

- **Heap** is a tree-based data structure which satifies the **heap property**:
  - **Min Heap** - Parent node is always smaller than children to the min value can be accessed in O(1) time.
  - **Max Heap** - Parent node is always larger than children so max value can be accessed in O(1) time.
- Used in problems where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part.
- A min heap is used to find the smallest element, while a max heap is used to find the largest.
- In Python, use the `heapq` library.
  - The default is a min heap data structure where `heappop(heap)` will return the minimum value.
  - To use a max heap in `heapq`, simply invert any of the values that are pushed to the heap `(ie. 3 -> -3, -6 -> 6)`.

### Problem 1 - Find the Median of a Number Stream ✅

Design a class to calculate the median of a number stream. The class should have the following two methods:

1. `insertNum(int num)`: stores the number in the class
2. `findMedian()`: returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

### Problem 2 - Sliding Window Median ✅

Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example: `Input: nums=[1, 2, -1, 3, 5], k = 2 -> Output = [1.5, 0.5, 1.0, 4.0]`

### Problem 3 - Maximize Capital ❌

Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

Example: `Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2 -> Output = 6`

### Problem Challenge 1: Next Interval ❌

Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

Example: `Input: Intervals [[2,3], [3,4], [5,6]] -> Output = [1, 2, -1]`

---

##[Chapter 10 - Subsets](chapters/ch10_subsets.py)

**Completed:** 4 / 9

- [Breadth first search (BFS)](chapters/ch07_breadth_first_search.py) is used to deal with permutations and combinations.
- For example, to find all distinct subsets for an array:
  - Start with an empty set.
  - With each iteration, copy the current results and add the current number to these arrays.

### Problem 1 - Subsets of a Distinct Set ✅

Given a set with distinct elements, find all of its distinct subsets.

```
Input: [1, 3]
Output: [], [1], [3], [1,3]
```

### Problem 2 - Subsets with Duplicates ✅

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

```
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
```

### Problem 3 - Permutations ✅

Given a set of distinct numbers, find all of its permutations.

```
Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
```

### Problem 4 - String Permutations by Changing Case ✅

Given a string, find all of its permutations preserving the character sequence but changing case.

```
Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
```

### Problem 5 - Balanced Parenthesis ❌

For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

```
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
```

### Problem 6 - Unique Generalized Abbreviations ❌

Given a word, write a function to generate all of its unique generalized abbreviations.

A generalized abbreviation of a word can be generated by replacing each substring of the word with the count of characters in the substring. Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After replacing these substrings in the actual word by the count of characters, we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.

```
Input: "BAT"
Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
```

### Problem Challenge 1 - Evaluate Expression ❌

Given an expression containing digits and operations (+, -, \*), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

```
Input: "1+2*3"
Output: 7, 9
Explanation:
  1+(2*3) => 7
  (1+2)*3 => 9
```

### Problem Challenge 2 - Structurally Unique Binary Search Trees ❌

Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

```
Input: 2
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:
```

### Problem Challenge 3 - Count of Structurally Unique Binary Search Trees ❌

Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

```
Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.
```

---

##[Chapter 11 - Modified Binary Search](chapters/ch11_binary_search.py)

**Completed:** 9 / 10

- Most efficient algorithm to search for an element in a sorted array / linked list.

### Problem 1 - Order-agnostic Binary Search ✅

Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

```
Input: [4, 6, 10], key = 10
Output: 2

Input: [10, 6, 4], key = 10
Output: 0
```

### Problem 2 - Ceiling of a Number ✅

Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

```
Input: [4, 6, 10], key = 6
Output: 1

Input: [4, 6, 10], key = -1
Output: 0
```

### Problem 3 - Next Letter ✅

Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

```
Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
```

### Problem 4 - Number Range ✅

Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

```
Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
```

### Problem 5 - Search in a Sorted Infinite Array ❌

Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

```
Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
```

### Problem 6 - Minimum Difference Element ✅

Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

```
Input: [4, 6, 10], key = 7
Output: 6
```

### Problem 7 - Bitonic Array Maximum ✅

Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index `i` in the array `arr[i] != arr[i+1]`.

```
Input: [1, 3, 8, 12, 4, 2]
Output: 12
```

### Problem Challenge 1 - Search Bitonic Array ✅

Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index `i` in the array `arr[i] != arr[i+1]`.

Write a function to return the index of the ‘key’. If the 'key' appears more than once, return the smaller index. If the ‘key’ is not present, return -1.

```
Input: [1, 3, 8, 4, 3], key=4
Output: 3
```

### Problem Challenge 2 - Search in Rotated Array ✅

Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

```
Input: [10, 15, 1, 3, 8], key = 15
Output: 1
```

### Problem Challenge 3 - Rotation Count ✅

Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

```
Input: [10, 15, 1, 3, 8]
Output: 2
```

---

##[Chapter 12 - Bitwise XOR](chapters/ch12_bitwise_xor.py)

**Completed:** 4 / 4

- A bitwise XOR is a **binary operation** that takes two bit patterns of equal length and perform the logical exclusive OR operation on each corresponding pair.
- XOR: if either bits A or B are 1 (but not both), return 1. Else return 0.

```bash
| A | B | A XOR B |
-------------------
| 0 | 0 |    0    |
| 1 | 0 |    1    |
| 0 | 1 |    1    |
| 1 | 1 |    0    |
```

Simple rules:

- XOR of a number with itself is always 0:

```
1 ^ 1 = 0
29 ^ 29 = 0
```

- The XOR of a number with 0 returns the same number:

```
1 ^ 0 = 1
31 ^ 0 = 31
```

- XOR is associative and commutative:

```
(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
```

Example:

```bash
3 ^ 4

|  3  |  0  1  1
|  4  |  1  0  0
| 3^4 |  1  1  1

3 ^ 4 = b111 = 7
```

### Problem 1 - Single Number ✅

In a non-empty array of integers, every number appears twice except for one, find that single number.

```bash
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
```

### Problem 2 - Two Single Numbers ✅

In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

```bash
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
```

### Problem 3 - Complement of Base 10 Number ✅

Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

```bash
Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.
```

### Problem Challenge 1 - Flip and Invert an Image ✅

Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

```bash
Input: [
  [1,0,1],
  [1,1,1],
  [0,1,1]
]
Output: [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]
```

---

##[Chapter 13 - Top 'K' Elements](chapters/ch13_top_k_elements.py)

**Completed:** 9 / 14

- Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
- Use a heap to keep track of 'k' elements.
- **Heap** is a tree-based data structure which satifies the **heap property**:
  - **Min Heap** - Parent node is always smaller than children to the min value can be accessed in O(1) time.
  - **Max Heap** - Parent node is always larger than children so max value can be accessed in O(1) time.

### Problem 1 - Top 'K' Numbers ✅

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

```bash
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
```

### Problem 2 - Kth Smallest Number ✅

Given an unsorted array of numbers, find Kth smallest number in it.

```bash
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
```

### Problem 3 - 'K' Closest Points to the Origin ✅

Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.

```bash
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
```

### Problem 4 - Connect Ropes ✅

Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.

```bash
Input: [1, 3, 11, 5]
Output: 33
```

### Problem 5 - Top 'K' Frequent Numbers ✅

Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

```bash
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
```

### Problem 6 - Frequency Sort ✅

Given a string, sort it based on the decreasing frequency of its characters.

```bash
Input: "Programming"
Output: "rrggmmPiano"
```

### Problem 7 - Kth Largest Number in a Stream ❌

Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

- The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
- The class should expose a function add(int num) which will store the given number and return the Kth largest number.

```bash
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
3. Calling add(4) should still return '6'.
```

### Problem 8 - 'K' Closest Numbers ✅

Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

```bash
Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
```

### Problem 9 - Maximum Distinct Elements ✅

Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

```bash
Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
```

### Problem 10 - Sum of Elements ✅

Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

```bash
Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
```

### Problem 11 - Rearrange String ❌

Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

```bash
Input: "aappp"
Output: "papap"
```

### Problem Challenge 1: Rearrange String K Distance Apart ❌

Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

```bash
Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
```

### Problem Challenge 2: Scheduling Tasks ❌

You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

```bash
Input: [a, a, a, b, c, c], K=2
Output: 7
```

### Problem Challenge 3: Frequency Stack ❌

Design a class that simulates a Stack data structure, implementing the following two operations:

1. `push(int num)`: Pushes the number ‘num’ on the stack.
2. `pop()`: Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

```bash
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
```

---

##[Chapter 14 - K Way Merge](chapters/ch14_k_way_merge.py)

**Completed:** 5 / 5

- Pattern is used to solve problems when presented with a **list of sorted arrays**.
- Whenever we are given ‘K’ sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays.
  - The smallest element of each sorted array can be pushed to a min heap to get the overall minimum.
  - While inserting elements to the min heap, keep track of which array the element came from.
  - Then, remove the top element from the heap to get the smallest element and push the next element from the same array, to which this smallest element belonged, to the heap.
  - This can be repeated to make a sorted traversal of all elements.

### Problem 1 - Merge K Sorted Lists ✅

Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

```bash
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
```

### Problem 2 - Kth Smallest Number in M Sorted Lists ✅

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

```bash
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
```

### Problem 3 - Kth Smallest Number in a Sorted Matrix ✅

Given an `N × N` matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

```bash
Input: Matrix=[
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
  ],
  K=5
Output: 7
```

### Problem 4 - Smallest Number Range ✅

Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

```bash
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
```

### Problem Challenge 1 - K Pairs with Largest Sums ✅

Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

```bash
Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6]
```

---

##[Chapter 16 - Topological Sort](chapters/ch16_topological_sort.py)

**Completed:** 4 / 7

- Topological Sort is used to find a linear ordering of elements that have dependencies on each other.
- For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.
- Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (`U`, `V`) from vertex `U` to vertex `V`, `U` comes before `V` in the ordering.

The basic idea behind the topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from `U` to `V` then `U ≤ V`

**Source:** Any node that has no incoming edge and has only outgoing edges is called a source.
**Sink:** Any node that has only incoming edges and no outgoing edge is called a sink.

- We can say that a **topological ordering** starts with one of the **sources** and ends at one of the **sinks**.
- A topological ordering is possible only when the graph has no **directed cycles**, _i.e. if the graph is a Directed Acyclic Graph (DAG)._
- If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.

Method

- To find the topological sort of a graph we can traverse the graph in a Breadth First Search (BFS) way.
  - Save all sources to a sorted list.
  - Remove all sources and their edges from the graph.
  - Once removed, we will have new sources, so repeat the above steps until all vertices are visited.

Algorithm

- Store graph in a hash map, where each parent node will correspond to a list of all its children.
- Use another hash map to store the number of in-degrees. Any vertex with 0 will be a source.
- Store any vertices with 0 in-degrees in a queue.
- For each source:
  - Add it to a sorted list.
  - Get all of its children from the graph.
  - Decrement the in-degree of each child by 1.
  - If a child's in-degree becomes 0, add it to the sources queue.
  - Repeat until queue is empty.

### Problem 1 - Topological Sort ✅

Given a directed graph, find the topological ordering of its vertices.

```bash
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
```

### Problem 2 - Tasks Scheduling ✅

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

```bash
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2]
```

### Problem 3 - Tasks Scheduling Order ✅

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

```bash
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
to finish before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
```

### Problem 4 - All Tasks Scheduling Orders ❌

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

```bash
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
```

### Problem 5 - Alien Dictionary ✅

There is a dictionary containing words from an alien language for which we don’t know the ordering of the letters. Write a method to find the correct order of the letters in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its letters.

```bash
Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
```

### Problem Challenge 1 - Reconstructing a Sequence ❌

Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

```bash
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
```

### Problem Challenge 2 - Minimum Height Trees ❌

We are given an undirected graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

```bash
Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
```

---

---

##[Chapter 18 - Islands (Matrix Traversal)](chapters/ch18_islands.py)

**Completed:** 0 / 7

- The Island pattern describes all the efficient ways to traverse a matrix.

- An **island** is a connected set of `1`s (land) and is surrounded by either an edge or `0`s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

- A **closed island** is an island that is totally surrounded by 0s (i.e., water). This means all horizontally and vertically connected cells of a closed island are water. This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

### Problem 1 - Number of Islands ✅

Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

### Problem 2 - Biggest Island ✅

Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a function to return the area of the biggest island.

### Problem 3 - Flood Fill ✅

Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

Given a matrix, a starting cell, and a color, flood fill the matrix.

### Problem 4 - Number of Closed Islands ✅

Write a function to find the number of closed islands in the given matrix.

### Problem Challenge 1 - Island Perimeter ✅

You are given a 2D matrix containing only 1s (land) and 0s (water).

There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1.

The given matrix has only one island, write a function to find the perimeter of that island.

### Problem Challenge 2 - Number of Distinct Islands ✅

Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

Write a function to find the number of distinct islands in the given matrix.

### Problem Challenge 3 - Cycle in a Matrix ❌

You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.

A cycle is a path in the matrix that starts and ends at the same cell and has four or more cells. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.

Write a function to find if the matrix has a cycle.
