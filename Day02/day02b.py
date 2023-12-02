def main():
    with open("Day02/day02.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])



    answer = 0
    for i, line in enumerate(lines):
        game_id, data = line.split(':')
        rounds = data.split(';')

        counts = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for r in rounds:
            r = r.strip().split(', ')
            for color in r:
                qty, color = color.split(' ')
                counts[color] = max(counts[color], int(qty))
        pwr = 1
        for value in counts.values():
            pwr *= value
        print(pwr)
        answer += pwr

    print(answer)