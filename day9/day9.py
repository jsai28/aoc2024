from typing import List


def _generate_freespace_map(diskmap: List[str]) -> List[str]:
    freespace = []

    for i in range(0, len(diskmap) - 1, 2):
        file = int(diskmap[i])
        space = int(diskmap[i + 1])
        for _ in range(file):
            freespace.append(i // 2)

        for _ in range(space):
            freespace.append(".")

    file = int(diskmap[len(diskmap) - 1])
    for _ in range(file):
        freespace.append((len(diskmap) - 1) // 2)

    return freespace


def solution_part1(diskmap: List) -> int:
    freespace = _generate_freespace_map(diskmap)

    left, right = 0, len(freespace) - 1

    while left < right:
        while freespace[left] != ".":
            left += 1

        while freespace[right] == ".":
            right -= 1

        if left >= right:
            break

        tmp = freespace[right]
        freespace[right] = freespace[left]
        freespace[left] = tmp

    result = 0
    for i, num in enumerate(freespace):
        if num == ".":
            break
        result += i * int(num)
    return result


if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as file:
        input = file.readline()

    print("Solution: ", solution_part1(input))
