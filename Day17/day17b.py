import util

# 0 = Going East
# 1 = Going West
# 2 = Going South
# 3 = Going North

class Tile:
    def __init__(self, heat):
        self.local_heat = int(heat)
        self.east_cost = float('inf') #not yet found
        self.west_cost = float('inf')
        self.south_cost = float('inf')
        self.north_cost = float('inf')

    def mark_as_exit(self): #Call on tile at bottom corner
        self.east_cost = self.local_heat
        self.west_cost = self.local_heat
        self.south_cost = self.local_heat
        self.north_cost = self.local_heat

    def __str__(self):
        return f"h{self.local_heat} {self.east_cost} {self.west_cost} {self.south_cost} {self.north_cost} |"
            #
            # str(min(self.east_cost, self.west_cost, self.south_cost, self.north_cost)))

def main():
    with open("Day17/day17.txt") as f:
        heat = [list(map(Tile, line.strip())) for line in f.readlines()]

    print(heat[0:10])
    heat[-1][-1].mark_as_exit()

    done = 1
    while done > 0:
        print("Changes: ", done)
        done = 0

        for y, row in enumerate(heat):
            for x, tile in enumerate(row):
                #SCAN EAST
                for xdif in [4, 5, 6, 7, 8, 9, 10]:
                    if util.out_of_bounds(heat, x + xdif, y):
                        continue

                    acc_cost = 0
                    for xcoord in range(x, x+xdif): #exclude the end
                        acc_cost += heat[y][xcoord].local_heat
                    acc_cost += min(heat[y][x+xdif].north_cost, heat[y][x+xdif].south_cost)
                    if acc_cost < tile.east_cost:
                        done += 1
                        tile.east_cost = acc_cost

                #SCAN WEST
                for xdif in [-10, -9, -8, -7, -6, -5, -4]:
                    if util.out_of_bounds(heat, x + xdif, y):
                        continue

                    acc_cost = 0
                    for xcoord in range(x + xdif + 1, x + 1):  # exclude the start
                        acc_cost += heat[y][xcoord].local_heat
                    acc_cost += min(heat[y][x + xdif].north_cost, heat[y][x + xdif].south_cost)
                    if acc_cost < tile.west_cost:
                        done += 1
                        tile.west_cost = acc_cost

                #SCAN SOUTH
                for ydif in [4, 5, 6, 7, 8, 9, 10]:
                    if util.out_of_bounds(heat, x, y + ydif):
                        continue

                    acc_cost = 0
                    for ycoord in range(y, y + ydif):  # exclude the end
                        acc_cost += heat[ycoord][x].local_heat
                    acc_cost += min(heat[y + ydif][x].east_cost, heat[y + ydif][x].west_cost)
                    if acc_cost < tile.south_cost:
                        done += 1
                        tile.south_cost = acc_cost

                # SCAN NORTH
                for ydif in [-10, -9, -8, -7, -6, -5, -4]:
                    if util.out_of_bounds(heat, x, y + ydif):
                        continue

                    acc_cost = 0
                    for ycoord in range(y + ydif + 1, y + 1):  # exclude the start
                        acc_cost += heat[ycoord][x].local_heat
                    acc_cost += min(heat[y + ydif][x].east_cost, heat[y + ydif][x].west_cost)
                    if acc_cost < tile.north_cost:
                        done += 1
                        tile.north_cost = acc_cost

    util.print_grid_spaced(heat)
    tile = heat[0][0]
    print(min(tile.east_cost, tile.west_cost, tile.north_cost, tile.south_cost) - tile.local_heat)