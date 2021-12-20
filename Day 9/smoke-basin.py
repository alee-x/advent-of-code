import numpy as np
from scipy import ndimage


def fileread():
    fname = 'input.txt'
    heightmap = []
    with open(fname, 'r') as fr:
        for line in fr.read().splitlines():
            linemap = np.array([int(x) for x in line])
            heightmap.append(linemap)
    return np.array(heightmap)


def partone(heightmap):
    hmshape = heightmap.shape
    sum_low_points = 0
    for rnumb, row in enumerate(heightmap):
        row_check = [-1, 1]
        if rnumb == 0:
            row_check = [1]
        if rnumb == hmshape[0]-1:
            row_check = [-1]
        for elcount, elem in enumerate(row):
            adjacents = []
            lr_check = [-1, 1]
            if elcount == 0:
                lr_check = [1]
            if elcount == hmshape[1]-1:
                lr_check = [-1]
            for check in row_check:
                adjacents.append(heightmap[rnumb+check][elcount])
            for check in lr_check:
                adjacents.append(row[elcount+check])
            is_low_point = np.all(np.array(adjacents) > elem)
            if is_low_point:
                sum_low_points = sum_low_points + elem+1
    print(sum_low_points)


def parttwo(heightmap):
    bool_mask = np.array(heightmap) < 9
    labels, nlabels = ndimage.label(bool_mask)
    size_all_basins = []
    for label_name in range(1, nlabels+1):
        nwithlabel = heightmap[labels == label_name]
        size_all_basins.append(len(nwithlabel))
    three_largest = -np.sort(-np.array(size_all_basins))[0:3]
    print(np.prod(three_largest))


if __name__ == "__main__":
    partone(fileread())
    parttwo(fileread())