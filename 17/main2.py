def solve(tx, ty):
    print(f"tx={tx} ty={ty}")

    best, bx, by = - (10**6), None, None
    vx = valid_x(tx)
    vy = valid_y(ty)
    good = 0
    print(f"Brute force perms: {len(vx) * len(vy)}")
    for dx in vx:
        for dy in vy:
            max_y = attempt(dx, dy, tx, ty)
            if max_y is not None:
                good += 1
    print(f"good {good}")


def valid_x(xrnge):
    valid = set()
    for shift in range(-1000, 1000):
        x, dx, steps = 0, 0 + shift, 0
        while True:
            x += dx
            if xrnge[0] <= x <= xrnge[1]:
                valid.add(shift)
            if dx == 0:
                break
            dx = max(0, dx - 1) if dx >= 0 else min(0, dx + 1)
            steps += 1
    return valid


def valid_y(yrnge):
    valid = set()
    for shift in range(-1000, 1000):
        y, dy, steps = 0, 0 + shift, 0
        while True:
            y += dy
            if yrnge[0] <= y <= yrnge[1]:
                # print(f"with shift={shift}, after {steps} steps we are at {y}")
                valid.add(shift)
            if y < yrnge[0]:
                break
            dy -= 1
            steps += 1
    return valid


def attempt(dx, dy, tx, ty):
    x, y, s = 0, 0, 0
    prev = []
    inside = False
    while True:
        s += 1
        x += dx
        y += dy
        prev.append((x, y))
        dx = max(0, dx - 1) if dx >= 0 else min(0, dx + 1)
        dy -= 1
        if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
            inside = True
        if y <= ty[0]:
            break
    if inside:
        return max([_[1] for _ in prev])
    else:
        return None


with open('case1.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
    for lin in lines:
        sp = lin.replace("target area: ", "").replace(", ", ",").replace("x=", "").replace("y=", "").split(",")
        solve(list(map(int, sp[0].split(".."))), list(map(int, sp[1].split(".."))))
