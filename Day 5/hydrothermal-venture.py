import numpy as np


def readfile():
    fname = 'input.txt'
    line_segments, all_x, all_y = [], [], []
    with open(fname, "r") as fd:
        for line in fd.read().splitlines():
            split_line = line.split(" -> ")
            line_from = np.array([int(x) for x in split_line[0].split(",")])
            line_to = np.array([int(x) for x in split_line[1].split(",")])
            all_x.append(int(line_from[0]))
            all_x.append(int(line_to[0]))
            all_y.append(int(line_from[1]))
            all_y.append(int(line_to[1]))
            line_segments.append(np.array([line_from, line_to]))
    return np.array(line_segments), [np.min(all_x), np.max(all_x)], [np.min(all_y), np.max(all_y)]


def is_straight(start, end):
    if start[0] == end[0]:
        return True, "y"
    if start[1] == end[1]:
        return True, "x"
    return False, ""


def line_gradient(start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    grad = (y2 - y1)/(x2 - x1)
    if abs(grad) == 0.0 or abs(grad) == np.inf or abs(grad) == 1.0:
        return True, abs(grad)
    return False, grad


def partone(line_segments, xrange, yrange):
    vent_map = np.zeros((yrange[1] + 1, xrange[1] + 1))
    for line in line_segments:
        line_straight, line_dir = is_straight(line[0], line[1])
        if line_straight:
            if line_dir == "x":
                start_x = np.min([line[0][0], line[1][0]])
                end_x = np.max([line[0][0], line[1][0]])
                fixed_y = line[0][1]
                for i in range(start_x, end_x + 1):
                    vent_map[fixed_y][i] += 1
            if line_dir == "y":
                start_y = np.min([line[0][1], line[1][1]])
                end_y = np.max([line[0][1], line[1][1]])
                fixed_x = line[0][0]
                for i in range(start_y, end_y + 1):
                    vent_map[i][fixed_x] += 1
    return (vent_map > 1).sum()


def parttwo(line_segments, xrange, yrange):
    vent_map = np.zeros((yrange[1] + 1, xrange[1] + 1))
    for line in line_segments:
        line_sord, line_grad = line_gradient(line[0], line[1])
        if line_sord:
            if line_grad == 0.0:
                start_x = np.min([line[0][0], line[1][0]])
                end_x = np.max([line[0][0], line[1][0]])
                fixed_y = line[0][1]
                for i in range(start_x, end_x + 1):
                    vent_map[fixed_y][i] += 1
            if line_grad == np.inf:
                start_y = np.min([line[0][1], line[1][1]])
                end_y = np.max([line[0][1], line[1][1]])
                fixed_x = line[0][0]
                for i in range(start_y, end_y + 1):
                    vent_map[i][fixed_x] += 1
            if line_grad == 1.0:
                diff_steps = line[0] - line[1]
                if diff_steps[0] > 0:
                    xstep = -1
                else:
                    xstep = 1
                if diff_steps[1] > 0:
                    ystep = -1
                else:
                    ystep = 1
                xcs = [i for i in range(line[0][0], line[1][0]+xstep, xstep)]
                ycs = [i for i in range(line[0][1], line[1][1]+ystep, ystep)]
                for i in range(len(xcs)):
                    vent_map[ycs[i]][xcs[i]] += 1
    return (vent_map > 1).sum()


if __name__ == "__main__":
    lines, xr, yr = readfile()
    print(partone(lines, xr, yr))
    lines, xr, yr = readfile()
    print(parttwo(lines, xr, yr))