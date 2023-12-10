import util

bottom = 'S|7F'
top    = 'S|JL'
left   = 'S-J7'
right  = 'S-FL'

def is_valid(pipe, x, y, grid):
    if pipe in '.S':
        return True

    if pipe in top:
        if util.out_of_bounds(grid, x, y-1):
            return False
        if grid[y-1][x] not in bottom:
            return False

    if pipe in bottom:
        if util.out_of_bounds(grid, x, y+1):
            return False
        if grid[y+1][x] not in top:
            return False

    if pipe in left:
        if util.out_of_bounds(grid, x-1, y):
            return False
        if grid[y][x-1] not in right:
            return False

    if pipe in right:
        if util.out_of_bounds(grid, x+1, y):
            return False
        if grid[y][x+1] not in left:
            return False

    return True

def find_adjacent(x, y, grid):
    pipe = grid[y][x]
    options = []
    if pipe in right and not util.out_of_bounds(grid, x+1, y) and grid[y][x+1] in left:
        options.append((x+1, y))
    if pipe in left and not util.out_of_bounds(grid, x-1, y) and grid[y][x-1] in right:
        options.append((x-1, y))
    if pipe in top and not util.out_of_bounds(grid, x, y-1) and grid[y-1][x] in bottom:
        options.append((x, y-1))
    if pipe in bottom and not util.out_of_bounds(grid, x, y+1) and grid[y+1][x] in top:
        options.append((x, y+1))
    return options

def pgrid(grid):
    for line in grid:
        print(''.join(line))
    print()

def main():
    with open("Day10/day10.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]
    print(lines[0:10])

    #first step - remove all non-connected tiles

    done = False
    s = (-1,-1)
    while not done:
        done = True
        for y, line in enumerate(lines):
            for x, pipe in enumerate(line):
                if is_valid(pipe, x, y, lines):
                    pass
                else:
                    lines[y][x] = '.'
                    done = False
                if pipe == 'S':
                    s = (x,y)

    pgrid(lines)
    last_a = s
    last_b = s
    a, b = find_adjacent(s[0], s[1], lines)
    counter = 1
    while True:
        t_a = a
        a = [p for p in find_adjacent(a[0], a[1], lines) if p != last_a][0]
        last_a = t_a

        t_b = b
        b = [p for p in find_adjacent(b[0], b[1], lines) if p != last_b][0]
        last_b = t_b

        counter += 1
        if a == b or a == last_b:
            print(counter)
            break

        #input(f"{a} {b}")
