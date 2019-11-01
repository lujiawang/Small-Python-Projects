import math
from collections import deque

graph = {0: {1, 2},
     1: {0, 3},
     2: {0, 3},
     3: {1, 2}}

h = {0: {1},
     1: {0},
     2: {3},
     3:{1}}

x = {0: [1, 2, 3],
     1: [0, 2, 4],
     2: [0, 1, 3],
     3: [0, 2, 4],
     4: [1, 3],
     5: [6],
     6: [5],
     7: []}

y = {0: {1, 2},
     1: {0, 3},
     2: {0, 3},
     3: {1, 2}}

l = {0: {1},
     1: {0}}

m = {0: {1, 2},
     1: {0, 3},
     2: {0, 3},
     3: {1, 2},
     4: {5, 6},
     5: {4, 6},
     6: {4, 5}}

z = {0: {1, 2},
     1: {0, 3},
     2: {0, 3},
     3: {1, 2},
     4: {5},
     5: {4}
     }


# g is a dictionary representation of an undirected graph

# The function should work by running BFS on the graph, alternately
# coloring vertices in each layer 0 or 1. If two adjacent vertices
# are ever colored the same color, the function returns False, else
# it returns True.

# The vertices of the graph are assumed to be labeled 0, 1, 2, 3, ...
# The graph is assumed to have at least one vertex

# Note: The graph might not be connected


def is_bipartite(g):
    color = {}
    for k in g.keys():
        color[k] = math.inf
    index = 0
    while math.inf in color:
        color[index] = 0

        q = deque()
        q.append(color[index])

        while q:  # while q is not empty
            u = q.popleft()  # remove from the front of the queue
            for v in g[u]:
                if color[v] == math.inf:
                    color[v] = color[u]-1
                elif color[v] != color[u]-1:
                    return False
        temp = False
        for k in color:
            if k == math.inf and not temp:
                index = k
                temp = True
    return True





def bfs2(g, s):
    color = {}
    res = True
    for k in g.keys():
        color[k] = math.inf

    color[s] = 0

    q = deque()
    q.append(s)

    while q and res:
        u = q.popleft()
        for v in g[u]:
            if color[v] == math.inf:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                res = False
                break

    return res, color


def bipartite(g):
    color = {}
    res = True
    for k in g.keys():
        color[k] = math.inf

    for i in color:
        if color[i] == math.inf:
            res, color = bfs2(g, i)
            if res == False:
                break

    return res


print(bipartite(m))





