import util

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

    counter = 0
    while True:
        if counter%100000 == 0:
            print(counter)

        move = seq[counter%len(seq)]

        done = True
        for i in range(0, len(c_locs)):
            if move == 'L':
                c_locs[i] = data[c_locs[i]][0]
            if move == 'R':
                c_locs[i] = data[c_locs[i]][1]
            if c_locs[i][-1] != 'Z':
                done = False

        #print(c_locs)

        counter += 1
        if done:
            break

    print(counter)
