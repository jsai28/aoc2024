from typing import List


# Part 1 solution, O(m*n) where m=num of reports and n=size of report
def _is_safe(nums: List) -> bool:
    prev_diff = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]

        if not ((diff * prev_diff) >= 0 and 1 <= abs(diff) <= 3):
            return False

        prev_diff = diff

    return True


def solution_part1(reports: List[List]) -> int:
    safe = 0
    for report in reports:
        safe += 1 if _is_safe(report) is True else 0

    return safe


# Part 2 solution, O(m*n^2)
def solution_part2(reports: List[List]) -> int:
    safe = 0
    for report in reports:
        if _is_safe(report):
            safe += 1
        else:
            for i in range(len(report)):
                if _is_safe(report[:i] + report[i + 1 :]):
                    safe += 1
                    break

    return safe


if __name__ == "__main__":
    reports = []
    with open("reports.txt", "r") as f:
        for line in f:
            values = line.split()
            reports.append([int(x) for x in values])

    print("part 1 solution: ", solution_part1(reports))
    print("part 2 solution: ", solution_part2(reports))

    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    print(solution_part2(reports))
