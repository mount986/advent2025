def part1(input_name):
    grid = Grid(input_name)

    return remove_rolls(grid, False)

def part2(input_name):
    grid = Grid(input_name)
    total = 0

    while True:
        movable = remove_rolls(grid, True)
        total += movable

        if movable == 0:
            break

    return total

class Grid:
    def __init__(self, filepath):
        self.data = {}
        # Maps (x, y) tuple to Boolean

        with open(filepath, 'r') as f:
            lines = f.readlines()
            self.height = len(lines)
            self.width = len(lines[0]) if self.height > 0 else 0

            for y, line in enumerate(lines):
                line = line.strip()
                for x, char in enumerate(line):
                    self.data[(x, y)] = (char == '@')

    def has_roll(self, x, y):
        return self.data.get((x, y), False)

def remove_rolls(grid: Grid, delete: bool) -> int:
    movable = 0

    for y in range(grid.height):
        for x in range(grid.width):
            if grid.has_roll(x, y):
                surrounding = rolls_surrounding(x, y, grid)

                if surrounding < 4:
                    print(f"({x},{y}) is movable with {surrounding} surrounding")
                    movable += 1

                    if delete:
                        grid.data[(x, y)] = False

    return movable

def rolls_surrounding(x, y, grid):
    count = 0

    if x - 1 >= 0:
        if y - 1 >= 0:
           count += 1 if grid.has_roll(x - 1, y - 1) else 0
        if y +1 < grid.height:
            count += 1 if grid.has_roll(x - 1, y + 1) else 0
        count += 1 if grid.has_roll(x - 1, y) else 0

    if x + 1 < grid.width:
        if y - 1 >= 0:
            count += 1 if grid.has_roll(x + 1, y - 1) else 0

        if y +1 < grid.height:
            count += 1 if grid.has_roll(x + 1, y+ 1) else 0

        count += 1 if grid.has_roll(x + 1, y) else 0

    if y - 1 >= 0:
        count += 1 if grid.has_roll(x, y - 1) else 0
    if y +1 < grid.height:
        count += 1 if grid.has_roll(x, y + 1) else 0

    return count


if __name__ == '__main__':
    print("part 1: ", part1("input.dat"))
    print("part 2: ", part2("input.dat"))