import sys


class Grid:
    def __init__(self, lines):
        self.data = [[int(_) for _ in line.replace("  ", " ").split(" ")] for line in lines]
        self.alive = True

    def won(self):
        for r in range(5):
            if max(self.data[r]) == -1:
                return True
        for c in range(5):
            if max([_[c] for _ in self.data]) == -1:
                return True
        return False

    def remove(self, v):
        for r in range(5):
            for c in range(5):
                if self.data[r][c] == v:
                    self.data[r][c] = -1

    def unmarked(self):
        tot = 0
        for r in range(5):
            for c in range(5):
                tot += max(0, self.data[r][c])
        return tot


# with open('test1.in') as fin:
with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    nums = map(int, ls[0].split(","))
    grids = [Grid(ls[2 + (6 * i): (6 * i) + 7]) for i in range((len(ls) - 1) // 6)]

    for n in nums:
        for idx, g in enumerate(grids):
            if g.alive:
                g.remove(n)
                if g.won():
                    g.alive = False
                    print(f"killed grid #{idx}")
                    print(f"nums: {n}")
                    print(f"unmarked: {g.unmarked()}")
                    print(g.unmarked() * n)
                    print(f"grids # left: {len([_ for _ in grids if _.alive])}")
                    print("")


