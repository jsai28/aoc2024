from typing import List


def solution_part1(antenna_list: List[List[str]]) -> int:
    result = set()
    antenna_map = {}
    m, n = len(antenna_list), len(antenna_list[0])

    for row in range(m):
        for col in range(n):
            value = antenna_list[row][col]
            if value == ".":
                continue

            if not value in antenna_map:
                antenna_map[value] = []
            antenna_map[value].append((row, col))

    for locations in antenna_map.values():
        if len(locations) == 1:
            continue

        for i in range(len(locations) - 1):
            row1, col1 = locations[i]
            for j in range(i + 1, len(locations)):
                row2, col2 = locations[j]

                row_diff, col_diff = row2 - row1, col2 - col1
                anti_row_1, anti_col_1 = row1 - row_diff, col1 - col_diff

                if 0 <= anti_row_1 < m and 0 <= anti_col_1 < n:
                    result.add((anti_row_1, anti_col_1))

                anti_row_2, anti_col_2 = row2 + row_diff, col2 + col_diff

                if 0 <= anti_row_2 < m and 0 <= anti_col_2 < n:
                    result.add((anti_row_2, anti_col_2))

    return len(result)


if __name__ == "__main__":
    matrix = []

    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)

    print("Solution: ", solution_part1(matrix))
