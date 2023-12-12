import util

def resolve_possibilties(item, numbers, number_index):
    count = 0

    item = item.strip('.')
    if item[0] == '?' and len(item) > 1:
        count += resolve_possibilties(item[1:], numbers, number_index)

    seq_len = numbers[number_index]
    if len(item) < seq_len:
        return count
    if any([c == '.' for c in item[0:seq_len]]):
        return count
    if len(item) > seq_len and item[seq_len] == '#':
        return count

    new_item = item[seq_len + 1:]
    if new_item == '' and number_index == len(numbers) - 1:
        print(f"Found valid {item}")
        return 1 + count
    elif new_item == '' or number_index == len(numbers) - 1:
        return count
    else:
        return count + resolve_possibilties(new_item, numbers, number_index + 1)


def main():
    with open("Day12/day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    #print(lines[0:10])

    answer = 0

    for i, line in enumerate(lines[5:]):

        markers, numbers = line.split(' ')
        numbers = list(map(int, numbers.split(',')))

        # markers: str = ((markers + '?') * 5)[:-1]
        # numbers = list(map(int, numbers.split(','))) * 5

        #spring_count = sum(numbers)

        count = resolve_possibilties(markers, numbers, 0)
        answer += count
        print(i, count)
    print(answer)
