def main():
    with open("Day01/day01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

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


    answer = 0
    for line in lines:
        v = ""
        for i, c in enumerate(line):
            if c.isnumeric():
                v += c
                break

            done = False
            for key in replace:
                if line[i:i+len(key)] == key:
                    v += replace[key]
                    done = True
                    break

            if done:
                break


        for i in range(len(line) - 1, -1, -1):
            c = line[i]
            if c.isnumeric():
                v += c
                break

            done = False
            for key in replace:
                #print(line, line[i-len(key):i+1])
                if line[i:i+len(key)] == key:
                    v += replace[key]
                    done = True
                    break

            if done:
                break

        print(v)

        answer += int(v)

    print(answer)