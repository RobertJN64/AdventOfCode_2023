import util

def main():
    with open("Day18/day18.txt") as f:
        cmds = [line.strip().split() for line in f.readlines()]
    print(cmds[0:10])

    grid = [['#']]
    x = 0
    y = 0
    for direction, qty, color in cmds:
        qty = int(qty)
        if direction == 'R':
            for dx in range(qty):
                x += 1
                if util.out_of_bounds(grid, x, y):
                    for line in grid:
                        line.append('.')
                grid[y][x] = '#'

        elif direction == 'L':
            for dx in range(qty):
                x -= 1
                if util.out_of_bounds(grid, x, y):
                    x += 1
                    for line in grid:
                        line.insert(0, '.')
                grid[y][x] = '#'

        elif direction == 'D':
            for dx in range(qty):
                y += 1
                if util.out_of_bounds(grid, x, y):
                    grid.append(['.'] * len(grid[0]))
                grid[y][x] = '#'

        elif direction == 'U':
            for dx in range(qty):
                y -= 1
                if util.out_of_bounds(grid, x, y):
                    y += 1
                    grid.insert(0, ['.'] * len(grid[0]))
                grid[y][x] = '#'

        else:
            raise Exception()

        # util.print_grid(grid)
        # input(f"{direction=}, {qty=}, {color=}")

    #NOW FLOODFILL OUTSIDE
    for line in grid:
        line.insert(0, 'X')
        line.append('X')
    grid.insert(0, ['X'] * len(grid[0]))
    grid.append(['X'] * len(grid[0]))

    util.print_grid(grid)

    done = False
    while not done:
        done = True
        for y, line in enumerate(grid):
            for x, tile in enumerate(line):
                if tile != '.':
                    continue

                for xd, yd in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if util.out_of_bounds(grid, x + xd, y + yd):
                        continue
                    if grid[y + yd][x + xd] == 'X':
                        grid[y][x] = 'X'
                        done = False

    util.print_grid(grid)

    xcount = 0
    for line in grid:
        for tile in line:
            if tile == 'X':
                xcount += 1

    true_x = xcount - len(grid) * 2 - len(grid[0]) * 2 + 4
    print((len(grid) - 2) * (len(grid[0]) - 2) - true_x)