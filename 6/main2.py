with open('case1.txt') as fin:
    heights = sorted([int(e.strip()) for e in fin.readline().split(",")])
    best_pos, best_val = None, None
    for pos in range(min(heights), 1 + max(heights)):
        v = sum([(abs(h - pos) * (1 + abs(h - pos))) // 2 for h in heights])
        if best_pos is None or v < best_val:
            best_pos, best_val = pos, v
    print(best_val)
