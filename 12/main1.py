class Graph:
    def __init__(self):
        self.adj = {}
        self.big = set()
        self.small = set()

    def add_edge(self, fr, to):
        if fr not in ['start', 'end']:
            if fr == fr.lower():
                self.small.add(fr)
            else:
                self.big.add(fr)

        if to not in ['start', 'end']:
            if to == to.lower():
                self.small.add(to)
            else:
                self.big.add(to)

        if fr not in self.adj:
            self.adj[fr] = [to]
        else:
            self.adj[fr].append(to)

        if to not in self.adj:
            self.adj[to] = [fr]
        else:
            self.adj[to].append(fr)

    def neighbours(self, vert):
        return self.adj[vert]

g = Graph()
with open('case1.txt') as fin:
    edges = [e.strip().split("-") for e in fin.readlines()]
    for e in edges:
        g.add_edge(e[0], e[1])


def bfs(_g, start, end, path):
    path = path + [start]
    if end == start:
        return [path]
    paths = []
    for neigh in _g.neighbours(start):
        if neigh in _g.big or neigh not in path:
            joining_paths = bfs(_g, neigh, end, path)
            for join in joining_paths:
                paths.append(join)
    return paths


all_paths = bfs(g, 'start', 'end', [])
print(len(all_paths))
