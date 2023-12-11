import util

def main():
    with open("Day11/day11.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    y = 0
    while y < len(grid):
        if '#' not in grid[y]:
            grid.insert(y, ['.'] * len(grid[y]))
            y += 1
        y += 1

    x = 0
    while x < len(grid[0]):
        if '#' not in [row[x] for row in grid]:
            for line in grid:
                line.insert(x, '.')
            x += 1
        x += 1

    util.print_grid(grid)

    coords = []
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == '#':
                coords.append((x, y))

    answer = 0
    for c in coords:
        for c2 in coords:
            answer += abs(c[0] - c2[0]) + abs(c[1] - c2[1])
    print(answer/2)  #answer div2 because we calculated AtoB and BtoA