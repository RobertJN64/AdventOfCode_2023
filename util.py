def out_of_bounds(grid, x, y):
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[y]):
        return True
    return False

def fast_in_bounds(x, y, minx, maxx, miny, maxy):
    return minx <= x < maxx and miny <= y < maxy

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def str_pad(x):
    s = str(x)
    return ' ' * (20 - len(s)) + s

def print_grid_spaced(grid):
    for line in grid:
        print(''.join(map(str_pad, line)))
    print()

def debug_IO(f):
    def wrap(*args, **kwargs):
        s = f"Calling {f.__name__} with {args=} {kwargs=}"
        print(s)
        retval = f(*args, **kwargs)
        print(s, f"-> {retval}")
        return retval
    return wrap