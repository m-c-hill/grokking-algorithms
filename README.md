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

**Completed:** 4 / 7

- Technique to deal with overlapping intervals. This allows us to find overlaps or to merge intervals if they overlap.
- Given intervals `a` and `b`, there will be six different ways these two intervals can relate to each other:
  - `a` and `b` do no overlap, `b` ends after `a`
  - `a` and `b` overlap, `b` ends after `a`
  - `a` completely overlaps `b`
  - `a` and `b` overlap, `a` ends after `b`
  - `b` completely overlaps `a`
  - `a` and `b` do not overlap, `a` ends after `b`

#### Problem 1 - Merge Intervals ✅

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,4], [2,5], [7,9]] -> Output = [[1,5], [7,9]]`

#### Problem 2 - Insert Interval ✅

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example: `intervals = [[1,3], [5,7], [8,12]], new interval = [4,6] -> Output = [[1,3], [4,7], [8,12]]`

#### Problem 3 - Intervals Intersection ✅

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example: `arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]] -> Output = [2, 3], [5, 6], [7, 7]`

#### Problem 4 - Conflicting Appointments ✅

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example: `appointments = [[1,4], [2,5], [7,9]] -> Output = false`

#### Challenge Problem 1 - Problem Challenge 1: Minimum Meeting Rooms ❌

Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example: `meetings = [[1,4], [2,5], [7,9]] -> Output = 2`

#### Challenge Problem 2 - Maximum CPU Load ❌

We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example: `jobs = [[1,4,3], [2,5,4], [7,9,6]] -> Output = 7`

#### Challenge Problem 3 - Problem Challenge 3: Employee Free Time ❌

For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example: `Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]] -> Output: [3,5]`

---

### [Chapter 5 - Cyclic Sort ](chapters/ch05_cyclic_sort.py)

**Completed:** 5 / 8

- For dealing with arrays containing numbers in a given **range**. It is a comparison sorting algorithm which sorts **in-place**.
- It is optimal in terms of the number of memory writes.
- Aim is to compare the number at the ith position with the number at the position if this number were the index.
- General method:
  - Iterate through the array
  - At each position, compare the current number to

#### Problem 1 - Cyclic Sort ✅

We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example: `arr = [3, 1, 5, 4, 2] -> Output = [1, 2, 3, 4, 5]`

#### Problem 2 - Find the Missing Number ✅

We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example: `arr = [4, 0, 3, 1] -> Output = 2`

#### Problem 3 - Find all Missing Numbers ✅

We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example: `arr = [2, 3, 1, 8, 2, 3, 5, 1] -> Output = [4, 6, 7]`

#### Problem 4 - Find the Duplicate Number ✅

We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example: `arr = [1, 4, 4, 3, 2] -> Output = 4`

#### Problem 5 - Find All Duplicate Numbers ✅

We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.

Example: `arr = [3, 4, 4, 5, 5] -> Output = [4, 5]`

#### Problem Challenge 1 ❌

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example: `arr = [3, 1, 2, 5, 2] -> Output = [2, 4]`

#### Problem Challenge 2 ❌

Given an unsorted array containing numbers, find the smallest missing positive number in it. **Note**: Positive numbers start from '1'.

Example: `arr = [-3, 1, 5, 4, 2] -> Output = 3`

#### Problem Challenge 3 ❌

Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example: `arr = [3, -1, 4, 5, 5], k = 3 -> Output = [1, 2, 6]`

---

### [Chapter 6 - In-place Linked List Reversal ](chapters/ch06_linked_list_reversal.py)

**Completed:** 5 / 5

- Linked list composed of a nodes, each having a value and a link to the next node.
- In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.
- In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem.

#### Problem 1 - Reverse a LinkedList ✅

Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

#### Problem 2 - Reverse a Sub-list ✅

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

#### Problem 3 - Reverse every K-element Sub-list ✅

Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

#### Problem Challenge 1 - Reverse alternating K-element Sub-list ✅

Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

#### Problem Challenge 2 - Rotate a LinkedList ✅

Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

---

### [Chapter 7 - Tree Breadth First Search (BFS)](chapters/ch07_breadth_first_search.py)

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

#### Problem 1 - Binary Tree Level Order Traversal ✅

Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

#### Problem 2 - Reverse Level Order Traversal ✅

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

#### Problem 3 - Zigzag Traversal ✅

Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

#### Problem 4 - Level Averages in a Binary Tree ✅

Given a binary tree, populate an array to represent the averages of all of its levels.

#### Problem 5 - Minimum Depth of a Binary Tree ✅

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

#### Problem 6 - Level Order Successor ✅

Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

#### Problem 7 - Connect Level Order Siblings ✅

Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

#### Problem Challenge 1 - Connect All Level Order Siblings ✅

Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

#### Problem Challenge 2 - Right View of a Binary Tree ✅

Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

### [Chapter 8 - Tree Depth First Search (DFS)](chapters/ch08_depth_first_search.py)

**Completed:** 5 / 7

- Alternative binary tree traversal method to breadth first search.
- In a depth first search, you start at the root, and follow one of the branches of the tree as far as possible until either the node you are looking for is found or you hit a leaf node ( a node with no children). If you hit a leaf node, then you continue the search at the nearest ancestor with unexplored children.
- The advantage of DFS over BFS is that it has much lower memory requirements as we don't need to store all the child pointers at each level (as we were doing in BFS with a queue).
- This algorithm has a time complexity of `O(h)` where `h` is the height of the tree.

**BFS vs DFS**

Depending on the data and what you are looking for, either DFS or BFS could be advantageous.

For example, given a family tree if one were looking for someone on the tree who’s still alive, then it would be safe to assume that person would be on the bottom of the tree. This means that a BFS would take a very long time to reach that last level. A DFS, however, would find the goal faster. But, if one were looking for a family member who died a very long time ago, then that person would be closer to the top of the tree. Then, a BFS would usually be faster than a DFS. So, the advantages of either vary depending on the data and what you’re looking for.

#### Problem 1 - Binary Tree Path Sum ✅

Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

#### Problem 2 - All Paths for a Sum ✅

Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

#### Problem 3 - Sum of Path Numbers ✅

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

#### Problem 4 - Path With Given Sequence ✅

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

#### Problem 5 - Count Paths for a Sum ❌

Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

#### Problem Challenge 1 - Tree Diameter ✅

Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

#### Problem Challenge 2 - Path with Maximum Sum ❌

Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.

---

### [Chapter 9 - Two Heaps](chapters/ch09_two_heaps.py)

**Completed:** 2 / 4

- **Heap** is a tree-based data structure which satifies the **heap property**:
  - **Min Heap** - Parent node is always smaller than children to the min value can be accessed in O(1) time.
  - **Max Heap** - Parent node is always larger than children so max value can be accessed in O(1) time.
- Used in problems where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part.
- A min heap is used to find the smallest element, while a max heap is used to find the largest.
- In Python, use the `heapq` library.
  - The default is a min heap data structure where `heappop(heap)` will return the minimum value.
  - To use a max heap in `heapq`, simply invert any of the values that are pushed to the heap `(ie. 3 -> -3, -6 -> 6)`.

#### Problem 1 - Find the Median of a Number Stream ✅

Design a class to calculate the median of a number stream. The class should have the following two methods:

1. `insertNum(int num)`: stores the number in the class
2. `findMedian()`: returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

#### Problem 2 - Sliding Window Median ✅

Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example: `Input: nums=[1, 2, -1, 3, 5], k = 2 -> Output = [1.5, 0.5, 1.0, 4.0]`

#### Problem 3 - Maximize Capital ❌

Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

Example: `Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2 -> Output = 6`

#### Problem Challenge 1: Next Interval ❌

Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

Example: `Input: Intervals [[2,3], [3,4], [5,6]] -> Output = [1, 2, -1]`

---
