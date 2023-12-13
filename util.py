def out_of_bounds(grid, x, y):
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[y]):
        return True
    return False

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def debug_IO(f):
    def wrap(*args, **kwargs):
        s = f"Calling {f.__name__} with {args=} {kwargs=}"
        print(s)
        retval = f(*args, **kwargs)
        print(s, f"-> {retval}")
        return retval
    return wrap