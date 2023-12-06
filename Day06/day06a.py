import util

def main():
    with open("Day06/day06.txt") as f:
        lines = [line.strip().split() for line in f.readlines()]

    times = map(int, lines[0][1:])
    dists = map(int, lines[1][1:])

    answer = 1
    for max_time, req_dist in zip(times, dists):
        count = 0
        for speed in range(0, max_time):
            d = (max_time - speed) * speed
            if d > req_dist:
                count += 1
                print(speed)
        answer *= count
    print(answer)