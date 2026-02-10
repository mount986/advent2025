from typing import Any


class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high

def part1(input_name):
    ranges = parse_input(input_name)

    invalid_ids = find_dups1(ranges)

    return sum(invalid_ids)

def part2(input_name):
    ranges = parse_input(input_name)

    invalid_ids = find_dups2(ranges)

    return sum(invalid_ids)

def parse_input(input_name):
    ranges = []
    with open(input_name) as file:
        data = file.read()
        lines = data.split(',')
        for line in lines:
            sp = line.split('-')
            ranges.append(Range(int(sp[0]), int(sp[1])))

    return ranges

def find_dups1(ranges: list[Any]):
    invalid_ids = []
    for r in ranges:
        for num in range(r.low, r.high + 1):
            num_str = str(num)
            l = len(num_str)
            if l % 2 == 1:
                continue
            if num_str[:int(l / 2)] == num_str[int(l / 2):]:
                invalid_ids.append(num)

    return invalid_ids

def find_dups2(ranges: list[Any]):
    invalid_ids = []
    for r in ranges:
        for num in range(r.low, r.high + 1):
            num_str = str(num)
            l = len(num_str)
            factors = [i for i in range(1, l) if l % i == 0]
            for factor in factors:
                chunks = [num_str[i:i + factor] for i in range(0, l, factor)]
                if len(set(chunks)) <= 1:
                    invalid_ids.append(num)
                    break

    return invalid_ids


if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))