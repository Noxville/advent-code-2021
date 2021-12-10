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
    return [ops[_] for _ in stack[::-1]]


with open('case1.txt') as fin:
    penalties = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in fin.readlines():
        cur_score = 0
        s = solve(line)
        if type(s) != int:
            for c in s:
                cur_score = (cur_score  * 5 ) + penalties[c]
            scores.append(cur_score)
    print(sorted(scores)[len(scores)//2])