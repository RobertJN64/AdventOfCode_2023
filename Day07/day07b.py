import util

order = "AKQT98765432J"

def get_valid_cards(x):
    if x == 'J':
        return "AKQT98765432"
    return x

def get_card_value(card):
    return order[::-1].index(card)

class Hand:
    def __init__(self, cards, bet):
        self.cards = list(cards)
        self.bet = int(bet)

    def get_hand_score(self):
        best_count = 0
        best_non_j_count = 0
        for v in range(0, 5):
            count = 0
            for i in range(0, 5):
                if self.cards[i] == self.cards[v]:
                    count += 1
            if count >= best_count:
                best_count = count
            if self.cards[v] != 'J' and count > best_non_j_count:
                best_non_j_count = count

        joker_score = self.cards.count('J')
        if best_non_j_count + joker_score == 5: #Five of a kind
            return 100
        if best_non_j_count + joker_score == 4: #Four of a kind
            return 90
        if best_count == 3 and len(set(self.cards)) == 2: #Full house
            return 80
        if best_count == 2 and len(set(self.cards)) == 3 and joker_score == 1: #Two pair -> Full house (with joker)
            return 80

        if best_count == 3 and len(set(self.cards)) == 3: #Three of a kind
            return 70
        if best_count == 2 and len(set(self.cards)) == 4 and joker_score == 1: #One pair -> Three of a kind (with joker)
            return 70
        if best_count == 2 and len(set(self.cards)) == 4 and joker_score == 2: #One pair -> Three of a kind (with joker)
            return 70

        if best_count == 2 and len(set(self.cards)) == 3: #Two pair
            return 60
        if best_count == 2 and len(set(self.cards)) == 4: #One pair
            return 50

        if best_count == 1 and joker_score == 1: #One pair
            return 50

        #print(self)
        assert best_count == 1 and len(set(self.cards)) == 5 and joker_score == 0
        return 0

    def get_old_score(self):
        best_count = 0
        for v in range(0, 5):
            count = 0
            for i in range(0, 5):
                if self.cards[i] == self.cards[v]:
                    count += 1
            best_count = max(count, best_count)

        if best_count == 5: #Five of a kind
            return 100
        if best_count == 4: #Four of a kind
            return 90
        if best_count == 3 and len(set(self.cards)) == 2: #Full house
            return 80
        if best_count == 3 and len(set(self.cards)) == 3: #Three of a kind
            return 70
        if best_count == 2 and len(set(self.cards)) == 3: #Two pair
            return 60
        if best_count == 2 and len(set(self.cards)) == 4: #One pair
            return 50
        assert best_count == 1 and len(set(self.cards)) == 5
        return 0

    def validate(self):
        best_score = 0
        for c0 in get_valid_cards(self.cards[0]):
            for c1 in get_valid_cards(self.cards[1]):
                for c2 in get_valid_cards(self.cards[2]):
                    for c3 in get_valid_cards(self.cards[3]):
                        for c4 in get_valid_cards(self.cards[4]):
                            best_score = max(best_score, Hand(c0 + c1 + c2 + c3 + c4, 0).get_old_score())
        print(self, best_score, self.get_hand_score())
        assert best_score == self.get_hand_score()




    def __gt__(self, other):
        if self.get_hand_score() > other.get_hand_score():
            return True
        if self.get_hand_score() < other.get_hand_score():
            return False
        for i in range(0, 5):
            if get_card_value(self.cards[i]) > get_card_value(other.cards[i]):
                return True
            if get_card_value(self.cards[i]) < get_card_value(other.cards[i]):
                return False
        raise Exception("SAME HAND!")

    def __repr__(self):
        return ''.join(self.cards) + " " + str(self.bet)

def main():
    with open("Day07/day07.txt") as f:
        hands = [Hand(*line.strip().split()) for line in f.readlines()]

    hands.sort()
    print(hands)
    answer = 0
    for i, hand in enumerate(hands):
        #hand.validate()
        answer += hand.bet * (i+1)
    print(answer)