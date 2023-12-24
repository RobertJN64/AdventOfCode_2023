class Stone:
    def __init__(self, s):
        pos, vel = s.split(" @ ")
        self.x, self.y, self.z = map(int, pos.split(', '))
        self.vx, self.vy, self.vz = map(int, vel.split(', '))

    def __repr__(self):
        return f"{(self.x, self.y, self.z)} @ {(self.vx, self.vy, self.vz)}"

    def could_work(self, rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz):
        check = []
        if rock_vx == self.vx: #div0
            if rock_x != self.x:
                return False
        else:
            check.append((rock_x - self.x) / (self.vx - rock_vx))

        if rock_vy == self.vy: #div0
            if rock_y != self.y:
                return False
        else:
            check.append((rock_y - self.y) / (self.vy - rock_vy))

        if rock_vz == self.vz: #div0
            if rock_z != self.z:
                return False
        else:
            check.append((rock_z - self.z) / (self.vz - rock_vz))

        if len(check) == 0:
            return True
        for item in check:
            if item != check[0]:
                return False
        return True

def main():
    with open("Day24/day24.txt") as f:
        stones = [Stone(line.strip()) for line in f.readlines()]

    for rock_vx in range(-1000, 1000):
        for rock_vy in range(-1000, 1000):
            print(rock_vx, rock_vy)
            for rock_vz in range(-1000, 1000):
                for time_step in range(0, 20):
                    rock_x = stones[0].x + (stones[0].vx - rock_vx) * time_step
                    rock_y = stones[0].y + (stones[0].vy - rock_vy) * time_step
                    rock_z = stones[0].z + (stones[0].vz - rock_vz) * time_step

                    if all(stone.could_work(
                            rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz
                    ) for stone in stones):
                        print(rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz)
