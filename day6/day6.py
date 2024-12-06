from typing import List, Tuple
from collections import deque


def import_to_matrix(file_path: str) -> List[List[int]]:
    with open(file_path, "r") as file:
        matrix = [list(line.strip()) for line in file.readlines()]
    return matrix


def _rotate_direction(direction):
    return (direction[1], -direction[0])


def solution_part1(matrix: List[List[int]]):
    m, n = len(matrix), len(matrix[0])

    direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    cur_direction = None
    r, c = 0, 0
    for row in range(m):
        for col in range(n):
            if matrix[row][col] in direction_map:
                cur_direction = direction_map[matrix[row][col]]
                r, c = row, col
                break

        if cur_direction:
            break

    visited = set()
    q = deque([(r, c)])
    while q:
        row, col = q.popleft()
        visited.add((row, col))
        new_row, new_col = row + cur_direction[0], col + cur_direction[1]
        if 0 <= new_row < m and 0 <= new_col < n:
            if matrix[new_row][new_col] == "#":
                cur_direction = _rotate_direction(cur_direction)
                new_row, new_col = row + cur_direction[0], col + cur_direction[1]
            q.append((new_row, new_col))

    return len(visited)


if __name__ == "__main__":
    input_array = import_to_matrix("./input.txt")

    print("Part 1 solution: ", solution_part1(input_array))
