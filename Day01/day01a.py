def main():
    with open("Day01/day01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0
    for line in lines:
        v = ""
        for c in line:
            if c.isnumeric():
                v += c
                break

        for c in line[::-1]:
            if c.isnumeric():
                v += c
                break

        answer += int(v)

    print(answer)