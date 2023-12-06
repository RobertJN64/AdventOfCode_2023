def main():
    with open("Day06/day06.txt") as f:
        lines = [line.strip().replace(" ", '').split(':') for line in f.readlines()]

    max_time = int(lines[0][1])
    req_dist = int(lines[1][1])

    count = 0
    for speed in range(0, max_time):

        d = (max_time - speed) * speed
        if d > req_dist:
            count += 1
            #print(speed)

    print(count)