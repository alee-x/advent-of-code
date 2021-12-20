import re

closers = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}


def partone():
    fname = "input.txt"
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    found_illegals = 0
    incomplete_lines = []
    with open(fname, "r") as fr:
        for line in fr.read().splitlines():
            is_corrupt, first_illegal = rec_search(line, closers)
            if is_corrupt:
                found_illegals = found_illegals + scores[first_illegal]
                continue
            incomplete_lines.append(line)
    print(found_illegals)
    return incomplete_lines


def rec_search(sstring, vdict):
    sstring_len = len(sstring)
    nstring_len = 0
    while sstring_len != nstring_len:
        sstring_len = len(sstring)
        for key, value in vdict.items():
            sstring = sstring.replace(key + value, '')
        nstring_len = len(sstring)
    for char in sstring:
        if char not in vdict.keys():
            return True, char
    return False, ''


def incomp_search(sstring, vdict):
    sstring_len = len(sstring)
    nstring_len = 0
    while sstring_len != nstring_len:
        sstring_len = len(sstring)
        for key, value in vdict.items():
            sstring = sstring.replace(key + value, '')
        nstring_len = len(sstring)
    return sstring


def parttwo(lines):
    scoretable = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    scores = []
    for line in lines:
        line_score = 0
        needs_closing = incomp_search(line, closers)
        for bracket in needs_closing[::-1]:
            closer = closers[bracket]
            line_score = line_score * 5
            line_score = line_score + scoretable[closer]
        scores.append(line_score)
    scores = sorted(scores)
    middleval = int((len(scores)-1)/2)
    print(scores[middleval])


if __name__ == "__main__":
    incompletes = partone()
    parttwo(incompletes)
