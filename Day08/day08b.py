import util
import math

#TODO - reimplement with cycle counter

def main():
    with open("Day08/day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    seq = lines[0]
    data = {}
    for line in lines[2:]:
        start, end = line.split(' = (')
        end = end.replace(')', '')
        a, b = end.split(', ')
        data[start] = (a, b)

    c_locs = []
    for key in data:
        if key[-1] == 'A':
            c_locs.append(key)

    last_cycle_time = [0] * len(c_locs)
    cycle_maps = [0] * len(c_locs)
    ok = [False] * len(c_locs)

    counter = 0
    while True:
        # if counter%100000 == 0:
        #     print(counter)

        move = seq[counter%len(seq)]
        counter += 1

        #done = True
        for i in range(0, len(c_locs)):
            if move == 'L':
                c_locs[i] = data[c_locs[i]][0]
            if move == 'R':
                c_locs[i] = data[c_locs[i]][1]
            if c_locs[i][-1] == 'Z':
                #print(i, c_locs[i], counter % len(seq), counter + 1)
                duration = counter - last_cycle_time[i]
                last_cycle_time[i] = counter
                if cycle_maps[i] == duration:
                    ok[i] = True
                elif cycle_maps[i] == 0:
                    cycle_maps[i] = duration
                    ok[i] = True
                else:
                    raise Exception(f"INVALID CYCLE {i=} {duration=} {cycle_maps[i]=}")
        if all(ok):
            break

    print(math.lcm(*cycle_maps))
