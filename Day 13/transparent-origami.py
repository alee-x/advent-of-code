import numpy as np
import matplotlib.pyplot as plt


def fileread():
    fname = "input.txt"
    coords = []
    instructions = []
    with open(fname, 'r') as fd:
        for line in fd.read().splitlines():
            if len(line) == 0:
                continue
            if line[0].isnumeric():
                tmp = [int(x) for x in line.split(",")]
                coords.append(tmp)
                continue
            else:
                linesplit = line.split("fold along ")
                fold_split = linesplit[1].split("=")
                instructions.append(fold_split)
    return coords, instructions


def max_val(points, axis):
    mv = 0
    for point in points:
        if point[axis] > mv:
            mv = point[axis]
    return mv


def partone():
    coords, folds = fileread()
    folds = [folds[0]]
    for fold in folds:
        if fold[0] == 'y':
            fold_dir = 1
        else:
            fold_dir = 0
        fold_point = int(fold[1])
        for point in coords:
            if point[fold_dir] > fold_point:
                point[fold_dir] = np.abs(point[fold_dir] - (fold_point * 2))
    point_set = ["{0},{1}".format(x[0], x[1]) for x in coords]
    print(len(set(point_set)))


def parttwo():
    coords, folds = fileread()
    for fold in folds:
        if fold[0] == 'y':
            fold_dir = 1
        else:
            fold_dir = 0
        fold_point = int(fold[1])
        for point in coords:
            if point[fold_dir] > fold_point:
                point[fold_dir] = np.abs(point[fold_dir] - (fold_point * 2))
    point_set = set(["{0},{1}".format(x[0], x[1]) for x in coords])
    point_list = list(point_set)
    point_list = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in point_list]
    drawn_board(point_list)


def drawn_board(points):
    x = [x for x, y in points]
    y = [-y for x, y in points]
    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    partone()
    parttwo()
