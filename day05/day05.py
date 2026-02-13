from typing import Any

from advent2025.day02.day02 import Range


class Range:
    def __init__(self, low, high):
        self.low = int(low)
        self.high = int(high)

    def __str__(self):
        return f"({self.low}, {self.high})"

    def __repr__(self):
        return f"({self.low}, {self.high})"

    def inRange(self, val: int) -> bool:
        return self.low <= val <= self.high

    def overlaps(self, other: Range) -> bool:
        return self.low <= other.low <= self.high or self.high >= other.high >= self.low

    def merge(self, other: Range) -> Range:
        self.low = min(self.low, other.low)
        self.high = max(self.high, other.high)

    def size(self) -> int:
        return self.high - self.low + 1


def part1(input_name):
    count = 0
    with open(input_name) as file:
        data = file.readlines()

    fresh_ranges, products = parse_data(data)

    for product in products:
        for r in fresh_ranges:
            if r.inRange(product):
                count += 1
                break

    return count


# too high 359771580274995
def part2(input_name):
    merged_ranges = []
    count = 0
    with open(input_name) as file:
        data = file.readlines()

    fresh_ranges, _ = parse_data(data)

    fresh_ranges.sort(key=lambda x: x.low)

    fresh_ranges = condense(fresh_ranges)

    for r in fresh_ranges:
        count += r.size()

    return count


def condense(ranges: list[Range]) -> list[Range]:
    index = 0
    while index < (len(ranges) - 1):
        merged = False
        if ranges[index].overlaps(ranges[index + 1]):
            ranges[index].merge(ranges[index + 1])
            ranges.pop(index + 1)
            merged = True

        if not merged:
            index += 1

    return ranges


def parse_data(data: list[str]):
    fresh_ranges = []
    products = []

    for line in data:
        line = line.strip()

        if line == "":
            continue

        if "-" in line:
            fresh_ranges.append(Range(*line.split("-")))
        else:
            products.append(int(line))

    return fresh_ranges, products


if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))
