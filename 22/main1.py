class Op:
    def __init__(self, s):
        sp = s.replace(" ", ",").replace("..", ",").replace("x=","").replace("y=","").replace("z=","").split(',')
        self.do = sp[0]
        self.x = (int(sp[1]), int(sp[2]))
        self.y = (int(sp[3]), int(sp[4]))
        self.z = (int(sp[5]), int(sp[6]))

    def __repr__(self):
        return f"{self.do}, x={self.x}, y={self.y}, z={self.z}"

with open('case1.txt') as fin:
    ops = [Op(e.strip()) for e in fin.readlines()]

    n = 101
    cube = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]

    for op in ops:
        print(op)
        for x in range(max(op.x[0], -50), 1 + min(op.x[1], 50)):
            if not -50 <= x <= 50:
                continue
            for y in range(max(op.y[0], -50), 1 + min(op.y[1], 50)):
                if not -50 <= y <= 50:
                    continue
                for z in range(max(op.z[0], -50), 1 + min(op.z[1], 50)):
                    if not -50 <= z <= 50:
                        continue

                    cube[z+50][y+50][x+50] = 1 if op.do == 'on' else 0

    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s += cube[k-50][j-50][i-50]
    print(s)