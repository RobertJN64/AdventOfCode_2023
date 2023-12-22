import util

X = 0
Y = 1
Z = 2

CORNER_1 = 0
CORNER_2 = 1

def get_brick_min_max(brick):
    min_x = min(brick[CORNER_1][X], brick[CORNER_2][X])
    max_x = max(brick[CORNER_1][X], brick[CORNER_2][X])

    min_y = min(brick[CORNER_1][Y], brick[CORNER_2][Y])
    max_y = max(brick[CORNER_1][Y], brick[CORNER_2][Y])

    min_z = min(brick[CORNER_1][Z], brick[CORNER_2][Z])
    max_z = max(brick[CORNER_1][Z], brick[CORNER_2][Z])

    return min_x, max_x, min_y, max_y, min_z, max_z

#@util.debug_IO
def check_partial_overlap(start, end, v1, v2):
    return start <= v1 <= end or start <= v2 <= end

def check_range_overlap(start1, end1, start2, end2):
    return check_partial_overlap(start1, end1, start2, end2) or check_partial_overlap(start2, end2, start1, end1)

def main():
    with open("Day22/day22.txt") as f:
        bricks = [line.strip().split('~') for line in f.readlines()]
    bricks = [(list(map(int, a.split(','))), list(map(int, b.split(',')))) for (a,b) in bricks]
    print(bricks[0:10])

    done = False
    while not done:
        print("loop iteration...")
        print(sum(brick[CORNER_1][Z] for brick in bricks) / len(bricks))
        moved = 0

        done = True
        for b1_index, b1 in enumerate(bricks):
            min_x, max_x, min_y, max_y, bottom_z, _ = get_brick_min_max(b1)

            if bottom_z == 1:
                continue

            for b2_index, b2 in enumerate(bricks):
                min_x2, max_x2, min_y2, max_y2, _, support_z = get_brick_min_max(b2)
                if bottom_z - 1 == support_z:
                    #print(f"{b1_index} one layer above {b2_index}")


                    if (check_range_overlap(min_x, max_x, min_x2, max_x2) and
                        check_range_overlap(min_y, max_y, min_y2, max_y2)):
                        #print(f"{b1_index} contacts {b2_index}")
                        break

            else:
                b1[CORNER_1][Z] -= 1
                b1[CORNER_2][Z] -= 1
                done = False
                moved += 1

        print(str(round(moved/len(bricks) * 100, 3)) + '%')

        print()

    print("------")

    safe_to_remove = [True] * len(bricks)
    for b1_index, b1 in enumerate(bricks):
        min_x, max_x, min_y, max_y, bottom_z, _ = get_brick_min_max(b1)

        depends_on = []
        for b2_index, b2 in enumerate(bricks):
            min_x2, max_x2, min_y2, max_y2, _, support_z = get_brick_min_max(b2)
            if bottom_z - 1 == support_z:
                print(f"{b1_index} one layer above {b2_index}")

                if (check_range_overlap(min_x, max_x, min_x2, max_x2) and
                        check_range_overlap(min_y, max_y, min_y2, max_y2)):

                    depends_on.append(b2_index)

        if len(depends_on) == 1:
            print(f"{b1_index} depends on {depends_on[0]}")
            safe_to_remove[depends_on[0]] = False

    print("\nFINAL ANSWER:")
    print(safe_to_remove.count(True))



