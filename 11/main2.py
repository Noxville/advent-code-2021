def neigh(x, y, N):
    ret = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if not (dx == 0 and dy == 0):
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    ret.append((x + dx, y + dy))
    return ret


def pg(grid):
    for l in grid:
        print("".join(map(str, l)))
    print("-" * 20)


with open('case1.txt') as fin:
# with open('tiny.in') as fin:

    result = []
    for line in fin.readlines():
        result.append([int(_) for _ in line.strip()])
    N = len(result[0])
    pg(result)

    step = 0
    while True:
        flashes = 0
        # step 1
        flag = True
        first = True
        while flag:
            flag = False
            # phase 1
            if first:
                for i in range(N):
                    for j in range(N):
                        result[j][i] += 1
                first = False

            # phase 2
            for i in range(N):
                for j in range(N):
                    if result[j][i] is not None and result[j][i] > 9:
                        flag = True
                        flashes += 1
                        result[j][i] = None
                        for n in neigh(j, i, N):
                            if result[n[0]][n[1]] is not None:
                                result[n[0]][n[1]] += 1

            if not flag:
                for i in range(N):
                    for j in range(N):
                        if result[j][i] is None:
                            result[j][i] = 0
        if flashes == N * N:
            print(1 + step)
            break
        step += 1