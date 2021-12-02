import numpy as np
from timer import timer
import logging

logging.basicConfig(level=logging.DEBUG)


def readfile():
    fname = 'input.txt'
    with open(fname, "r") as fd:
        directions = [x.split() for x in fd.read().splitlines()]
        directions = [[x[0], int(x[1])] for x in directions]
    return directions


@timer('function:partone', unit='ms')
def partone():
    dirs = [x if x[0] != "up" else [x[0], -x[1]] for x in readfile()]
    horizontal_position = np.sum([x[1] for x in dirs if x[0] == "forward"])
    depth = np.sum([x[1] for x in dirs if x[0] != "forward"])
    return horizontal_position * depth


@timer('function:parttwo', unit='ms')
def parttwo():
    directions = [x if x[0] != "up" else [x[0], -x[1]] for x in readfile()]
    horizontal, aim, depth = 0, 0, 0
    for direc in directions:
        if direc[0] != "forward":
            aim += direc[1]
        else:
            horizontal += direc[1]
            depth += aim * direc[1]
    return horizontal * depth


if __name__ == "__main__":
    print(partone())
    print(parttwo())
