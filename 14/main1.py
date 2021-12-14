with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    start = ls[0]

    swaps = {}
    for swap in ls[2:]:
        swaps[swap.split("->")[0].strip()] = swap.split("->")[1].strip()

    for _ in range(10):
        nxt = start[0]
        for idx, (c1, c2) in enumerate(zip(start, start[1:])):
            nxt += swaps[c1 + c2] + c2
        start = nxt

    cc = {}
    for c in start:
        cc[c] = 1 + cc.get(c, 0)
    std = sorted(cc.items(), key=lambda x: x[1])
    print(std[-1][1] - std[0][1])
