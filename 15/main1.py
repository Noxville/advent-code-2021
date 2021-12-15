import heapq

with open('case1.txt') as fin:
    arr = [[int(c) for c in e.strip()] for e in fin.readlines()]

    distances, unseen, seen = {}, {}, {}
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