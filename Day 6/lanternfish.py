from collections import Counter
import numpy as np
import math
from tqdm import tqdm


def readfile():
    fname = 'input.txt'
    fish = []
    fishstr = ""
    with open(fname, "r") as fd:
        for line in fd.read().splitlines():
            fish = [int(x) for x in line.split(",")]
            fishstr = line
    return fish, fishstr


def partone(all_fish, ndays):
    for i in tqdm(range(ndays)):
        today_new_fish = 0
        for j in range(len(all_fish)):
            fish_age = all_fish[j]
            if fish_age == 0:
                all_fish[j] = 6
                today_new_fish += 1
            else:
                all_fish[j] = all_fish[j] - 1
        for k in range(today_new_fish):
            all_fish.append(8)
    return len(all_fish)


def parttwo(all_fish, ndays):
    for i in tqdm(range(ndays)):
        today_new_fish = 0
        for j in range(len(all_fish)):
            fish_age = all_fish[j]
            if fish_age == 0:
                all_fish[j] = 6
                today_new_fish += 1
            else:
                all_fish[j] = all_fish[j] - 1
        for k in range(today_new_fish):
            all_fish.append(8)
    return len(all_fish)


def solve(input):
    fishes = Counter(int(n) for n in input.strip().split(','))
    for time in range(256):
        spawn = fishes[0]
        for cycle in range(8):
            fishes[cycle] = fishes[cycle + 1]
        fishes[8] = spawn
        fishes[6] += spawn

    return sum(fishes.values())


if __name__ == "__main__":
    fish, fishstr = readfile()
    ndays = 80
    print(partone(fish, ndays))
    new_fish, fishstr = readfile()
    next_days = 256
    print(solve(fishstr))
