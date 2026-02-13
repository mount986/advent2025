import math
import re


class Problem(object):
    def __init__(self, nums: list, sign):
        self.nums = nums
        self.sign = sign

    def solve(self):
        if self.sign == "+":
            return sum(self.nums)
        elif self.sign == "*":
            return math.prod(self.nums)
        else:
            return 0


def part1(input_name):
    sum = 0
    problems = []
    with open(input_name, "r") as file:
        data = file.readlines()

    for d in data:
        problems.append(re.split(r"\s+", d.strip()))

    for index in range(len(problems[0])):
        sum += calculate(problems)

    return sum


def part2(input_name):
    total = 0
    data_list = []
    with open(input_name, "r") as file:
        data = file.readlines()

    for d in data:
        data_list.append(list(d.rstrip("\n")))

    problems = parse(list(data_list))

    for problem in problems:
        total += problem.solve()

    return total


def parse(data) -> list:
    nums = []
    problems = []
    while len(data[0]) > 0:
        num = []
        for index in range(len(data) - 1):
            num.append(data[index].pop())

        number = int("".join(num))
        nums.append(number)

        sign = data[len(data) - 1].pop()

        if sign != " ":
            problems.append(Problem(nums, sign))
            nums = []

            for index in range(len(data)):
                if len(data[index]) > 0:
                    data[index].pop()

    return problems


def calculate(problems: list) -> int:
    nums = []
    for i in range(len(problems) - 1):
        nums.append(int(problems[i].pop()))

    sign = problems[len(problems) - 1].pop()

    if sign == "+":
        return sum(nums)
    elif sign == "*":
        return math.prod(nums)
    else:
        return 0


if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))
