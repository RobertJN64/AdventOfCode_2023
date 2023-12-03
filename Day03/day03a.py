import util

def check_pos(lines, x, y):
    valid = False
    if util.out_of_bounds(lines, x, y):
        return False

    cd = lines[y][x]
    if not (cd.isnumeric() or cd == '.'):
        valid = True

    return valid

def main():
    with open("Day03/day03.txt") as f:
        lines = [line.strip() + '.' for line in f.readlines()] # adding '.' handles numbers at end of line for free

    numbers = []
    for y, line in enumerate(lines):
        start_index = 0
        number_acc = ""
        for x, c in enumerate(line):
            if c.isnumeric():
                if number_acc == "":
                    start_index = x
                number_acc += c
            elif number_acc != "":
                #check surrounding
                valid = False
                for yd in [-1, 0, 1]:
                    for xd in range(start_index-1, x+1):
                        valid = valid or check_pos(lines, xd, y+yd)

                if valid:
                    numbers.append(int(number_acc))

                print(number_acc, valid)

                number_acc = ""
    print(sum(numbers))

