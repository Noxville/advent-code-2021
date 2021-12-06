with open('te') as fin:
    ls = [int(e.strip()) for e in fin.readlines()]
    prev = None
    inc = 0
    for idx in range(0, len(ls) - 2):
        _ = sum(ls[idx:idx + 3])
        if prev is None:
            prev = _
        else:
            if _ > prev:
                inc += 1
        prev = _
    print(inc)
