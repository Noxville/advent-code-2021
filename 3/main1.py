with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]

    ones = {}
    zero = {}

    n = len(ls[0])

    for line in ls:
        for idx, c in enumerate(line):
            if c == '0':
                zero[idx] = 1 + zero.get(idx, 0)
            else:
                ones[idx] = 1 + ones.get(idx, 0)

    gamma = ''
    epsilon = ''

    for i in range(n):
        if ones.get(i, 0) > zero.get(i, 0):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(f"eps: {gamma}: {int(gamma, 2)}")
    print(f"eps: {epsilon}: {int(epsilon, 2)}")
    print(int(gamma, 2) * int(epsilon, 2))