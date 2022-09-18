from collections import deque
from itertools import permutations
from math import perm
from typing import List


# Problem 1 - Subsets of a Distinct Set
def find_subsets(arr: List[int]) -> List[int]:
    subsets = [[]]  # Include empty set to start

    for num in arr:
        for i in range(len(subsets)):
            # Take each subset in the results, copy it and append the current number to create a new set.
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)

    return subsets


# Problem 2 - Subsets with Duplicates
def find_subsets_with_duplicates(arr: List[int]) -> List[int]:
    list.sort(arr)
    subsets = [[]]  # Include empty set to start
    end = 0
    for i in range(len(arr)):
        start = 0
        if i > 0 and arr[i] == arr[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, len(subsets)):
            subset = list(subsets[j])
            subset.append(arr[i])
            subsets.append(subset)

    return subsets


# Problem 3 - Permutations
def find_permutations(arr: List[int]):
    results = []
    permutations = deque()
    permutations.append([])

    for num in arr:
        for _ in range(len(permutations)):
            old_perm = permutations.popleft()
            for i in range(len(old_perm) + 1):
                new_perm = list(old_perm)
                new_perm.insert(i, num)
                if len(new_perm) == len(arr):
                    results.append(new_perm)
                else:
                    permutations.append(new_perm)

    return results


# Problem 4 - String Permutations by Changing Case
def case_permutations(s: str):
    permutations = [s]

    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            n_perms = len(permutations)
            for j in range(n_perms):
                new_perm = list(permutations[j])
                new_perm[i] = new_perm[i].swapcase()
                permutations.append("".join(new_perm))

    return permutations


# Deviation - Is String Parenthesis Balanced?
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def is_balanced(s: str) -> bool:
    par = {")": "(", "}": "{", "]": "["}
    par_close = par.keys()
    par_open = par.values()
    stack = Stack()

    for p in s:
        if p in par_open:
            stack.push(p)
        elif p in par_close:
            if stack.is_empty() or stack.pop() != par[p]:
                return False
        else:
            return False

    if stack.is_empty():
        return True
    return False


# Problem 5 - Balanced Parenthesis
def balanced_parenthesis():
    # TODO
    return


# Problem 6 - Unique Generalized Abbreviations
def abbreviations():
    # TODO
    return


# Problem Challenge 1 - Evaluate Expression
def evaluate_expression():
    return


# Problem Challenge 2 - Structurally Unique Binary Search Trees
def unique_bin_trees():
    return


# Problem Challenge 3 - Count of Structurally Unique Binary Search Trees
def count_unique_bin_trees():
    return
