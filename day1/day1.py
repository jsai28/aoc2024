from typing import List
from collections import Counter


# Part 1 solution, O(nlogn)
def solution_part1(list1: List, list2: List) -> int:
    list1.sort()
    list2.sort()
    result = 0
    for num1, num2 in zip(list1, list2):
        diff = abs(num1 - num2)
        result += diff

    return result


# Part 2 solution, O(n)
def solution_part2(list1: List, list2: List) -> int:
    count_list1 = Counter(list1)  # O(n)
    count_list2 = Counter(list2)  # O(n)
    result = 0
    for num in count_list1.keys():
        if num in count_list2:
            result += num * count_list2[num]

    return result


if __name__ == "__main__":
    list1, list2 = [], []
    with open("lists.txt", "r") as f:
        for line in f:
            values = line.split()
            list1.append(int(values[0]))
            list2.append(int(values[1]))

    print("Part 1 solution: ", solution_part1(list1, list2))
    print("Part 2 solution: ", solution_part2(list1, list2))
