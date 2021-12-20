from collections import defaultdict


def fileread():
    fname = "input.txt"
    neighbours = defaultdict(list)
    with open(fname, 'r') as fr:
        for line in fr.read().splitlines():
            a, b = line.strip().split('-')
            neighbours[a] += [b]
            neighbours[b] += [a]
    return neighbours


def count(part, seen=[], cave='start'):
    neighbours = fileread()
    if cave == 'end': return 1
    if cave in seen:
        if cave == 'start': return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(count(part, seen + [cave], n)
               for n in neighbours[cave])


def partone():
    answer = count(part=1)
    print(answer)

def parttwo():
    answer = count(part=2)
    print(answer)


if __name__ == "__main__":
    partone()
    parttwo()
