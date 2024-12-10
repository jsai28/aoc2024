from typing import List, Tuple


def solution_part1(topographic_map: List[List[int]]) -> int:
    m, n = len(topographic_map), len(topographic_map[0])
    zero_positions = []

    for row in range(m):
        for col in range(n):
            if topographic_map[row][col] == 0:
                zero_positions.append((row, col))

    visited = set()

    def find_trail(row: int, col: int):
        cur_num = topographic_map[row][col]

        if cur_num == 9 and (row, col) not in visited:
            visited.add((row, col))
            return

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in directions:
            new_row, new_col = row + y, col + x
            if 0 <= new_row < m and 0 <= new_col < n:
                new_num = topographic_map[new_row][new_col]

                if new_num == cur_num + 1:
                    find_trail(new_row, new_col)

        return

    result = 0
    for r, c in zero_positions:
        find_trail(r, c)
        result += len(visited)
        visited = set()

    return result


if __name__ == "__main__":
    matrix = []

    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            row = [int(x) for x in row]
            matrix.append(row)

    print("Solution: ", solution_part1(matrix))
