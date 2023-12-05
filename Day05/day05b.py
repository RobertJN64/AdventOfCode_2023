import util

#SEED RANGE COMPUTER

def main():
    with open("Day05/day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]



    _t = list(map(int, lines[0].replace('seeds: ', '').split()))
    seeds = []
    for i in range(0, len(_t), 2):
        seeds.append((_t[i], _t[i+1]))
    print(seeds)

    lines = lines[1:]

    for i in range(0, len(lines)):
        line = lines[i]
        if line == '': #starting a new soil map
            print(lines[i +1])
            i += 2

            maps = []
            while i < len(lines) and lines[i] != '':
                dest_start, src_start, range_length = list(map(int, lines[i].split()))
                maps.append((dest_start, src_start, range_length))

                i += 1

            maps.sort(key=lambda x: x[1])
            print("MAPS: ", maps)

            j = 0
            new_seeds = []
            while j < len(seeds):
                seed, l = seeds[j]
                for dest_start, src_start, range_length in maps:
                    if src_start <= seed < src_start + range_length: #seed drops into range
                        seed_end_v = seed + l
                        input_end_v = src_start + range_length

                        if seed_end_v <= input_end_v:
                            new_seeds.append((dest_start + (seed - src_start), l))
                            break

                        else:

                        new_l = l - range_length

                        if new_l > 0:
                            seed = seed + range_length
                            l = new_l
                        else:
                            break

                    elif src_start <= seed + l and seed < src_start + range_length:
                        # ok - we need to slice off some values from the bottom - we can add these as raw
                        print("app", seed, src_start-seed)
                        new_seeds.append((seed, src_start-seed))

                        seed = src_start
                        l = l - (src_start-seed)

                        new_seeds.append((dest_start + (seed - src_start), min(l, range_length)))
                        new_l = l - range_length

                        if new_l > 0:
                            seed = seed + range_length
                            l = new_l
                        else:
                            break

                else:
                    new_seeds.append((seed, l))

                j += 1



            seeds = new_seeds
            print("SEEDS", seeds)

    m = float('inf')
    for s, r in seeds:
        m = min(m, s)
    print(m)


