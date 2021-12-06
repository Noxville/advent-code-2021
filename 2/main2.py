with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    loc_aim = [0, 0, 0]

    for c in ls:
        sp = c.split(" ")
        mag = int(sp[1])
        if sp[0] == 'forward':
            loc_aim[0] += mag
            loc_aim[1] += loc_aim[2] * mag
        elif sp[0] == "up":
            loc_aim[2] -= mag
        elif sp[0] == 'down':
            loc_aim[2] += mag

    print(loc_aim[0] * loc_aim[1])
