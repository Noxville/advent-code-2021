import heapq


def rotate(start, shift):
    for _ in range(shift):
        start += 1
        if start == 10:
            start = 1
    return start


with open('case1.txt') as fin:
    arr_simp = [[int(c) for c in e.strip()] for e in fin.readlines()]
    count_y, count_x = len(arr_simp), len(arr_simp[0])

    arr = [[-1]*(5 * count_x) for _ in range(5*count_y)]
    for sy in range(5):
        for sx in range(5):
            shift = sy + sx
            for ny in range(count_y):
                for nx in range(count_x):
                    arr[sy * count_y + ny][sx * count_x + nx] = rotate(arr_simp[ny][nx], sy + sx)

    mY, mX = len(arr), len(arr[0])
    goal = (mX - 1, mY - 1)
    pq = [(0, (0, 0))]
    heapq.heapify(pq)

    while pq:
        risk, (x, y) = heapq.heappop(pq)
        if goal == (x, y):
            print(risk)
            break
        for _x, _y in [(x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)]:
            if 0 <= _x < mX and 0 <= _y < mY and arr[_y][_x] is not None:
                heapq.heappush(pq, (risk + arr[_y][_x], (_x, _y)))
                arr[_y][_x] = None
