import copy
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

    return [min_x, max_x, min_y, max_y, min_z, max_z]

#@util.debug_IO
def check_partial_overlap(start, end, v1, v2):
    return start <= v1 <= end or start <= v2 <= end

def check_range_overlap(start1, end1, start2, end2):
    return check_partial_overlap(start1, end1, start2, end2) or check_partial_overlap(start2, end2, start1, end1)

def simulate_iteration(bricks, verbose=True):
    total_moved = set()

    done = False
    while not done:
        if verbose:
            print("loop iteration...")
            print(sum(brick[4] for brick in bricks) / len(bricks))
        moved = 0

        done = True
        for b1_index, b1 in enumerate(bricks):
            min_x, max_x, min_y, max_y, bottom_z, _ = b1

            if bottom_z == 1:
                continue

            for b2_index, b2 in enumerate(bricks):
                min_x2, max_x2, min_y2, max_y2, _, support_z = b2
                if bottom_z - 1 == support_z:
                    # print(f"{b1_index} one layer above {b2_index}")

                    if (check_range_overlap(min_x, max_x, min_x2, max_x2) and
                            check_range_overlap(min_y, max_y, min_y2, max_y2)):
                        # print(f"{b1_index} contacts {b2_index}")
                        break

            else:
                b1[4] -= 1
                b1[5] -= 1
                done = False
                moved += 1
                total_moved.add(b1_index)

        if verbose:
            print(str(round(moved / len(bricks) * 100, 3)) + '%')
            print()

    return len(total_moved)

def main():
    with open("Day22/day22.txt") as f:
        bricks = [line.strip().split('~') for line in f.readlines()]
    bricks = [(list(map(int, a.split(','))), list(map(int, b.split(',')))) for (a,b) in bricks]
    bricks = [get_brick_min_max(brick) for brick in bricks]

    simulate_iteration(bricks)

    print("------")
    answer = 0
    for bindex, brick in enumerate(bricks):
        t_b = copy.deepcopy(bricks)
        t_b.remove(brick)
        count = simulate_iteration(t_b, verbose=False)
        answer += count
        print(bindex, count)
    print("\nFINAL ANSWER:", answer)

