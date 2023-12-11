import util

def main():
    with open("Day11/day11.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    col_expansion = []
    row_expansion = []

    for y, row in enumerate(grid):
        if '#' not in row:
            col_expansion.append(y)

    for x in range(0, len(grid[0])):
        if '#' not in [row[x] for row in grid]:
            row_expansion.append(x)

    util.print_grid(grid)

    coords = []
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == '#':
                coords.append((x, y))

    answer = 0
    mul = 1000000
    for c in coords:
        for c2 in coords:
            for x in range(min(c[0], c2[0]), max(c[0], c2[0])):
                if x in row_expansion:
                    answer += mul
                else:
                    answer += 1

            for y in range(min(c[1], c2[1]), max(c[1], c2[1])):
                if y in col_expansion:
                    answer += mul
                else:
                    answer += 1

    print(answer/2) #answer div2 because we calculated AtoB and BtoA