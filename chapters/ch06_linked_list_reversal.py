from curses import KEY_LEFT
import re
from dataclasses.node import Node


# Problem 1 - Reverse a LinkedList
def reverse_linked_list(head: Node) -> Node:
    prev = None

    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev

# Problem 2 - Reverse a Sub-list
def reverse_sub_list(head: Node, start: int, stop: int) -> Node:
    # Note: start and stop indexed from 1, adjust to 0 index
    start, stop = start - 1, stop -1
    
    if start == stop:
        return head

    current, previous = head, None
    i = 0

    while current is not None and i < start:
        previous = current
        current = current.next
        i += 1

    end_of_first_section = previous
    end_of_first_section.next = None
    end_of_subarray = current
    
    while current is not None and i <= stop:
        previous = current
        current = current.next
        i += 1
    
    start_of_subarray = previous
    start_of_subarray.next = None
    reversed_subarray = reverse_linked_list(end_of_subarray)
    
    start_of_third_section = current
    end_of_first_section.next = reversed_subarray
    end_of_subarray.next = start_of_third_section
    
    return head
    

# Problem 3 - Reverse every K-element Sub-list 
def reverse_every_k_element_sub_list(head: Node, k: int) -> Node:
    if head is None or k<= 1:
        return head

    current, previous = head, None
    while True:
        end_of_previous_section = previous
        end_of_reverse_section = current

        i = 0
        while current is not None and i < k:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            i += 1

        if end_of_previous_section is not None:
            end_of_previous_section.next = previous
        else:
            head = previous
        
        end_of_reverse_section.next = current
    
        if current is None:
            break
        
        previous = end_of_reverse_section
    
    return head


# Problem Challenge 1 - Reverse alternating K-element Sub-list 
def reverse_every_alternating_k_element_sub_list(head: Node, k: int) -> Node:
    if head is None or k<= 1:
        return head

    current, previous = head, None
    while True:
        end_of_previous_section = previous
        end_of_reverse_section = current

        i = 0
        while current is not None and i < k:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            i += 1

        if end_of_previous_section is not None:
            end_of_previous_section.next = previous
        else:
            head = previous
        
        end_of_reverse_section.next = current
    
        if current is None:
            break
        
        previous = end_of_reverse_section
    
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1

    return head


# Problem Challenge 2 - Rotate a LinkedList 
def rotate_linked_list_by_k_nodes(head: Node, k: int) -> Node:
    if head is None or head.next is None or k == 0:
        return head

    linked_list_length = 0
    previous, current = None, head

    while current is not None:
        previous = current
        current = current.next
        linked_list_length += 1
    
    final_node = previous
    final_node.next = head

    k = k % linked_list_length
    
    previous, current = None, head
    i = linked_list_length
    while i > k:
        previous = current
        current = current.next
        i -= 1
    
    new_end = previous
    new_end.next = None
    new_head = current

    return new_head
