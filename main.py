from random import uniform
import heapq

__author__ = 'Devon Chen'

def genRandomGraph(n, p):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if uniform(0, 1) < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def fillColor(g):
    def findColor(colors):
        c = 1
        while c in set(filter(lambda c: c != 0, colors)):
            c += 1
        return c
    color_set = [0] * len(g)
    h = [(-len(g[v]), v) for v in range(len(g))]
    heapq.heapify(h)
    while len(h) != 0:
        p, v = heapq.heappop(h)
        c = findColor([color_set[neighbor] for neighbor in g[v]])
        color_set[v] = c
    return set(color_set)


if __name__ == '__main__':
    g = genRandomGraph(1000, 0.02)
    s = fillColor(g)
    print(f"Number of colors: {len(s)}")
