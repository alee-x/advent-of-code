import numpy as np
from collections import Counter


def filereader():
    file = "input.txt"
    crabs = []
    with open(file, "r") as fd:
        for line in fd.read().splitlines():
            crabs = [int(x) for x in line.split(',')]
    return crabs


def partone(crabs):
    move_sums = []
    for position in list(set(crabs)):
        difference_array = np.array(crabs) - np.array([position for x in crabs])
        difference_array = [np.abs(x) for x in difference_array]
        move_sums.append(np.sum(difference_array))
    print(np.min(move_sums))


def parttwo(crabs):
    # for the given sequence, a_n = 1/2 * n(n+1)
    move_sums = []
    for position in range(np.min(crabs), np.max(crabs)):
        difference_array = np.array(crabs) - np.array([position for x in crabs])
        difference_array = [np.abs(x) for x in difference_array]
        tmp = [int((1/2)*x*(x+1)) for x in difference_array]
        move_sums.append(np.sum(tmp))
    print(np.min(move_sums))


if __name__ == "__main__":
    partone(filereader())
    parttwo(filereader())
