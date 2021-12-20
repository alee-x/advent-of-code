from collections import Counter
from tqdm import tqdm


def filereader():
    fname = "input.txt"
    poly_temp = ""
    rules = dict()
    with open(fname, 'r') as fr:
        for line_count, line in enumerate(fr.read().splitlines()):
            if line_count == 0:
                poly_temp = line
                continue
            if len(line) == 0:
                continue
            rls = line.split(" -> ")
            rules[rls[0]] = rls[1]
    return poly_temp, rules


def stepper(step_template, rules):
    new_template = [char for char in step_template]
    for i in reversed(range(len(step_template)-1)):
        pair = step_template[i]+step_template[i+1]
        if pair in rules.keys():
            new_char = rules[pair]
            new_template.insert(i+1, new_char)
    return "".join(new_template)


def partone():
    poly_template, poly_rules = filereader()
    for i in range(10):
        poly_template = stepper(poly_template, poly_rules)
    elm_count = sorted(Counter(poly_template).values())
    most_common = elm_count[-1]
    least_common = elm_count[0]
    return most_common - least_common


def parttwo():
    poly_template, poly_rules = filereader()
    poly_pairs = Counter(map(str.__add__, poly_template, poly_template[1:]))
    poly_chars = Counter(poly_template)
    for _ in range(40):
        for (a, b), c in poly_pairs.copy().items():
            x = poly_rules[a+b]
            poly_pairs[a+b] -= c
            poly_pairs[a+x] += c
            poly_pairs[x+b] += c
            poly_chars[x] += c
    print(max(poly_chars.values()) - min(poly_chars.values()))


if __name__ == "__main__":
    print(partone())
    print(parttwo())