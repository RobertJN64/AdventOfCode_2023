import util

def main():
    with open("Day09/day09.txt") as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    #print(lines[0:10])


    answer = 0
    for line in lines:
        difs = [line]
        done = False
        while not done:
            c_difs = []
            for num, next_num in zip(line[:-1], line[1:]):
                c_difs.append(next_num - num)
            if all([x == 0 for x in c_difs]):
                done = True
            else:
                difs.append(c_difs)
                line = c_difs

        for i in range(len(difs) - 2, -1, -1):
            difs[i][-1] += difs[i+1][-1]
        print(difs[0][-1])
        answer += difs[0][-1]
    print(answer)
