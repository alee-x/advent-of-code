import numpy as np
from timer import timer
import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG)


def readfile():
    fname = 'input.txt'
    with open(fname, "r") as fd:
        diagnostic_report = [[int(y) for y in list(x)] for x in fd.read().splitlines()]
        diagnostic_report = np.array(diagnostic_report)
    return diagnostic_report


def binary_to_dec(binary):
    return binary.dot(1 << np.arange(binary.shape[-1] - 1, -1, -1))


def system_rating(system_report, invert=False):
    i = 0
    do_inv = lambda x: x if not invert else (1 if invert and x == 0 else 0)
    while system_report.shape[0] != 1:
        col_vals = system_report[np.arange(system_report.shape[0]), [i]]
        most_common = do_inv(Counter(col_vals).most_common(1)[0][0])
        # check for most common tie
        if np.sum(col_vals) == (col_vals.shape[0] / 2):
            most_common = do_inv(1)
        system_report = system_report[system_report[:, i] == most_common, :]
        i += 1
    return binary_to_dec(system_report[0])


@timer('function:partone', unit='ms')
def partone(diagnostic_report):
    num_array_cols = diagnostic_report.shape[1]
    gamma = []
    for i in range(num_array_cols):
        col_vals = diagnostic_report[np.arange(diagnostic_report.shape[0]), [i]]
        most_common = Counter(col_vals).most_common(1)[0][0]
        gamma.append(most_common)
    gamma_array = np.array(gamma)
    epsilon_array = 1 - gamma_array
    gamma = binary_to_dec(gamma_array)
    epsilon = binary_to_dec(epsilon_array)
    return gamma * epsilon


@timer('function:parttwo', unit='ms')
def parttwo(diagnostic_report):
    oxy_rating = system_rating(diagnostic_report)
    co2_rating = system_rating(diagnostic_report, True)
    return oxy_rating * co2_rating


if __name__ == "__main__":
    report = readfile()
    print(partone(report))
    print(parttwo(report))
