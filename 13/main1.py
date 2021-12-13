with open('case1.txt') as fin:
    ls = [e.strip() for e in fin.readlines()]
    dots = set([tuple(map(int, _.split(","))) for _ in ls if _.count(',')])
    instructions = [_.split(' ')[-1] for _ in ls if _.count('fold')]
    for idx, fold in enumerate(instructions):
        val = int(fold.split("=")[-1])
        dots = {(x, y) if y < val else (x, 2 * val - y) for (x, y) in dots} \
            if 'y' == fold[0] else \
            {(x, y) if x < val else (2 * val - x, y) for (x, y) in dots}

        if idx == 0: print(len(dots))  # after first fold
    for j in range(1 + max([_[1] for _ in dots])):
        print("".join(['#' if (i, j) in dots else ' ' for i in range(1 + max([_[0] for _ in dots]))]))
