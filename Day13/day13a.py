import util

def find_horiz_line(grid):
    for x in range(1, len(grid[0])):
        perfect = True
        for row in grid:
            a = row[:x]
            b = row[x:][::-1]

            if len(a) > len(b):
                a = a[-len(b):]
            else:
                b = b[-len(a):]

            for c, d in zip(a, b):
                if c != d:
                    perfect = False
        if perfect:
            return x
    #return None
    return 0

def find_vert_line(grid):
    for y in range(1, len(grid)):
        perfect = True
        a = grid[:y]
        b = grid[y:][::-1]

        if len(a) > len(b):
            a = a[-len(b):]
        else:
            b = b[-len(a):]


        for c, d in zip(a, b):
            if c != d:
                perfect = False

        if perfect:
            return y
    #return None
    return 0

def main():
    with open("Day13/day13.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    grids = []
    cgrid = []
    for line in lines:
        if line == '':
            grids.append(cgrid)
            cgrid = []
        else:
            cgrid.append(line)

    grids.append(cgrid)

    answer = 0
    for grid in grids:
        util.print_grid(grid)
        answer += find_horiz_line(grid) + 100 * find_vert_line(grid)

        #util.print_grid(grid)
        #print(find_horiz_line(grid))
        #print(find_vert_line(grid))
        assert find_horiz_line(grid) != 0 or find_vert_line(grid) != 0
        assert find_horiz_line(grid) == 0 or find_vert_line(grid) == 0
    print(answer)




