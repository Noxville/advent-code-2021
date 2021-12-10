def solve(l):
    ops = {'[': ']', '(': ')', '{': '}', '<': '>'}
    vals = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    for c in l.strip():
        if c in ops.keys():
            stack.append(c)
        else:
            p = stack.pop()
            if ops[p] != c:
                return vals[c]
    return 0


with open('case1.txt') as fin:
    total = 0
    for line in fin.readlines():
        total += solve(line)
    print(total)
