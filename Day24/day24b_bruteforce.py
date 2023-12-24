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

    s1 = stones[0]
    s2 = stones[1]

    scan_size = 20
    for rock_vx in range(-scan_size, scan_size):
        for rock_vy in range(-scan_size, scan_size):
            print(rock_vx, rock_vy)
            for rock_vz in range(-scan_size, scan_size):
                #GOAL: solve for s1 time so we can derive x, y, z pos using s1 and s2 pos
                #(s1.vx - rock_vx) * s1_time + s1.x = (s2.vx - rock_vx) * s2_time + s2.x
                #(s1.vy - rock_vy) * s1_time + s1.y = (s2.vy - rock_vy) * s2_time + s2.y

                s1_dvx = (s1.vx - rock_vx)
                s1_dvy = (s1.vy - rock_vy)
                s2_dvx = (s2.vx - rock_vx)
                s2_dvy = (s2.vy - rock_vy)

                num = (s1.y - s2.y) * s2_dvx - (s1.x - s2.x) * s2_dvy
                denom = s1_dvx * s2_dvy - s1_dvy * s2_dvx
                try:
                    time = num/denom

                    rock_x = s1_dvx * time + s1.x
                    rock_y = s1_dvy * time + s1.y
                    rock_z = (s1.vz - rock_vz) * time + s1.z
                    #
                    # if rock_vx == -3 and rock_vy == 1:
                    #     print(time, rock_x, rock_y, rock_z)

                    if all(stone.could_work(
                            rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz
                    ) for stone in stones):
                        print(rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz)
                        raise Exception("FINAL ANSWER")

                except ZeroDivisionError:
                    pass



