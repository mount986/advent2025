
def part1(input_name):
    num = 50
    count = 0
    with open(input_name) as file:
        lines = file.readlines()

    for line in lines:
        direction, distance = parse_line(line)
        num += direction * distance

        num = num % 100

        if num == 0:
            count += 1

    return count

def part2(input_name):
    num = 50
    count = 0
    with open(input_name) as file:
        lines = file.readlines()

    for line in lines:
        direction, distance = parse_line(line)
        if num == 0 and direction == -1:
            count -= 1

        num += direction * distance

        zeros = int(abs(num) / 100)
        if num <= 0:
            count += 1

        num = num % 100
        count += zeros

    return count

def parse_line(line):
    direction = 0
    distance = 0

    if line[:1] == "L":
        direction = -1
    else:
        direction = 1
    distance = int(line[1:])

    return direction, distance

if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))