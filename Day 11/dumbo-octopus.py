import numpy as np
from scipy import signal


def filereader():
    fname = 'input.txt'
    octos = []
    with open(fname, 'r') as fd:
        for line in fd.read().splitlines():
            rowocts = [int(x) for x in line]
            octos.append(np.array(rowocts))
    return np.array(octos)


def partone():
    octs = filereader()
    conv_matrix = np.ones((3, 3))
    step = 0
    flash_count = 0
    p1 = 0
    while True:
        step += 1
        octs = octs + 1
        flashes = octs > 9
        have_new_flashes = True
        while have_new_flashes:
            neighbour_flashes = (signal.convolve(flashes, conv_matrix, mode='same')
                                 .round(0).astype(int))
            new_octs = octs + neighbour_flashes
            new_flashes = new_octs > 9
            have_new_flashes = (new_flashes & ~flashes).sum().sum() > 0
            flashes = new_flashes
        octs = new_octs
        octs[flashes] = 0
        flash_count += flashes.sum().sum()
        if step == 100:
            p1 = flash_count
        if flashes.all().all():
            return p1, step


if __name__ == "__main__":
    p1, p2 = partone()
    print(p1)
    print(p2)