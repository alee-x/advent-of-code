import numpy as np


def readfile():
    fname = 'challenge1-input.txt'
    with open(fname, "r") as fd:
        measures = [int(x) for x in fd.read().splitlines()]
    return measures


def partone():
    depth_measures = readfile()
    is_increasing = [depth_measures[x] - depth_measures[x - 1] for x in range(1, len(depth_measures))]
    return len(list(filter(lambda x: (x > 0), is_increasing)))


def parttwo():
    depth_measures = readfile()
    sliding_window = [np.sum([depth_measures[x], depth_measures[x + 1], depth_measures[x + 2]])
                      for x in range(0, len(depth_measures) - 2)]
    is_increasing = [sliding_window[x] - sliding_window[x - 1] for x in range(1, len(sliding_window))]
    return len(list(filter(lambda x: (x > 0), is_increasing)))


if __name__ == "__main__":
    print(partone())
    print(parttwo())
    