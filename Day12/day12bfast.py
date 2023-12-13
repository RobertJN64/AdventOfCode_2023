#cache must be wiped between each row b/c numbers are not stored
import util

@util.debug_IO
def combination_count(markers, numbers, num_index):
    spring_count = sum(numbers[num_index:])
    # check if combos > 0
    if markers.count('#') > spring_count:
        return 0
    if markers.count("#") + markers.count("?") < spring_count:
        return 0

    markers = markers.strip('.')
    if num_index == len(numbers):
        if markers.count('#') == 0:
            return 1
        else:
            return 0


    c_num = numbers[num_index]

    count = 0
    for starting_index in range(0, len(markers) - c_num + 1):
        if '#' in markers[0:starting_index]:
            return count

        for c in markers[starting_index:starting_index+c_num]:
            if c == '.':
                break
        else:
            count += combination_count(markers[starting_index+c_num+1:], numbers, num_index+1)

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



