class Cube:
    def __init__(self, s):
        if type(s) == str:
            sp = s.replace(" ", ",").replace("..", ",").replace("x=", "").replace("y=", "").replace("z=", "").split(',')
            self.do = sp[0]
            self.x = (int(sp[1]), int(sp[2]))
            self.y = (int(sp[3]), int(sp[4]))
            self.z = (int(sp[5]), int(sp[6]))
        else:
            self.do = 'who cares'
            self.x = (s[0], s[1])
            self.y = (s[2], s[3])
            self.z = (s[4], s[5])

    def __repr__(self):
        return f"{self.do}, x={self.x}, y={self.y}, z={self.z}"

    def intersects(self, another_cube):
        if another_cube.x[0] > self.x[1] or another_cube.y[0] > self.y[1]:
            return False
        if another_cube.z[0] > self.z[1] or another_cube.x[1] < self.x[0]:
            return False
        if another_cube.y[1] < self.y[0] or another_cube.z[1] < self.z[0]:
            return False
        return True

    def shard(self, oc):
        return [_ for _ in [
            Cube((max(self.x[0], oc.x[0]), min(self.x[1], oc.x[1]), max(self.y[0], oc.y[0]), min(self.y[1], oc.y[1]), oc.z[1] + 1, self.z[1])),
            Cube((max(self.x[0], oc.x[0]), min(self.x[1], oc.x[1]), max(self.y[0], oc.y[0]), min(self.y[1], oc.y[1]), self.z[0], oc.z[0] - 1)),
            Cube((max(self.x[0], oc.x[0]), min(self.x[1], oc.x[1]), oc.y[1] + 1, self.y[1], self.z[0], self.z[1])),
            Cube((oc.x[1] + 1, self.x[1], self.y[0], self.y[1], self.z[0], self.z[1])),
            Cube((self.x[0], oc.x[0] - 1, self.y[0], self.y[1], self.z[0], self.z[1])),
            Cube((max(self.x[0], oc.x[0]), min(self.x[1], oc.x[1]), self.y[0], oc.y[0] - 1, self.z[0], self.z[1]))
        ] if (_.x[0] <= _.x[1]) and (_.y[0] <= _.y[1]) and (_.z[0] <= _.z[1])
                ]

    def vol(self):
        return (1 + self.x[1] - self.x[0]) * (1 + self.y[1] - self.y[0]) * (1 + self.z[1] - self.z[0])


with open('case1.txt') as fin:
    ops = [Cube(e.strip()) for e in fin.readlines()]
    tracked_cubes = []

    for op in ops:
        next_cubes = []

        if op.do == 'on':
            next_cubes.append(op)
        for c in tracked_cubes:
            if op.intersects(c):
                next_cubes.extend(c.shard(op))
            else:
                next_cubes.append(c)
        tracked_cubes = next_cubes

total = 0
for c in tracked_cubes:
    total += c.vol()
print(total)
