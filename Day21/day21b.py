import util

def main():
    with open("Day21/day21.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])


    answer = 0
    for line in lines:
        answer += int(line)

    print(answer)