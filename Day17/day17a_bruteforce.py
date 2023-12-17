import copy

import util

def should_add(x, y, d, c, h, visited):
    if (x, y, d, c) in visited and visited[(x, y, d, c)] < h:
        return False
    #print(x, y, d, c)
    #print((x, y, d, c) in visited)
    visited[(x, y, d, c)] = h
    return True

def print_path(hist, heat):
    heat = copy.deepcopy(heat)
    for x, y in hist:
        heat[y][x] = '#'

    util.print_grid([list(map(str, row)) for row in heat])

def main():
    with open("Day17/day17.txt") as f:
        heat = [list(map(int, line.strip())) for line in f.readlines()]
    print(heat[0:10])

    # 0 = Going East
    # 1 = Going West
    # 2 = Going South
    # 3 = Going North

    queue = [(0,0,d,1,0,[]) for d in range(0,3)] #x, y, direction, counter, heat
    visited = {}
    while queue:
        x, y, d, c, h, hist = queue.pop(0)

        # if x == 12 and y == 12:
        #     print(h, hist)
        #     print_path(hist, heat)

        hist = copy.deepcopy(hist)
        hist.append((x,y))

        if c > 3:
            raise Exception()

        if d == 0:
            x += 1
        if d == 1:
            x -= 1
        if d == 2:
            y += 1
        if d == 3:
            y -= 1

        if util.out_of_bounds(heat, x, y):
            continue
        h += heat[y][x]

        for nd in range(0, 4):
            if d == 0 and nd == 1:
                continue
            if d == 1 and nd == 0:
                continue
            if d == 2 and nd == 3:
                continue
            if d == 3 and nd == 2:
                continue

            if nd == d:
                if c < 3:
                    if should_add(x, y, d, c+1, h, visited):
                        queue.append((x, y, d, c+1, h, hist))
            else:
                if should_add(x, y, nd, 1, h, visited):
                    queue.append((x, y, nd, 1, h, hist))

        print(len(queue))

    #print('DONE', visited)
    best_score = float('inf')
    for key in visited:
        if key[0] == len(heat[0]) - 1 and key[1] == len(heat) - 1:
            print(key, visited[key])
            best_score = min(best_score, visited[key])
    print(best_score)
