import util
import copy

def find_horiz_line(grid):
    opts = []
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
            opts.append(x)
    return opts

def find_vert_line(grid):
    opts = []
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
            opts.append(y)
    return opts

def main():
    with open("Day13/day13.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    grids = []
    cgrid = []
    for line in lines:
        if len(line) == 0:
            grids.append(cgrid)
            cgrid = []
        else:
            cgrid.append(line)

    grids.append(cgrid)

    answer = 0
    for grid in grids:
        util.print_grid(grid)
        old_h = find_horiz_line(grid)
        old_v = find_vert_line(grid)

        for y in range(0, len(grid)):
            done = False
            for x in range(0, len(grid[0])):
                t_grid = copy.deepcopy(grid)
                if t_grid[y][x] == '.':
                    t_grid[y][x] = '#'
                else:
                    t_grid[y][x] = '.'

                h_line = find_horiz_line(t_grid)
                v_line = find_vert_line(t_grid)

                #print(x, y, h_line, v_line, old_h, old_v)

                for h in h_line:
                    if h not in old_h:
                        answer += h
                        done = True
                        break
                if done:
                    break

                for v in v_line:
                    if v not in old_v:
                        answer += v * 100
                        done = True
                        break
                if done:
                    break

            if done:
                break

        else:
            util.print_grid(grid)
            raise Exception("NO NEW LINE FOUND")

    print(answer)




