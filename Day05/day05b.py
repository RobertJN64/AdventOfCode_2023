import util

#SEED RANGE COMPUTER

def main():
    with open("Day05/day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]



    _t = list(map(int, lines[0].replace('seeds: ', '').split()))
    seeds = []
    for i in range(0, len(_t), 2):
        seeds.append((_t[i], _t[i+1]))


    lines = lines[1:]

    for i in range(0, len(lines)):
        line = lines[i]
        if line == '': #starting a new soil map

            i += 2

            maps = []
            while i < len(lines) and lines[i] != '':
                dest_start, src_start, range_length = list(map(int, lines[i].split()))
                maps.append((dest_start, src_start, range_length))

                i += 1

            maps.sort(key=lambda x: x[1])


            j = 0
            new_seeds = []
            while j < len(seeds):
                seed, l = seeds[j]
                if l == 0:
                    j+=1
                    continue

                for dest_start, src_start, range_length in maps:
                    if seed < src_start:
                        if l < src_start-seed:
                            new_seeds.append((seed, l)) #range smaller than smallest
                        else:
                            new_seeds.append((seed, src_start-seed))  # range smaller than smallest
                            seeds.append((src_start, l-(src_start-seed)))
                        break

                    if src_start <= seed < src_start + range_length: #seed drops into range
                        if l < range_length - (seed-src_start):
                            new_seeds.append((dest_start + (seed-src_start), l)) #falls entirely in range
                        else: #extends past edge
                            new_seeds.append((dest_start + (seed-src_start), range_length - (seed-src_start)))  # range smaller than smallest
                            seeds.append((src_start + range_length, l - (range_length - (seed-src_start))))
                            #print(seeds)
                        break


                    else:
                        pass
                        #TOO HIGH, KEEP CEHCKINF FOR HIGHER ONES

                else:
                    new_seeds.append((seed, l))

                j += 1

            seeds = new_seeds

    m = float('inf')
    for s, r in seeds:
        m = min(m, s)
    print(m)


