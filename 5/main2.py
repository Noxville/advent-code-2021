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

def convert_problem_sol(s):
    counter = {}
    for _ in map(int, s.split(",")):
        counter[_] = 1 + counter.get(_, 0)
    print(counter)

#convert_problem_sol("6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8")
# {6: 5, 0: 3, 4: 2, 5: 1, 1: 5, 2: 3, 3: 2, 7: 1, 8: 4}
# {6: 5, 0: 3, 4: 2, 5: 1, 1: 5, 2: 3, 3: 2, 7: 1, 8: 4}

