def main():
    with open("Day02/day02.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    counts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    answer = 0
    for i, line in enumerate(lines):
        _, data = line.split(':') #throw out game_id - they are in order so we just use (i+1)
        rounds = data.split(';') #round = each time items removed

        valid = True
        for r in rounds:
            r = r.strip().split(', ')
            for color in r:
                qty, color = color.split(' ')
                if int(qty) > counts[color]:
                    valid = False

        if valid:
            answer += (i+1)


    print(answer)