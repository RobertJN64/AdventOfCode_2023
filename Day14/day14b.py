import util

def roll_north(grid):
    done = False
    while not done:
        done = True
        for y in range(1, len(grid)):
            for x, tile in enumerate(grid[y]):
                if tile == 'O' and grid[y - 1][x] == '.':
                    grid[y - 1][x] = 'O'
                    grid[y][x] = '.'
                    done = False

def roll_south(grid):
    done = False
    while not done:
        done = True
        for y in range(len(grid) - 2, -1, -1):
            for x, tile in enumerate(grid[y]):
                if tile == 'O' and grid[y + 1][x] == '.':
                    grid[y + 1][x] = 'O'
                    grid[y][x] = '.'
                    done = False

def roll_west(grid):
    done = False
    while not done:
        done = True
        for row in grid:
            for x, tile in enumerate(row[1:]):
                if tile == 'O' and row[x + 1- 1] == '.':
                    row[x + 1 - 1] = 'O'
                    row[x + 1] = '.'
                    done = False

def roll_east(grid):
    done = False
    while not done:
        done = True
        for row in grid:
            for x, tile in enumerate(row[:-1]):
                if tile == 'O' and row[x + 1] == '.':
                    row[x + 1] = 'O'
                    row[x] = '.'
                    done = False

def cycle_grid(grid):
    roll_north(grid)
    roll_west(grid)
    roll_south(grid)
    roll_east(grid)

def grid_to_str(grid):
    return ''.join([''.join(row) for row in grid])

def main():
    with open("Day14/day14.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    util.print_grid(grid)

    cache = {}

    skip_val = 0
    end_pt = 0
    for i in range(0, 1000000000):
        print(i)
        cycle_grid(grid)

        s = grid_to_str(grid)
        if s in cache:
            skip_val = i - cache[s]
            end_pt = i
            break
        else:
            cache[s] = i

    for i in range(0, (1000000000-end_pt)%skip_val-1):
        cycle_grid(grid)


    answer = 0
    for y, row in enumerate(grid):
        weight = len(grid) - y
        for tile in row:
            if tile == 'O':
                answer += weight

    print(answer)