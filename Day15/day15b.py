import util

def chash(x: str):
    cval = 0
    for c in x:
        cval += ord(c)
        cval *= 17
        cval%=256
    return cval

def main():
    with open("Day15/day15.txt") as f:
        lines = f.readlines()[0].strip().split(',')
    print(lines[0:10])

    boxes = [[] for _ in range(256)]

    for line in lines:
        label = ''
        cmd = ''
        num = 0
        for c in line:
            if c.isalpha():
                label += c
            elif c.isnumeric():
                num = int(c)
            else:
                cmd = c

        hashval = chash(label)
        #print(label, cmd, num, hashval)

        box = boxes[hashval]

        if cmd == '=':
            for index, t in enumerate(box):
                if t[0] == label:
                    box[index] = (label, num)
                    break

            else:
                box.append((label, num))

        elif cmd == '-':
            for index, t in enumerate(box):
                if t[0] == label:
                    box.pop(index)
                    break

        else:
            raise Exception("INVALID CMD")


        #print(boxes)

    score = 0
    for loc, box in enumerate(boxes):
        for indxex, (lense, power) in enumerate(box):
            score += (loc+1) * (indxex+1) * power
    print(score)
