import util

def area_given_coords(coords: list[tuple[int, int]]):
    assert coords[0] == coords[-1]
    area = 0
    for i in range(0, len(coords)-1):
        x1, y1 = coords[i]
        x2, y2 = coords[i+1]
        area += x1 * y2
        area -= x2 * y1
    return abs(area/2)

def main():
    with open("Day18/day18.txt") as f:
        cmds = [line.strip().split() for line in f.readlines()]
    print(cmds[0:10])

    x, y = 0, 0
    coords = [(x,y)]
    trench_len = 0

    for direction, qty, color in cmds:
        qty = int(qty)
        trench_len += qty
        if direction == 'R':
            x += qty

        elif direction == 'L':
            x -= qty

        elif direction == 'D':
            y += qty

        elif direction == 'U':
            y -= qty

        else:
            raise Exception()

        coords.append((x, y))

    print(coords)
    print(area_given_coords(coords), trench_len)
    print(area_given_coords(coords) + trench_len/2 + 1)