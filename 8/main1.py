from itertools import permutations


def case(words, output):
    segs = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    phrases = {"".join(v): k for (k, v) in segs.items()}

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for perm in permutations(alpha):
        pegs, togo = dict(zip(perm, alpha)), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        for word in words:
            translated = "".join(sorted([pegs[c] for c in word]))
            if translated in phrases:
                togo.remove(phrases[translated])
            else:
                break
        if len(togo) == 0:
            ret = []
            for out_word in output:
                translated_out = "".join(sorted([pegs[_] for _ in out_word]))
                ret.append(phrases.get(translated_out))
            return ret


with open('case1.txt') as fin:
    counter = 0
    for line in fin.readlines():
        sp = line.split(" | ")
        _words = [e.strip() for e in sp[0].split(" ")]
        _output = [e.strip() for e in sp[1].split(" ")]
        nums = case(_words, _output)
        for num in nums:
            if num in [1, 4, 7, 8]:
                counter += 1
    print(counter)
