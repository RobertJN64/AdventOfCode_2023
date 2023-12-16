from line_profiler import profile
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

def get_step(x, y, d):
    if d == 0:
        x += 1
    if d == 1:
        x -= 1
    if d == 2:
        y += 1
    if d == 3:
        y -= 1
    return x, y, d

@profile
def score(grid, startx, starty, startd):
    energerized = set()
    lasers = [(startx, starty, startd)]
    visited = set()

    maxy = len(grid)
    maxx = len(grid[0])

    while lasers:
        # util.print_grid(energerized)
        x, y, d = lasers.pop(0)
        while util.fast_in_bounds(x, y, 0, maxx, 0, maxy):
            if (x, y, d) in visited:
                break
            visited.add((x, y, d))
            energerized.add((x, y))

            tile = grid[y][x]

            if tile == '.':
                x, y, d = get_step(x, y, d)
            elif tile in mir_map:
                d = mir_map[grid[y][x]][d]
                x, y, d = get_step(x, y, d)
            elif tile == '|':
                if d in [0, 1]:
                    x, y, d = get_step(x, y, 2)
                    lasers.append(get_step(x, y, 3))
                else:
                    x, y, d = get_step(x, y, d)
            elif tile == '-':
                if d in [2, 3]:
                    x, y, d = get_step(x, y, 0)
                    lasers.append(get_step(x, y, 1))
                else:
                    x, y, d = get_step(x, y, d)
            else:
                raise Exception("Invalid square")

    return len(energerized)

def main():
    with open("Day16/day16.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    print(grid[0:10])

    mscore = 0
    for x in range(0, len(grid[0])):
        #print(x)
        mscore = max(mscore, score(grid, x, 0, 2))
        mscore = max(mscore, score(grid, x, len(grid)-1, 3))

    for y in range(0, len(grid)):
        #print(y)
        mscore = max(mscore, score(grid, 0, y, 0))
        mscore = max(mscore, score(grid, len(grid[0])-1, y, 1))

    print(mscore)


