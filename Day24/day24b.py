from sympy import symbols, Eq, nsolve
import util

class Stone:
    def __init__(self, s):
        pos, vel = s.split(" @ ")
        self.x, self.y, self.z = map(int, pos.split(', '))
        self.vx, self.vy, self.vz = map(int, vel.split(', '))

    def __repr__(self):
        return f"{(self.x, self.y, self.z)} @ {(self.vx, self.vy, self.vz)}"


min_pos = 200000000000000
max_pos = 400000000000000

def main():
    with open("Day24/day24.txt") as f:
        stones = [Stone(line.strip()) for line in f.readlines()]

    rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz = symbols(
        "rock_x,rock_y,rock_z,rock_vx,rock_vy,rock_vz"
    )

    eqs = []
    timers = [5, 3, 4, 6, 1]
    letters = 'abcdefg'
    for index, stone in enumerate(stones):
        # print(f"Adding stone {index}")
        # s_timer = symbols(f's{letters[index]}_timer')
        # #s_timer = timers[index]
        # t_eq_x = Eq((rock_x - stone.x), (s_timer * (stone.vx - rock_vx)))
        # t_eq_y = Eq((rock_y - stone.y), (s_timer * (stone.vy - rock_vy)))
        # t_eq_z = Eq((rock_z - stone.z), (s_timer * (stone.vz - rock_vz)))
        print(f"rockx - {stone.x} = s{index}timer * ({stone.vx} - rockvx)")
        print(f"rocky - {stone.y} = s{index}timer * ({stone.vy} - rockvy)")
        print(f"rockz - {stone.z} = s{index}timer * ({stone.vz} - rockvz)")
        #eqs.extend([t_eq_x, t_eq_y, t_eq_z])

    for eq in eqs:
        print(eq)

    #print(nsolve(eqs, (rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz), (0,0,0,0,0,0)))
