from collections import deque

from dataclasses import TreeNode
from typing import List, Optional

# Problem 1 - Binary Tree Level Order Traversal
def traverse_and_create_array(root: TreeNode) -> list:
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level = []
        level_width = len(queue)

        for _ in range(level_width):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Problem 2 - Reverse Level Order Traversal
def reverse_level_order_traversal(root: TreeNode) -> list:
    result = deque()

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level = []
        level_width = len(queue)

        for _ in range(level_width):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.appendleft(level)

    return list(result)


# Problem 3 - Zigzag Traversal
def zigzag(root: TreeNode) -> list:
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)
    reverse = False

    while queue:
        level = deque()
        level_width = len(queue)

        for _ in range(level_width):
            node = queue.popleft()
            if reverse:
                level.appendleft(node.val)
            else:
                level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)
        reverse = not reverse

    return result


# Problem 4 - Level Averages in a Binary Tree
def level_averages(root: TreeNode) -> list:
    results = []

    queue = deque()
    deque.append(root)

    while queue:
        level = []
        level_length = len(queue)

        for _ in range(level_length):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        level_average = sum(level) / level_length
        results.append(level_average)

    return results


# Problem 5 - Minimum Depth of a Binary Tree
def minimum_depth(root: TreeNode) -> int:
    queue = deque()
    deque.append(root)

    while queue:
        depth += 1
        for _ in queue:
            node = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)


# Problem 6 - Level Order Successor
def level_order_successor(root: TreeNode, target: int) -> Optional[TreeNode]:
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        if node.val == target:
            break

    return queue[0] if queue else None


# Problem 7 - Connect Level Order Siblings
def connect_level_order_siblings(root: TreeNode) -> None:
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        previous_node = None

        for _ in queue:
            current_node = queue.popleft()
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


# Problem Challenge 1 - Connect All Level Order Siblings
def connect_all_level_order_siblings(root: TreeNode) -> None:
    if root is None:
        return

    queue = deque()
    queue.append(root)

    previous_node = None

    while queue:
        current_node = queue.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


# Problem Challenge 2 - Right View of a Binary Tree
def right_view(root: TreeNode) -> List[TreeNode]:
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_width = len(queue)

        for i in range(level_width):
            node = queue.popleft()

            if i == level_width - 1:
                result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
