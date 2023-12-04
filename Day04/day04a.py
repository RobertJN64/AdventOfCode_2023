import util

def main():
    with open("Day04/day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])


    answer = 0
    for card in lines:
        _, card = card.split(':')
        win, mine = card.split('|')
        win = win.strip().split()
        mine = mine.strip().split()
        count = 0
        for item in mine:
            if item in win:
                count += 1
        if count == 0:
            score = 0
        else:
            score = 2 ** (count - 1)
        print(score)
        answer += score

    print(answer)