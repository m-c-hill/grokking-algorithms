from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node = None):
        self.value = value
        self.next = next

    def __repr__(self):
        curr = self
        linked_list = []
        while curr is not None:
            linked_list.append(str(curr.value))
            curr = curr.next

        return " -> ".join(linked_list)

    def __eq__(self, other) -> bool:
        if self is None and other is None:
            return True

        return self.value == other.value and self.next == other.next
