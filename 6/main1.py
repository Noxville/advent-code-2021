with open('case1.txt') as fin:
    heights = sorted([int(e.strip()) for e in fin.readline().split(",")])
    best = None
    for idx, _ in enumerate(range(min(heights), 1 + max(heights))):
        v = sum([abs(h - _) for h in heights])
        best = min(best, v) if best is not None else v
    print(best)
