with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    loc = [0, 0]

    for c in ls:
        sp = c.split(" ")
        mag = int(sp[1])
        if sp[0] == 'forward':
            loc[0] += mag
        elif sp[0] == "up":
            loc[1] -= mag
        elif sp[0] == 'down':
            loc[1] += mag

    print(loc[0] * loc[1])
