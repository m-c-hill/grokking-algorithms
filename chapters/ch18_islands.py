from typing import List, Tuple
from collections import deque

# Problem 1a - Number of Islands (DFS)
def count_islands_dfs(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    result = 0

    for i in range(rows):
        for j in range(columns):
            cell = matrix[i][j]
            if cell == 1:
                result += 1
                visit_island_dfs(matrix, i, j)

    return result


def visit_island_dfs(matrix: List[List[int]], x: int, y: int) -> None:
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return  # Coordinates are outside the boundaries of the matrix
    if matrix[x][y] == 0:
        return  # Found the edge of the island, can stop searching

    if matrix[x][y] == 1:
        matrix[x][y] = 0  # Mark the cell as visited

    # Visit all neighboring cells
    visit_island_dfs(matrix, x + 1, y)
    visit_island_dfs(matrix, x, y + 1)
    visit_island_dfs(matrix, x - 1, y)
    visit_island_dfs(matrix, x, y - 1)


# Problem 1b - Number of Islands (BFS)
def count_islands_bfs(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    result = 0

    for i in range(rows):
        for j in range(columns):
            cell = matrix[i][j]
            if cell == 1:
                result += 1
                visit_island_bfs(matrix, i, j)

    return result


def visit_island_bfs(matrix: List[List[int]], x: int, y: int) -> None:
    neighbors = deque([(x, y)])

    while neighbors:
        row, col = neighbors.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue  # continue, if it is not a valid cell
        if matrix[row][col] == 0:
            continue  # continue if it is a water cell

        matrix[row][col] = 0  # mark cell as visited

        neighbors.extend([(row + 1, col)])  # lower cell
        neighbors.extend([(row - 1, col)])  # upper cell
        neighbors.extend([(row, col + 1)])  # right cell
        neighbors.extend([(row, col - 1)])  # left cell


# Problem 1c - Number of Islands (BFS with visited matrix)
def count_islands_bfs(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    result = 0

    visited = [[False for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            cell = matrix[i][j]
            if cell == 1:
                result += 1
                visit_island_bfs(matrix, visited, i, j)

    return result


def visit_island_bfs(
    matrix: List[List[int]], visited: List[List[int]], x: int, y: int
) -> None:
    neighbors = deque([(x, y)])

    while neighbors:
        row, col = neighbors.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue  # continue, if it is not a valid cell
        if matrix[row][col] == 0 or visited[row][col]:
            continue  # continue if it is a water cell

        visited[row][col] = True  # mark cell as visited

        neighbors.extend([(row + 1, col)])  # lower cell
        neighbors.extend([(row - 1, col)])  # upper cell
        neighbors.extend([(row, col + 1)])  # right cell
        neighbors.extend([(row, col - 1)])  # left cell


# Problem 2 - Biggest Island
def find_biggest_island(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    area = 0

    for i in range(rows):
        for j in range(cols):
            cell = matrix[i][j]
            if cell == 1:
                area = max(area, visit_island_dfs_area(matrix, i, j))

    return area


def visit_island_dfs_area(matrix: List[List[int]], row: int, col: int) -> int:
    if row < 0 or row >= len(matrix) or col < 0 or col > len(matrix[0]):
        return 0

    if matrix[row][col] == 0:
        return 0

    matrix[row][col] = 0  # Mark as visited

    area = 1
    area += visit_island_dfs_area(matrix, row + 1, col)
    area += visit_island_dfs_area(matrix, row - 1, col)
    area += visit_island_dfs_area(matrix, row, col + 1)
    area += visit_island_dfs_area(matrix, row, col - 1)

    return area


# Problem 3 - Flood Fill
def flood_fill(
    matrix: List[List[int]], new_colour: int, coords: Tuple[int]
) -> List[List[int]]:
    x, y = coords
    old_colour = matrix[x][y]
    if matrix[x][y] != new_colour:
        flood_fill_dfs(matrix, x, y, old_colour, new_colour)
    return matrix


def flood_fill_dfs(
    matrix: List[List[int]], x: int, y: int, old_colour: int, new_colour: int
) -> None:
    rows, cols = len(matrix), len(matrix[0])
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if matrix[x][y] != old_colour:
        return

    matrix[x][y] = new_colour

    flood_fill_dfs(matrix, x + 1, y, old_colour, new_colour)
    flood_fill_dfs(matrix, x - 1, y, old_colour, new_colour)
    flood_fill_dfs(matrix, x, y + 1, old_colour, new_colour)
    flood_fill_dfs(matrix, x, y - 1, old_colour, new_colour)


# Problem 4 - Number of Closed Islands
def count_closed_islands(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    closed_island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                if is_closed_island_dfs(matrix, visited, i, j):
                    closed_island_count += 1

    return closed_island_count


def is_closed_island_dfs(
    matrix: List[List[int]], visited: List[List[int]], i: int, j: int
) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return False  # Must have reached a boundary of the map

    if matrix[i][j] == 0 or visited[i][j]:
        return True  #  Island is surrounded by water

    visited[i][j] = True

    return (
        is_closed_island_dfs(matrix, visited, i + 1, j)
        and is_closed_island_dfs(matrix, visited, i - 1, j)
        and is_closed_island_dfs(matrix, visited, i, j + 1)
        and is_closed_island_dfs(matrix, visited, i, j - 1)
    )


# Problem Challenge 1 - Island Perimeter
def find_island_perimeter(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                return island_perimeter_dfs(matrix, visited, i, j)

    return 0


def island_perimeter_dfs(
    matrix: List[List[int]], visited: List[List[int]], i: int, j: int
):
    rows, cols = len(matrix), len(matrix[0])

    if i < 0 or i >= rows or j < 0 or j >= cols:
        return 1  # Found a boundary at edge of map
    if matrix[i][j] == 0:
        return 1  # Found a boundary between land and water

    visited[i][j] == True
    edge_count = 0

    # Visit all neighbouring cells
    edge_count += (
        island_perimeter_dfs(matrix, visited, i + 1, j)
        + island_perimeter_dfs(matrix, visited, i - 1, j)
        + island_perimeter_dfs(matrix, visited, i, j - 1)
        + island_perimeter_dfs(matrix, visited, i, j + 1)
    )

    return edge_count


# Problem Challenge 2 - Number of Distinct Islands
def count_distinct_islands(matrix: List[List[int]]) -> int:
    """
    If two islands are same, their traversal path should be same too.
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_set = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                traversal_path = get_island_traversal_path(matrix, visited, i, j)

    return 0


def get_island_traversal_path(
    matrix: List[List[int]], visited: List[List[int]], i: int, j: int, direction: int
) -> str:
    rows = len(matrix)
    cols = len(matrix[0])

    if i < 0 or i >= rows or j < 0 or j >= cols:
        return ""

    if matrix[i][j] == 0 or visited[i][j]:
        return ""

    visited[i][j] = True

    return (
        direction
        + get_island_traversal_path(matrix, visited, i + 1, j, "D")
        + get_island_traversal_path(matrix, visited, i - 1, j, "U")
        + get_island_traversal_path(matrix, visited, i, j - 1, "L")
        + get_island_traversal_path(matrix, visited, i, j + 1, "R")
    )


# Problem Challenge 3 - Cycle in a Matrix
# TODO