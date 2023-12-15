import util

def chash(x: str):
    cval = 0
    for c in x:
        cval += ord(c)
        cval *= 17
        cval%=256
    return cval

def main():
    with open("Day15/day15.txt") as f:
        lines = f.readlines()[0].strip().split(',')
    print(lines[0:10])

    answer = 0
    for line in lines:
        answer += chash(line)
        print(chash(line))
    print(answer)
