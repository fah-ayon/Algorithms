f = open('input4.txt', 'r')
f1 = open('output4.txt', 'w')
nodes, edges = [int(i) for i in f.readline().split()]
graph = []
for i in range(nodes+1):
    graph.append([])
for i in range(edges):
    u, v = [int(i) for i in f.readline().split()]
    graph[u].append(v)

def DFS(G, u, explored, re_explored):
    explored[u] = True
    re_explored[u] = True
    for v in G[u]:
        if not explored[v]:
            if DFS(G, v, explored, re_explored):
                return True
        elif re_explored[v]:
            return True
    re_explored[u] = False
    return False

def cycle(G, nodes):
    explored = [False] * (nodes + 1)
    re_explored = [False] * (nodes + 1)
    for i in range(1, nodes + 1):
        if not explored[i]:
            if DFS(G, i, explored, re_explored):
                return True
    return False

if cycle(graph, nodes):
    f1.write('YES')
else:
    f1.write('NO')