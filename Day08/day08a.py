import util

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

    c_loc = 'AAA'

    counter = 0
    while True:
        print(counter)
        move = seq[counter%len(seq)]
        if move == 'L':
            c_loc = data[c_loc][0]
        if move == 'R':
            c_loc = data[c_loc][1]

        counter += 1
        if c_loc == 'ZZZ':
            break

    print(counter)
