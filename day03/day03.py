from typing import Any


def part1(input_name):
    joltage = 0
    with open(input_name) as file:
        banks = file.readlines()

    for bank in banks:
        bank = bank.strip()
        left = 0
        right = 0
        i = 0
        for battery in bank:
            battery = int(battery)
            if battery > right:
                right = battery

            if i != len(bank) - 1:
                if battery > left:
                    left = battery
                    right = 0

            i += 1

        joltage += left * 10 + right

    return joltage


def part2(input_name):
    joltage = 0

    with open(input_name) as file:
        banks = file.readlines()

    for bank in banks:
        bank = bank.strip()
        values = []

        for index in range(12):
            length = len(bank)
            max_val = max(bank[:(length - 11 + index)])
            max_pos = bank[:(length - 11 + index)].index(max_val)

            values.append(max_val)
            bank = bank[(max_pos  + 1):]

        joltage += int("".join(values))

    return joltage


if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))
