import util

def main():
    with open("Day04/day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    card_counts = {}

    answer = 0
    for card in lines:
        i, card = card.split(':')
        i = int(i.replace("Card ", ''))
        card_counts[i] = card_counts.get(i, 0) + 1

        win, mine = card.split('|')
        win = win.strip().split()
        mine = mine.strip().split()
        count = 0
        for item in mine:
            if item in win:
                count += 1

        for idel in range(1, count+1):
            card_counts[i+idel] = card_counts.get(i+idel, 0) + card_counts.get(i)

    print(sum(card_counts.values()))