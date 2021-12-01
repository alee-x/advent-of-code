import numpy as np
from timer import timer, get_timer
import logging
logging.basicConfig(level=logging.DEBUG)


def readfile():
    fname = 'challenge1-input.txt'
    with open(fname, "r") as fd:
        measures = [int(x) for x in fd.read().splitlines()]
    return measures


@timer('function:partone', unit='s')
def partone():
    depth_measures = readfile()
    num_increasing = len([x for x in range(1, len(depth_measures)) if depth_measures[x] - depth_measures[x - 1] > 0])
    return num_increasing


@timer('function:parttwo', unit='s')
def parttwo():
    depth_measures = readfile()
    sliding_window = [np.sum([depth_measures[x], depth_measures[x + 1], depth_measures[x + 2]])
                      for x in range(0, len(depth_measures) - 2)]
    num_increasing = len([x for x in range(1, len(sliding_window)) if sliding_window[x] - sliding_window[x - 1] > 0])
    return num_increasing


if __name__ == "__main__":
    print(partone())
    print(parttwo())
