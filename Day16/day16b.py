import util

# 0 = Going East
# 1 = Going West
# 2 = Going South
# 3 = Going North

mir_map = {
    '/':
        {0: 3, 1: 2, 2: 1, 3: 0},
    '\\':
        {0: 2, 1: 3, 3: 1, 2: 0}
}

def add_laser(lasers, x, y, d, grid):
    if d == 0:
        x += 1
    if d == 1:
        x -= 1
    if d == 2:
        y += 1
    if d == 3:
        y -= 1
    if util.out_of_bounds(grid, x, y):
        return
    lasers.append((x, y, d))

def score(grid, startx, starty, startd):
    energerized = []
    for row in grid:
        t = []
        for _ in row:
            t.append('.')
        energerized.append(t)

    lasers = [(startx, starty, startd)]
    visited = []

    while lasers:
        # util.print_grid(energerized)

        x, y, d = lasers.pop(0)
        if (x, y, d) in visited:
            continue
        visited.append((x, y, d))
        energerized[y][x] = '#'

        tile = grid[y][x]

        if tile == '.':
            add_laser(lasers, x, y, d, grid)
        elif tile in mir_map:
            d = mir_map[grid[y][x]][d]
            add_laser(lasers, x, y, d, grid)
        elif tile == '|':
            if d in [0, 1]:
                add_laser(lasers, x, y, 2, grid)
                add_laser(lasers, x, y, 3, grid)
            else:
                add_laser(lasers, x, y, d, grid)
        elif tile == '-':
            if d in [2, 3]:
                add_laser(lasers, x, y, 0, grid)
                add_laser(lasers, x, y, 1, grid)
            else:
                add_laser(lasers, x, y, d, grid)
        else:
            raise Exception("Invalid square")

    answer = 0
    for row in energerized:
        for val in row:
            if val == '#':
                answer += 1
    return answer

def main():
    with open("Day16/day16.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    print(grid[0:10])

    mscore = 0
    for x in range(0, 10):
        print(x)
        mscore = max(mscore, score(grid, x, 0, 2))
        mscore = max(mscore, score(grid, x, len(grid)-1, 3))

    for y in range(0, 10):
        print(y)
        mscore = max(mscore, score(grid, 0, y, 0))
        mscore = max(mscore, score(grid, len(grid[0])-1, y, 1))

    print(mscore)


