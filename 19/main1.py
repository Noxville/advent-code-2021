def rotate(val, r):
    x, y, z = val
    return {
        0: (x, y, z),
        1: (x, z, y),
        2: (y, x, z),
        3: (y, z, x),
        4: (z, x, y),
        5: (z, y, x),
        -1: (),
        -2: (),
        -3: (x, y, z),
        -4: (),
        -5: (),
    }[r]


def flip(val, f):
    x, y, z = val
    return {
        0: (x, y, z),
        1: (x, y, -z),
        2: (x, -y, z),
        3: (x, -y, -z),
        4: (-x, y, z),
        5: (-x, y, -z),
        6: (-x, -y, z),
        7: (-x, -y, -z),
    }[f]


class Scanner:
    def __init__(self, num):
        self.num = num
        self.beacons = list()
        self.pos = (None, None, None)  # pos of this scanner
        self.solved = False  # have we figured out this scanner
        self.ori = None  # base orientation of the scanner

    def solve(self, xyz, ori):
        self.pos = xyz
        self.ori = ori
        self.solved = True

    def add_beacon(self, x, y, z):
        self.beacons.append((x, y, z))

    def orientated_beacons(self):
        ro, fl = self.ori
        return [
            addt(rotate(flip(b, fl), ro), self.pos)
            for b in self.beacons]

    def permute(self):
        confs = {}
        for ro in range(6):
            for fl in range(8):
                confs[(ro, fl)] = [flip(rotate(b, ro), fl) for b in self.beacons]
        return confs

    def __repr__(self):
        return f"@{self.pos} // beacons: {self.beacons}"


def brute(solved, unsolved):
    lookup = set()
    for known_b in solved.beacons:
        lookup.add(known_b)

    for ori, unknown_beacons in unsolved.permute().items():
        for known_b in solved.beacons:
            for unknown_b in unknown_beacons:
                good = 1  # we assume the fixed beacon is "good"
                offset = subt(known_b, unknown_b)
                for other_b in [_ for _ in unknown_beacons if _ != unknown_b]:
                    if addt(other_b, offset) in lookup:
                        good += 1
                        if good >= 12:
                            new_pos = addt(solved.pos, rotate(flip(offset, solved.ori[1]), solved.ori[0]))
                            print(
                                f"Scanner {unsolved.num}. Relative to {solved.pos}, we are with offset {offset} => {new_pos}, with orientation {solved.ori}")
                            unsolved.solve(new_pos, ori)
                            return True
    return False


def subt(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def addt(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def dist(i, j):
    return abs(i.pos[0] - j.pos[0]) + abs(i.pos[1] - j.pos[1]) + abs(i.pos[2] - j.pos[2])

def solve_all(ss):
    for _ in range(len(ss) - 1):
        solve_single()


def solve_single():
    tried = set()  # We never get more info, so why retry?
    for s1 in [_ for _ in scanners if _.solved]:
        for s2 in [_ for _ in scanners if not _.solved]:
            if (s1, s2) not in tried:
                tried.add((s1, s2))
                if brute(s1, s2):
                    return


with open('test1.in') as fin:
    inp = [e.strip() for e in fin.readlines()]
    scanners = []
    scanner = None
    num = 0
    for line in inp:
        if line.startswith("---"):
            scanner = Scanner(num)
        elif line == '':
            scanners.append(scanner)
            num += 1
        else:
            scanner.add_beacon(*map(int, line.split(",")))
    scanners.append(scanner)
    scanners[0].solve((0, 0, 0), (0, 0))
    solve_all(scanners)

    all_beacs = set()
    for s in scanners:
        print(f"Scanner {s.num} @ {s.pos} with ori {s.ori}")
        for b in s.orientated_beacons():
            all_beacs.add(b)
    print(len(all_beacs))

    big = 0
    for s1 in scanners:
        for s2 in scanners:
            big = max(big, dist(s1, s2))
    print(big)
