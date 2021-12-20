class Algo:
    def __init__(self, s):
        self.bitmap = dict()
        for idx, c in enumerate(s):
            self.bitmap[idx] = int(c == '#')


class Img:
    def __init__(self, d, alg):
        self.d = d
        self.alg = alg
        self.orig = (len(d[0]), len(d))
        self.epoch = 0

    def pr(self, rep):
        out = ''
        for r in self.d:
            out += ("".join(map(str, r))) + '\n'
        return out.replace("0", ".").replace("1", "#") if rep else out

    def __repr__(self):
        return self.pr(True)

    def box_at(self, x, y):
        out = ''
        for (i, j) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y), (x + 1, y), (x - 1, y + 1),
                       (x, y + 1), (x + 1, y + 1)]:
            if 0 <= i < len(self.d[0]) and 0 <= j < len(self.d):
                out += str(self.d[j][i])
            else:
                out += '0'
        return self.alg.bitmap[int(out, 2)]

    def enhance(self):
        nw = []
        for i in range(-1, 1 + len(self.d[0])):
            li = []
            for j in range(-1, 1 + len(self.d)):
                li.append(self.box_at(j, i))
            nw.append(li)
        self.d = nw
        self.epoch += 1

    def pad(self):
        nw = []
        for i in range(-1, 1 + len(self.d[0])):
            li = []
            for j in range(-1, 1 + len(self.d)):
                if 0 <= i < len(self.d[0]) and 0 <= j < len(self.d):
                    li.append(self.d[i][j])
                else:
                    li.append(0)
            nw.append(li)
        self.d = nw

    def trim(self):
        nw = []
        for i in range(len(self.d[0])):
            if i in [0, len(self.d[0])-1]:
                continue
            li = []
            for j in range(len(self.d)):
                if j in [0, len(self.d) - 1]:
                    continue
                li.append(self.d[i][j])
            nw.append(li)
        self.d = nw

    def lit(self):
        cnt = 0
        for y, r in enumerate(self.d):
            for x, c in enumerate(r):
                        cnt += c
        return cnt


with open('case1.txt') as fin:
    algo = Algo(fin.readline().strip())
    _ = fin.readline()
    image = Img([[int(_ == '#') for _ in e.strip()] for e in fin.readlines()], algo)

    print("raw")
    print(image)
    for _ in range(150):
        # print(f"pad #{1+_}")
        image.pad()
        # print(image)

    for _ in range(50):
        print(f"enhance #{1+_}")
        image.enhance()
        # print(image)

    for _ in range(85):
        image.trim()
    # print(image)
    print(f"lit: {image.lit()}")