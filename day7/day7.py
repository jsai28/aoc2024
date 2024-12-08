def solution_part1(input: str) -> int:
    result = 0

    def calculate(nums):
        if len(nums) == 1:
            return True if nums[0] == test_value else False

        return calculate([nums[0] + nums[1]] + nums[2:]) or calculate(
            [nums[0] * nums[1]] + nums[2:]
        )

    for line in input:
        test_value, equation = line.split(": ")
        test_value = int(test_value)
        equation = list(map(int, equation.split()))
        result += test_value if calculate(equation) else 0

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.readlines()
    print("Part 1 solution: ", solution_part1(input_data))
