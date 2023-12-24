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
        color = color.replace(')', '').replace('(#', '')
        direction = color[-1:]
        qty = int(color[:-1], 16)
        print(qty, direction)

        qty = int(qty)
        trench_len += qty
        if direction in ['R', '0']:
            x += qty

        elif direction in ['L', '2']:
            x -= qty

        elif direction in ['D', '1']:
            y += qty

        elif direction in ['U', '3']:
            y -= qty

        else:
            raise Exception(f"{direction=}")

        coords.append((x, y))

    print(coords)
    print(area_given_coords(coords), trench_len)
    print(area_given_coords(coords) + trench_len/2 + 1)