import util



def main():
    with open("Day23/day23.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    util.print_grid(grid)
    queue = [(1, 0, {(1,0)})]

    def add_pt(_x, _y, _hist: set):
        if (_x, _y) in hist:
            return
        _hist = _hist.copy()
        _hist.add((_x, _y))
        queue.append((_x, _y, _hist))

    best_len = 0
    while queue:
        if len(queue) % 1000 == 0:
            print(len(queue))

        x, y, hist = queue.pop(0)

        if y == len(grid) - 1 and x == len(grid[0]) - 2:
            print("Found new len: ", len(hist) - 1)
            best_len = max(best_len, len(hist) - 1)


        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if util.out_of_bounds(grid, x + dx, y + dy):
                continue

            if grid[y][x] == '#':
                continue

            add_pt(x+dx, y+dy, hist)

    print("ANSWER", best_len)