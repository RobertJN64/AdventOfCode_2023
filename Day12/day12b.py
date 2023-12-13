import util

def quick_valid(markers, spring_count):
    if markers.count('#') > spring_count:
        return False
    if markers.count("#") + markers.count("?") < spring_count:
        return False
    return True

def resolve_possibilties(item, numbers, number_index, cache):
    #print(f"Called with {item} {number_index}")
    count = 0

    item = item.strip('.')
    if not quick_valid(item, sum(numbers[number_index:])):
        return 0

    if item in cache[number_index]:
        return cache[number_index][item]

    if item[0] == '?' and len(item) > 1:
        count += resolve_possibilties(item[1:], numbers, number_index, cache)

    seq_len = numbers[number_index]
    if len(item) < seq_len:
        cache[number_index][item] = count
        return count
    if any([c == '.' for c in item[0:seq_len]]):
        cache[number_index][item] = count
        return count
    if len(item) > seq_len and item[seq_len] == '#':
        cache[number_index][item] = count
        return count

    new_item = item[seq_len + 1:]
    if '#' not in new_item and number_index == len(numbers) - 1:
        #print(f"Found valid {item}")
        cache[number_index][item] = count + 1
        return 1 + count
    elif new_item == '' or number_index == len(numbers) - 1:
        cache[number_index][item] = count
        return count
    else:
        retval = count + resolve_possibilties(new_item, numbers, number_index + 1, cache)
        cache[number_index][item] = retval
        return retval


def main():
    with open("Day12/day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    #print(lines[0:10])

    answer = 0

    for i, line in enumerate(lines):
        markers, numbers = line.split(' ')
        markers: str = ((markers + '?') * 5)[:-1]
        numbers = list(map(int, numbers.split(','))) * 5
        cache = [{} for _ in numbers]
        count = resolve_possibilties(markers, numbers, 0, cache)
        answer += count
        print(i, count)
    print(answer)
