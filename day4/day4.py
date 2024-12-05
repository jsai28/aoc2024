from typing import List

sample = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


# Part 1 solution
def solution_part1(puzzles: List[str]):
    result = 0
    rows = len(puzzles)
    cols = len(puzzles[0])
    word = "XMAS"

    def _search_neighbours(r: int, c: int):
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
        ]
        num_found = 0
        for dx, dy in directions:
            cur_found = 0
            for i in range(4):
                new_row = r + i * dy
                new_col = c + i * dx
                if not ((0 <= new_row < rows) and (0 <= new_col < cols)):
                    break
                if puzzles[new_row][new_col] == word[i]:
                    cur_found += 1

            num_found += 1 if cur_found == 4 else 0

        return num_found

    for row in range(rows):
        for col in range(cols):
            if puzzles[row][col] == "X":
                result += _search_neighbours(row, col)

    return result


if __name__ == "__main__":
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    sample = [list(row) for row in sample.split("\n")]
    print(sample)

    print("Part 1 solution: ", solution_part1(grid))
