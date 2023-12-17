import util

def main():
    with open("Day17/day17.txt") as f:
        heat = [list(map(int, line.strip())) for line in f.readlines()]
    print(heat[0:10])
    cost = [[-1] * len(heat[0]) for _ in heat]

    cost[-1][-1] = heat[-1][-1]

    util.print_grid_spaced(cost)

    done = False
    while not done:
        done = True
        for y, row in enumerate(cost):
            for x, c in enumerate(cost):

                potential_cost = float('inf')

                for xdif in [-3, -2, -1]:
                    if util.out_of_bounds(cost, x+xdif, y):
                        continue
                    if cost[y][x+xdif] == -1:
                        continue

                    heat_score = cost[y][x+xdif]
                    for xcoord in range(x+xdif-1, x-1):
                        heat_score += heat[y][xcoord]
                    print(f"from {(x+xdif,y)} to {(x, y)} had cost of {heat_score}")

                for xdif in [1, 2, 3]:
                    if util.out_of_bounds(cost, x + xdif, y):
                        continue
                    if cost[y][x+xdif] == -1:
                        continue

                    heat_score = cost[y][x+xdif]
                    for xcoord in range(x+1, x+xdif+1):
                        heat_score += heat[y][xcoord]
                    print(f"from {(x, y)} to {(x+xdif, y)} had cost of {heat_score}")


                for ydif in [-3, -2, -1, 1, 2, 3]:
                    pass

