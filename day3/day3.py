import re
from typing import List

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def _multiply(matches: List) -> int:
    result = []
    for num1, num2 in matches:
        result.append(int(num1) * int(num2))

    return sum(result)


# Part 1 solution
def solution_part1(input: str) -> int:
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(mul_pattern, input)
    return _multiply(matches)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().strip()

    print("Part 1 solution: ", solution_part1(input))
    # print("Part 2 solution: ", solution_part2(text))
