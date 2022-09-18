from typing import List
from data_structures.tree import TreeNode


# Problem 1 - Binary Tree Path Sum
def has_path_with_sum(root: TreeNode, target_sum: int) -> True:
    if root is None:
        return False

    if root.val == target_sum and root.left is None and root.right is None:
        return True

    return has_path_with_sum(root.left, target_sum - root.val) or has_path_with_sum(
        root.right, target_sum - root.val
    )


# Problem 2 - All Paths for a Sum
def find_paths_with_sum(root: TreeNode, target_sum: int) -> list:
    results = []
    find_paths_with_sum_recursive(root, target_sum, [], results)
    return results


def find_paths_with_sum_recursive(
    current_node: TreeNode,
    target_sum: int,
    current_path: List[int],
    all_paths: List[int],
) -> None:
    if current_node is None:
        return

    current_path.append(current_node.val)

    if (
        current_node.val == target_sum
        and current_node.left is None
        and current_node.right is None
    ):
        all_paths.append(current_path)

    else:
        find_paths_with_sum_recursive(
            current_node.left, target_sum - current_node.val, current_path, all_paths
        )

        find_paths_with_sum_recursive(
            current_node.right, target_sum - current_node.val, current_path, all_paths
        )

    del current_path[-1]


# Problem 3 - Sum of Path Numbers
def sum_of_path_numbers(root: TreeNode) -> int:
    return sum_of_path_numbers(root, 0)


def sum_of_path_numbers_recursive(current_node: TreeNode, path_sum: int) -> int:
    if current_node is None:
        return 0

    path_sum = path_sum * 10 + current_node.val

    if current_node.left is None and current_node.right is None:
        return path_sum

    return sum_of_path_numbers_recursive(
        current_node.left, path_sum
    ) + sum_of_path_numbers_recursive(current_node.right, path_sum)


# Problem 4 - Path With Given Sequence
def find_path_with_sequence(root: TreeNode, sequence: List[int]) -> bool:
    pass


def find_path_with_sequence_recursive(
    current_node: TreeNode, sequence: List[int], sequence_index: int
) -> bool:
    if current_node is None:
        return False

    sequence_length = len(sequence)

    if (
        sequence_index > sequence_length - 1
        or current_node.val != sequence[sequence_index]
    ):
        return False

    if (
        current_node.left is None
        and current_node.right is None
        and sequence_index == sequence_length - 1
    ):
        return True

    return find_path_with_sequence_recursive(
        current_node.left, sequence, sequence_index + 1
    ) or find_path_with_sequence_recursive(
        current_node.right, sequence, sequence_index + 1
    )


# Problem 5 - Count Paths for a Sum
def count_paths_for_a_sum(root: TreeNode, target_sum: int):
    pass


def count_paths_for_a_sum_recursive(root: TreeNode):
    pass


# Problem Challenge 1 - Tree Diameter


def tree_diameter(node: TreeNode):
    """Calculate the current max diameter of a node"""

    if node is None:
        return 0  # Null node has no diameter

    height_left = height_recursive(node.left)
    height_right = height_recursive(node.right)

    diameter = 1 + height_left + height_right  # Diameter of the current node
    diameter_left = tree_diameter(node.left)
    diameter_right = tree_diameter(node.right)

    return max(diameter, diameter_left, diameter_right)


def height_recursive(node: TreeNode):
    """Calculate the maximum height of a node"""
    if node is None:
        return 0  # Null node has no height

    return max(height_recursive(node.left), height_recursive(node.right)) + 1


# Problem Challenge 2 - Path with Maximum Sum
