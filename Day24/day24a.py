import util
import math

def solve_for_intersection(s1, i1, s2, i2):
    if s2 == s1:
        return None

    x = (i1-i2) / (s2-s1)
    y = s1 * x + i1

    assert math.isclose(y, s2 * x + i2), f"slope solve error {s1, i1, s2, i2}"
    return x, y

class Stone:
    def __init__(self, s):
        pos, vel = s.split(" @ ")
        self.x, self.y, self.z = map(int, pos.split(', '))
        self.vx, self.vy, self.vz = map(int, vel.split(', '))

    def __repr__(self):
        return f"{(self.x, self.y, self.z)} @ {(self.vx, self.vy, self.vz)}"

    def slope_inter_form(self):
        """Returns slope, intercept"""
        intercept = self.y + self.vy * self.x / -self.vx #work backwards until intersect
        slope = self.vy / self.vx
        return slope, intercept

    def repr_si_form(self):
        s, i = self.slope_inter_form()
        return f"y = {s}x + {i}"

min_pos = 200000000000000
max_pos = 400000000000000

def main():
    with open("Day24/day24.txt") as f:
        stones = [Stone(line.strip()) for line in f.readlines()]

    answer = 0
    for index, s1 in enumerate(stones):
        for s2 in stones[index+1:]:
            #print()
            slope1, intercept1 = s1.slope_inter_form()
            slope2, intercept2 = s2.slope_inter_form()
            # print(s1.repr_si_form())
            # print(s2.repr_si_form())

            result = solve_for_intersection(slope1, intercept1, slope2, intercept2)
            if result is None:
                #print("Will never intersect")
                continue

            x, y = result
            past = False
            if (x > s1.x and s1.vx < 0) or (x < s1.x and s1.vx > 0):
                #print("In the past for Stone A")
                past = True

            if (x > s2.x and s2.vx < 0) or (x < s2.x and s2.vx > 0):
                #print("In the past for Stone B")
                past = True

            if past:
                continue

            #print(x, y)
            if min_pos <= x <= max_pos and min_pos <= y <= max_pos:
                answer += 1
            # else:
            #     print("outside of test area")




    print("\nANSWER", answer)

