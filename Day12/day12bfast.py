
def _internal_count(markers, c_num, numbers, num_index):
    print(f"Calling internal with {markers=} {num_index=}")
    for c in markers[:c_num]:
        if c == '.':
            return 0

    if c_num < len(markers):
        if markers[c_num] == '#':
            return 0
        return combination_count(markers[c_num + 1:], numbers, num_index + 1)
    else:
        assert c_num == len(markers)
        if num_index == len(numbers) - 1:
            print('valid')
            return 1
        else:
            return 0

#cache must be wiped between each row b/c numbers are not stored
def combination_count(markers, numbers, num_index):
    print(f"Called with {markers=} {num_index=}")

    spring_count = sum(numbers[num_index:])
    # check if combos > 0
    if markers.count('#') > spring_count:
        return 0
    if markers.count("#") + markers.count("?") < spring_count:
        return 0

    markers = markers.strip('.')
    if num_index == len(numbers):
        if markers.count('#') == 0:
            print("valid")
            return 1
        else:
            return 0

    # if markers in cache[num_index]:
    #     print("ret cache")
    #     return cache[num_index][markers]

    c_num = numbers[num_index]


    if markers[0] == '#':
        retval = _internal_count(markers, c_num, numbers, num_index)
        return retval

    print()

    count = 0
    for starting_index in range(0, len(markers) - c_num + 1):
        print('------')
        r = _internal_count(markers[starting_index:], c_num, numbers, num_index)
        print('r-----', r)
        count += r
        if markers[starting_index] != '?':
            break

    #count += combination_count(markers[starting_index:], numbers, num_index, cache
    return count

def main():
    with open("Day12/day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    #print(lines[0:10])

    answer = 0

    for i, line in enumerate(lines):
        markers, numbers = line.split(' ')
        #markers: str = ((markers + '?') * 5)[:-1]
        numbers = list(map(int, numbers.split(',')))# * 5

        cache = [{} for _ in numbers]
        count = combination_count(markers, numbers, 0)
        answer += count
        print(i, count)
    print(answer)



