def reduce(ls, equal):
    n = len(ls[0])
    for i in range(n):
        one, zero = 0, 0
        for v in ls:
            if v[i] == '1':
                one += 1
            else:
                zero += 1
        sig = ('1' if one >= zero else '0') if equal else ('1' if one > zero else '0')
        ls = [_ for _ in ls if _[i] == sig]
        if len(ls) == 1:
            return ls[0]
    return ls[0]


with open('case1.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
    ox2 = reduce(list(set(lines)), True)
    co2 = reduce(list(set(lines)), False)

    print(int(ox2, 2) * int(co2, 2))