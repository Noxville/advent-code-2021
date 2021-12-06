with open('case1.txt') as fin:
    ls = [int(e.strip()) for e in fin.readlines()]
    prev = None
    inc = 0
    for _ in ls:
        if prev is None:
            prev = _
        else:
            if _ > prev:
                inc += 1
        prev = _
    print(inc)
