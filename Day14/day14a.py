import util

def main():
    with open("Day14/day14.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    util.print_grid(grid)

    done = False
    while not done:
        done = True
        for y in range(1, len(grid)):
            for x, tile in enumerate(grid[y]):
                if tile == 'O' and grid[y-1][x] == '.':
                    grid[y-1][x] = 'O'
                    grid[y][x] = '.'
                    done = False

    answer = 0
    for y, row in enumerate(grid):
        weight = len(grid) - y
        for tile in row:
            if tile == 'O':
                answer += weight

    print(answer)