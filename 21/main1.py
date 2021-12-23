class Player:
    def __init__(self, idx, pos):
        self.idx = idx
        self.pos = pos
        self.score = 0

    def move(self, n):
        self.pos += n
        self.pos = 1 + ((self.pos - 1) % 10)
        self.score += self.pos
        print(f"Player {self.idx} is now at {self.pos} with score {self.score}")


class Dice:
    def __init__(self):
        self.val = 1
        self.count = 0

    def roll(self):
        ret = 0 + self.val
        self.val += 1
        self.count += 1
        if self.val == 101:
            self.val = 1
        return ret

    def rolln(self, n):
        tot = 0
        for _ in range(n):
            tot += self.roll()
        return tot


with open('case1.txt') as fin:
    starts = list(map(int, [e.strip().split(" ")[-1] for e in fin.readlines()]))

    p1, p2 = Player(1, starts[0]), Player(2, starts[1])
    dice = Dice()

    active = p1
    while True:
        move = dice.rolln(3)
        print(f"Dice rolled sum of {move}")
        active.move(move)
        if active.score >= 1000:
            break
        active = p2 if active.idx == 1 else p1

    print(min(p1.score, p2.score) * dice.count)
