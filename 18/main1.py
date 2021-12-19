import sys
from math import floor, ceil
from functools import reduce

DEBUG = False


def split(val):
    #if DEBUG: print(f"split = {val}")
    if isinstance(val, int):
        if val > 9:
            return True, [floor(val / 2), ceil(val / 2)]
        return False, val
    else:
        i, j = val[0], val[1]
        work_done, i = split(i)
        # print(f"work_done = {work_done}, j = {j}")
        if work_done:
            return True, [i, j]
        work_done, j = split(j)
        return work_done, [i, j]


def explode(vals, depth):
    if DEBUG: print(f"explode vals = {vals}, depth = {depth}")
    # Returns -> left, middle, right, has_changed
    if isinstance(vals, int):
        return None, vals, None, False
    if 0 == depth:
        return vals[0], 0, vals[1], True
    a, b = vals  # vals[0], vals[1]  # MUT
    l, a, r, has_changed = explode(a, depth - 1)  # explode A
    if has_changed:
        return l, [a, add_l(b, r)], None, True
    l, b, r, has_changed = explode(b, depth - 1)  # explode B
    if has_changed:
        return None, [add_r(a, l), b], r, True
    return None, vals, None, False


def add_r(i, j):
    # if DEBUG: print(f"add_r, i={i}, j={j}")
    if j is None:
        return i
    if isinstance(i, int):
        return i + j
    return [i[0], add_r(i[1], j)]


def add_l(i, j):
    # if DEBUG: print(f"add_l, i={i}, j={j}")
    if j is None:
        return i
    if isinstance(i, int):
        return i + j
    return [add_l(i[0], j), i[1]]


def add(a, b):
    if DEBUG: print(f"add a={a}, b={b}")
    ret = [a, b]
    while True:
        ignore, ret, ignore, work_done = explode(ret, 4)
        if work_done:
            continue

        work_done, ret = split(ret)
        if not work_done:
            break
    return ret


def mag(p):
    if isinstance(p, int):
        return p
    else:
        return (2 * mag(p[1])) + (3 * mag(p[0]))


if False:
    # Let's test some explosions
    for case, expected in [
        ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
        ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
        ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
        ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]),
        ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])
    ]:
        print(f"Case {case}")
        boom = explode(case, 4)[1]
        print(f"exploded: {boom}")
        assert boom == expected
        print("")

    # Process
    assert add([[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    sys.exit(0)

with open('case1.txt') as fin:
    cases = [eval(e.strip()) for e in fin.readlines()]
    ans = reduce(add, cases)
    print(mag(ans))

    best = None
    for left in cases:
        for right in [c for c in cases if c != left]:
            this_mag = mag(add(left, right))
            if best is None or this_mag > best:
                best = this_mag
    print(best)
