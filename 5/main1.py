class Fish:
    def __init__(self, countdown, child):
        self.countdown = countdown
        self.child = child

    def next(self):
        self.countdown -= 1
        if self.countdown == -1:
            self.countdown = 6
            return Fish(2 + self.child, self.countdown)
        return None

    def __repr__(self):
        return str(self.countdown)

with open('case1.txt') as fin:
    fish = [Fish(int(e.strip()), 6) for e in fin.readline().split(",")]

    print(fish)
    for i in range(256):
        ng = [f.next() for f in fish]
        ng = [_ for _ in ng if _ is not None]
        fish.extend(ng)
        row = ",".join([str(_) for _ in fish])
        #print(f"Day {1 + i}: {row}")
        print(f"Day {1 + i}: {len(fish)}")


