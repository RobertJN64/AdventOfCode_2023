import util

def main():
    with open("Day05/day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])


    seeds = list(map(int, lines[0].replace('seeds: ', '').split()))
    seed_next_values = [-1] * len(seeds)
    print(seeds)
    lines = lines[1:]

    for i in range(0, len(lines)):
        line = lines[i]
        if line == '': #starting a new soil map
            print(lines[i +1])
            i += 2

            while i < len(lines) and lines[i] != '':
                dest_start, src_start, range_length = list(map(int, lines[i].split()))
                print(dest_start, src_start, range_length)

                for index, seed in enumerate(seeds):
                    if src_start <= seed < src_start + range_length:
                        seed_next_values[index] = dest_start + (seed - src_start)


                for index, sv in enumerate(seed_next_values):
                    if sv == -1:
                        seed_next_values[index] = seeds[index]

                i += 1
            seeds = seed_next_values
            seed_next_values = [-1] * len(seeds)

    print(min(seeds))


