from collections import Counter
with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    start = ls[0]

    swaps = {}
    for swap in ls[2:]:
        swaps[swap.split("->")[0].strip()] = swap.split("->")[1].strip()

    count = Counter()
    for idx, (c1, c2) in enumerate(zip(start, start[1:])):
        count[c1 + c2] += 1

    for _ in range(40):
        old_count = count
        count = Counter()
        for pair, num in old_count.items():
            count[swaps[pair] + pair[1]] += num
            count[pair[0] + swaps[pair]] += num

    letters = Counter()
    for pair, num in count.items():
        letters[pair[1]] += num
    letters[start[0]] += 1  # fucksake

    std = sorted(letters.items(), key=lambda x: x[1])
    print(std[-1][1] - std[0][1])