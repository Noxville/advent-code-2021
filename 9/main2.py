def basin_size(grid, basin):
    todo, seen = [basin], {}
    while todo:  # flood fill each basin, BFS
        x, y = todo.pop()
        seen[(x, y)] = True

        add = []
        if x - 1 >= 0 and result[x - 1][y] != 9:
            add.append((x - 1, y))
        if x + 1 < len(result) and result[x + 1][y] != 9:
            add.append((x + 1, y))
        if y - 1 >= 0 and result[x][y - 1] != 9:
            add.append((x, y - 1))
        if y + 1 < len(grid[0]) and result[x][y + 1] != 9:
            add.append((x, y + 1))

        todo.extend([_ for _ in set(add) if _ not in seen])

    return len(seen)


with open('case1.txt') as fin:
    result = []
    for line in fin.readlines():
        result.append([int(_) for _ in line.strip()])

    basins = []
    for i, _ in enumerate(result):
        for j, val in enumerate(_):
            surround = []
            if i - 1 >= 0: surround.append(result[i - 1][j])
            if i + 1 < len(result): surround.append(result[i + 1][j])
            if j - 1 >= 0: surround.append(result[i][j - 1])
            if j + 1 < len(_): surround.append(result[i][j + 1])

            if val < min(surround):
                basins.append((i, j))

    sizes = sorted([basin_size(result, basin) for basin in basins])
    print(f"{sizes[-1] * sizes[-2] * sizes[-3]}")
