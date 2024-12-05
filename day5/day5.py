from typing import Dict, List


def solution_part1(page_order_rules: Dict[int, int], updates: List[List[int]]) -> int:
    correct = []
    for update in updates:
        correct_order = True
        row_order_map = {}
        for i, num in enumerate(update):
            row_order_map[num] = i

            if not num in page_order_rules:
                continue

            for after_num in page_order_rules[num]:
                if after_num in row_order_map:
                    correct_order = False
                    break

            if not correct_order:
                break

        if correct_order:
            correct.append(update)

    res = 0
    for arr in correct:
        res += arr[len(arr) // 2]
    return res


def _parse_text_to_data(file_path: str):
    page_order_rules: Dict[int, List[int]] = {}
    updates: List[List[int]] = []

    with open(file_path, "r") as file:
        lines = file.read().strip().splitlines()

    rules_part = True
    for line in lines:
        if "|" in line:
            key, value = map(int, line.split("|"))
            if key not in page_order_rules:
                page_order_rules[key] = []
            page_order_rules[key].append(value)
        else:
            rules_part = False

        if not rules_part and "," in line:
            updates.append(list(map(int, line.split(","))))

    return page_order_rules, updates


if __name__ == "__main__":
    page_order_rules, updates = _parse_text_to_data("input.txt")

    print("Part 1 solution: ", solution_part1(page_order_rules, updates))
