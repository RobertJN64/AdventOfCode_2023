import util

def get_number(lines, x, y): #work backwards to find start of number, move foward one, find number
    number_acc = ""
    while x >= 0 and lines[y][x].isnumeric():
        x -= 1
    x += 1
    startx = x
    while x < len(lines) and lines[y][x].isnumeric():
        number_acc += lines[y][x]
        x += 1
    return startx, int(number_acc)

def main():
    with open("Day03/day03.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    answer = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '*':
                numbers = set()

                for xd in [-1, 0, 1]:
                    for yd in [-1, 0, 1]:
                        if xd == 0 and yd == 0:
                            continue

                        if util.out_of_bounds(lines, x + xd, y + yd):
                            continue

                        if lines[y+yd][x+xd].isnumeric():
                            startx, num = get_number(lines, x+xd, y+yd)
                            numbers.add((startx, y+yd, num)) #ensure each number is unique based on starting pos

                if len(numbers) == 2:
                    gr = numbers.pop()[2] * numbers.pop()[2]
                    answer += gr
    print(answer)

