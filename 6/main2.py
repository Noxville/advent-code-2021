with open('case1.txt') as fin:
    fish = [int(e.strip()) for e in fin.readline().split(",")]
    fc = {}
    for f in fish:
        fc[f] = 1 + fc.get(f, 0)

    print(fc)
    for i in range(256):
        ng = {}
        spawn = 0
        for left, c in fc.items():
            if left == 0:
                spawn = c
                ng[6] = c
            else:
                ng[left - 1] = ng.get(left - 1, 0) + c
        ng[8] = spawn
        fc = ng
        print(f"Day {1 + i}: {sum(fc.values())}")
