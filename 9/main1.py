with open('case1.txt') as fin:
    result = []
    for line in fin.readlines():
        result.append([int(_) for _ in line.strip()])

    risk = 0
    for i, _ in enumerate(result):
        for j, val in enumerate(_):
            surround = []
            if i - 1 >= 0: surround.append(result[i - 1][j])
            if i + 1 < len(result): surround.append(result[i + 1][j])
            if j - 1 >= 0: surround.append(result[i][j - 1])
            if j + 1 < len(_): surround.append(result[i][j + 1])

            if val < min(surround):
                print(f"{i}, {j}, {val}")
                risk += 1 + val
    print(risk)
