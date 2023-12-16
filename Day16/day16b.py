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

        new_lasers = []

        if grid[y][x] == '.':
            new_lasers.append((x, y, d))
        elif grid[y][x] in mir_map:
            d = mir_map[grid[y][x]][d]
            new_lasers.append((x, y, d))
        elif grid[y][x] == '|':
            if d in [0, 1]:
                new_lasers.append((x, y, 2))
                new_lasers.append((x, y, 3))
            else:
                new_lasers.append((x, y, d))
        elif grid[y][x] == '-':
            if d in [2, 3]:
                new_lasers.append((x, y, 0))
                new_lasers.append((x, y, 1))
            else:
                new_lasers.append((x, y, d))
        else:
            raise Exception("Invalid square")

        for (x, y, d) in new_lasers:
            if d == 0:
                x += 1
            if d == 1:
                x -= 1
            if d == 2:
                y += 1
            if d == 3:
                y -= 1
            if util.out_of_bounds(grid, x, y):
                continue
            lasers.append((x, y, d))

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
    for x in range(0, len(grid[0])):
        print(x)
        mscore = max(mscore, score(grid, x, 0, 2))
        mscore = max(mscore, score(grid, x, len(grid)-1, 3))

    for y in range(0, len(grid)):
        print(y)
        mscore = max(mscore, score(grid, 0, y, 0))
        mscore = max(mscore, score(grid, len(grid[0])-1, y, 1))

    print(mscore)


