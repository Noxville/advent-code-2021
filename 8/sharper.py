def case(words, output):
    B, E, F, ONE = None, None, None, None
    for _ in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        sm = sum([w.count(_) for w in words])
        if sm == 4: E = _
        elif sm == 6: B = _
        elif sm == 9: F = _

    lookup = {}
    for w in sorted(words, key=lambda x: len(x)):
        lookup["".join(sorted(w))] = {
            # E is present, B is present, F is present, length of string without EBF, contains the letters of ONE
            (1, 1, 1, 3, 1): 0,
            (0, 0, 1, 1, 0): 1,
            (1, 0, 0, 4, 0): 2,
            (0, 0, 1, 4, 1): 3,
            (0, 1, 1, 2, 1): 4,
            (0, 1, 1, 3, 0): 5,
            (1, 1, 1, 3, 0): 6,
            (0, 0, 1, 2, 1): 7,
            (1, 1, 1, 4, 1): 8,
            (0, 1, 1, 4, 1): 9
        }[(
            w.count(E),
            w.count(B),
            w.count(F),
            len(w) - (w.count(E) + w.count(B) + w.count(F)),
            0 if ONE is None else int(w.count(ONE[0]) == 1 and w.count(ONE[1]) == 1)
        )]

        if len(w) == 2:
            ONE = w
    return [lookup["".join(sorted(w))] for w in output]

with open('case1.txt') as fin:
    counter = 0
    for line in fin.readlines():
        sp = line.split(" | ")
        _words = [e.strip() for e in sp[0].split(" ")]
        _output = [e.strip() for e in sp[1].split(" ")]
        nums = case(_words, _output)
        counter += int("".join([str(_) for _ in nums]))
    print(counter)
