from ..dataclasses.node import Node


# Problem 1 - LinkedList Cycle
def linked_list_has_cycle(head: Node) -> bool:
    # Initially, both pointers point toward the head of the linked list
    s, f = head, head

    # Loop until linked list terminates (f has reached the last node)
    while f is not None and f.next is not None:
        # The slow pointer then takes one step, while the fast pointer takes two
        s = s.next
        f = s.next.next

        if s == f:
            return True  # cycle has been found

    return False


# Problem 2 - Start of LinkedList Cycle
def find_start_of_linked_list_cycle(head: Node) -> Node:
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # Once a collision point has been found, the number of steps to take from
        # this point to the start of the cycle is equal to the number of steps
        # to take from the origin head to the start of the cycle.
        if fast == slow:
            cycle_start = head

            while cycle_start != slow:
                cycle_start = cycle_start.next
                slow = slow.next

    return cycle_start


# Problem 3 - Happy Numbers
def is_happy_number(num: int) -> bool:
    """Return true if a number is a happy number"""
    slow = num
    fast = num

    while True:
        slow = square_digits(slow)
        fast = square_digits(square_digits(fast))

        if slow == fast:
            break

    return slow == 1


def square_digits(num: int) -> int:
    """Helper function to square the digits of a number and sum them"""
    res = 0

    while num > 0:
        rem = num % 10  # Get current digit as remainder from 10 div
        num = (
            num // 10
        )  # Remove the current digit from the number using integer division
        res += rem * rem  # Add the square of the remainder to the result

    return res


# Problem 4 - Middle of Linked List
def find_middle_of_linked_list(head: Node) -> Node:
    f, s = head, head

    while f is not None and f.next is not None:
        f = f.next.next
        s = s.next

    return s


# Problem Challenge 1: Palindrome LinkedList
def linked_list_palindrome(head: Node) -> bool:

    if head is None or head.next is None:
        return True

    middle = find_middle_of_linked_list(head)

    second_half_reversed = reverse_linked_list(middle)

    while head is not None and second_half_reversed is not None:
        if head.value != second_half_reversed.value:
            break

        head = head.next
        second_half_reversed = second_half_reversed.next

    return head is None or second_half_reversed is None


def reverse_linked_list(head: Node) -> Node:
    prev = None

    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev


# Problem Challenge 2: Rearrange a LinkedList
def rearrange_a_linked_list(head: Node) -> None:
    """
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.

    Original: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
    Result:   1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null
    """

    if head is None or head.next is None:
        return

    middle = find_middle_of_linked_list(head)

    second_half_reversed = reverse_linked_list(middle)

    while head_first_half.next is not None and second_half_reversed is not None:
        temp = head_first_half.next
        head_first_half.next = second_half_reversed
        head_first_half = temp

        temp = second_half_reversed.next
        second_half_reversed.next = head_first_half
        second_half_reversed = temp

    # Ensure final node is null
    head_first_half.next = None


# Problem Challenge 3: Cycle in a Circular Array
# TODO
