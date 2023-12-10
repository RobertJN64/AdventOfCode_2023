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

def mark_right_side(past_loc, loc, grid):
    x, y = loc
    if past_loc[0] < loc[0]: #moving right, mark below
        ydp = 1 #delta to mark m
        xdp = 0 #delta to mark m
        xd2 = -1 # delta to mark going backwards
        yd2 = 0  # delta to mark going backwards


    if past_loc[0] > loc[0]: #moving left, mark above
        ydp = -1  # delta to mark m
        xdp = 0  # delta to mark m
        xd2 = 1  # delta to mark going backwards
        yd2 = 0  # delta to mark going backwards


    if past_loc[1] > loc[1]: #moving up, mark right
        ydp = 0  # delta to mark m
        xdp = 1  # delta to mark m
        xd2 = 0 # delta to mark going backwards
        yd2 = 1  # delta to mark going backwards


    if past_loc[1] < loc[1]: #moving down, mark left
        ydp = 0  # delta to mark m
        xdp = -1  # delta to mark m
        xd2 = 0  # delta to mark going backwards
        yd2 = -1  # delta to mark going backwards

    def safe_mark(smx, smy, letter):
        if not util.out_of_bounds(grid, smx, smy) and grid[smy][smx] == '.':
            grid[smy][smx] = letter
    safe_mark(x + xdp, y + ydp, 'M')
    safe_mark(x + xdp + xd2, y + ydp + yd2, 'M')
    safe_mark(x - xdp, y - ydp, 'Q')
    safe_mark(x - xdp + xd2, y - ydp + yd2, 'Q')

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

    # MARK ALL TILES TO THE RIGHT OF THE PATH

    pgrid(lines)
    last_a = s
    a = find_adjacent(s[0], s[1], lines)[0]
    counter = 1
    while True:
        t_a = a
        a = [p for p in find_adjacent(a[0], a[1], lines) if p != last_a][0]
        last_a = t_a

        counter += 1
        if a == s:
            break

        mark_right_side(last_a, a, lines)

    # FLOOD FILL

    pgrid(lines)
    done = False
    while not done:
        done = True
        for y, line in enumerate(lines):
            for x, pipe in enumerate(line):
                if pipe != '.':
                    continue

                for xd, yd in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if util.out_of_bounds(lines, x+xd, y+yd):
                        continue
                    if lines[y+yd][x+xd] == 'Q':
                        lines[y][x] = 'Q'
                        done = False
                    elif lines[y+yd][x+xd] == 'M':
                        lines[y][x] = 'M'
                        done = False

    print('final')
    pgrid(lines)

    mc = 0
    qc = 0
    dotc = 0
    for line in lines:
        for pipe in line:
            if pipe == 'M':
                mc += 1
            elif pipe == 'Q':
                qc += 1
            elif pipe == '.':
                dotc += 1

    print(f"{mc=} {qc=} {dotc=}")