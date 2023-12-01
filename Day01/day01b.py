replace = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def parse(line: str, r):
    for i in r:
        c = line[i]
        if c.isnumeric():
            return c

        for key in replace:
            if line[i:i + len(key)] == key:
                return replace[key]

def main():
    with open("Day01/day01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0
    for line in lines:
        answer += int(parse(line, range(0, len(line))) +
                      parse(line, range(len(line) - 1, -1, -1)))
    print(answer)