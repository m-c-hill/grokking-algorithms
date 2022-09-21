from collections import deque
from typing import List


# Problem 1 - Topological Sort
def topological_sort(vertices: int, edges: List[List[int]]) -> List[int]:
    sorted_order = []

    # edge case
    if vertices <= 0:
        return sorted_order

    # track the children in a list for each parent node, i
    graph = {i: [] for i in range(vertices)}
    # track the number of in degrees for each node
    in_degree = {i: 0 for i in range(vertices)}

    # populate the graph and in-degree hash maps
    for (u, v) in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # find the initial sources
    sources = deque([v for v in in_degree if in_degree[v] == 0])

    while sources:
        node = sources.popleft()
        sorted_order.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # If the number of nodes in the sorted result does not equal the number of
    #   input nodes, then we have found a cycle in the graph. Return null answer.
    if len(sorted_order) != vertices:
        return []

    return sorted_order


# Problem 2 - Tasks Scheduling
def can_tasks_be_scheduled(tasks: int, prerequisites: List[List[int]]) -> bool:
    ordered_tasks = []

    # edge case
    if tasks <= 0:
        return False

    # track the children in a list for each parent node, i
    graph = {i: [] for i in range(tasks)}
    # track the number of in degrees for each node
    in_degree = {i: 0 for i in range(tasks)}

    # populate the graph and in-degree hash maps
    for (u, v) in tasks:
        graph[u].append(v)
        in_degree[v] += 1

    # find the initial sources
    sources = deque([v for v in in_degree if in_degree[v] == 0])

    while sources:
        node = sources.popleft()
        ordered_tasks.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # Return true if we have managed to order the tasks. If we haven't, then we
    #   won't have been able to add all tasks to the sorted_order list. This is
    #   due to a cycle in the graph, so not all tasks can be scheduled.
    return len(ordered_tasks) == tasks


# Problem 3 - Tasks Scheduling Order
def order_tasks(tasks: int, prerequisites: List[List[int]]) -> bool:
    ordered_tasks = []

    # edge case
    if tasks <= 0:
        return False

    # track the children in a list for each parent node, i
    graph = {i: [] for i in range(tasks)}
    # track the number of in degrees for each node
    in_degree = {i: 0 for i in range(tasks)}

    # populate the graph and in-degree hash maps
    for (u, v) in tasks:
        graph[u].append(v)
        in_degree[v] += 1

    # find the initial sources
    sources = deque([v for v in in_degree if in_degree[v] == 0])

    while sources:
        node = sources.popleft()
        ordered_tasks.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(ordered_tasks) != tasks:
        return []  # Unable to schedule tasks due to graph cycle

    return ordered_tasks


# Problem 4 - All Tasks Scheduling Orders
# TODO
def all_tasks_scheduling_orders():
    return


# Problem 5 - Alien Dictionary
def alien_dictionary(words: List[str]) -> str:
    # edge case
    if len(words) == 0:
        return ""

    graph = {}
    in_degree = {}
    for word in words:
        for char in word:
            graph[char] = []
            in_degree[char] = 0

    # populate the graph and in-degree hash maps
    for i in range(len(words) - 1):
        # Compare characters from two words
        w1, w2 = words[i], words[i+1]

        for j in range(min(len(w1), len(w2))):
            u, v = w1[j], w2[j]
            if u != v:
                graph[u].append(v)
                in_degree[v] += 1
                break

    # find the initial sources
    sources = deque([v for v in in_degree if in_degree[v] == 0])
    ordered_chars = []

    while sources:
        node = sources.popleft()
        ordered_chars.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(ordered_chars) != len(graph):
        return ""  # error: graph cycle found

    return "".join(ordered_chars)


# Problem Challenge 1 - Reconstructing a Sequence
# TODO

# Problem Challenge 2 - Minimum Height Trees
# TODO
