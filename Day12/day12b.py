import util

def is_valid(markers: str, numbers: list[int]):
    numbers = [x for x in numbers] #copy

    c_count = 0
    for m in markers:
        if m == '#':
            c_count += 1
        if m == '.':
            if c_count > 0:
                if len(numbers) == 0 or numbers[0] != c_count:
                    return False
                numbers.pop(0)

            c_count = 0

    if c_count > 0:
        if len(numbers) == 0 or numbers[0] != c_count:
            return False
        numbers.pop(0)
    if len(numbers) > 0:
        return False
    return True

def quick_valid(markers, spring_count):
    if markers.count('#') > spring_count:
        return False
    if markers.count("#") + markers.count("?") < spring_count:
        return False
    return True


def main():
    with open("Day12/day12fast.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0

    for i, line in enumerate(lines):
        count = 0
        markers, numbers = line.split(' ')
        numbers = list(map(int, numbers.split(',')))
        spring_count = sum(numbers)
        #assert is_valid(markers, numbers), f"{markers=} {numbers=}"

        queue: list[str] = [markers]
        while queue:
            item = queue.pop(0)
            if '?' in item:
                new_item = item.replace('?', '#', 1)
                if quick_valid(new_item, spring_count):
                    queue.append(new_item)

                new_item = item.replace('?', '.', 1)
                if quick_valid(new_item, spring_count):
                    queue.append(new_item)

            else:
                if is_valid(item, numbers):
                    #print(item, numbers)
                    count += 1
                # else:
                #     print(item, numbers, 'x')
        answer += count
        print(i, count)
    print(answer)
