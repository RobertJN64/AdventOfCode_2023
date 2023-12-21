import util

def main():
    with open("Day21/day21.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    sx = None
    sy = None

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == 'S':
                sx = x
                sy = y

    assert sx is not None
    assert sy is not None

    cpos = [(sx, sy)]
    next_steps = []

    for i in range(64):
        print(f"{i=}")
        for x, y in cpos:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if util.out_of_bounds(grid, x+dx, y+dy):
                    continue
                if (x+dx, y+dy) in next_steps:
                    continue
                if grid[y+dy][x+dx] == '#':
                    continue
                next_steps.append((x+dx, y+dy))
        cpos = next_steps
        next_steps = []

    print(len(cpos))