class Rule:
    def __init__(self, raw):
        sp = [_.split(",") for _ in raw.replace(" -> ", "|").split("|")]
        self.x1, self.y1, self.x2, self.y2 = int(sp[0][0]), int(sp[0][1]), int(sp[1][0]), int(sp[1][1])

    def __repr__(self):
        return f"{self.x1},{self.y1} - {self.x2},{self.y2}"

    def max_x(self):
        return self.x1 if self.x1 > self.x2 else self.x2

    def max_y(self):
        return self.y1 if self.y1 > self.y2 else self.y2

    def covers(self):
        delta_x = self.x1 - self.x2
        delta_y = self.y1 - self.y2
        if abs(delta_x) and abs(delta_y):
            smaller_x = min(self.x1, self.x2)
            dy = delta_y if (self.x2 == smaller_x) else -delta_y
            dydx = dy // abs(delta_x)
            starting_y = self.y1 if (self.x1 == smaller_x) else self.y2
            #print(f"Smaller x = {smaller_x} / dy = {dy}, dydx = {dydx}, starting y = {starting_y}")
            return [(_x, starting_y + (i*dydx)) for i, _x in enumerate(range(smaller_x, 1 + max(self.x1, self.x2)))]
        elif abs(delta_x):
            return [(_, self.y1) for _ in range(min(self.x1, self.x2), 1 + max(self.x1, self.x2))]
        elif abs(delta_y):
            return [(self.x1, _) for _ in range(min(self.y1, self.y2), 1 + max(self.y1, self.y2))]

with open('case1.txt') as fin:
    rules = [Rule(e.strip()) for e in fin.readlines()]

    X, Y = 1 + max([_.max_x() for _ in rules]), 1 + max([_.max_y() for _ in rules])

    grid = [[0 for i in range(X)] for j in range(Y)]
    for r in rules:
        for cell in r.covers():
            grid[cell[1]][cell[0]] += 1

    overlaps = 0
    for x in range(X):
        for y in range(Y):
            if grid[x][y] >= 2:
                overlaps += 1
    print(overlaps)

