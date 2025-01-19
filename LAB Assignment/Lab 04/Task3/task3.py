f = open('input3.txt', 'r')
f1 = open('output3.txt', 'w')
nodes, edges = [int(i) for i in f.readline().split()]
graph = []
for i in range(nodes+1):
    graph.append([])
for i in range(edges):
    u,v = [int(i) for i in f.readline().split()]
    graph[u].append(v)
    graph[v].append(u)
e = 1
explore = [0]*(nodes+1)
def DFS(G,u):
    explore[u] = 1
    f1.write(f'{str(u)} ')
    for v in graph[u]:
        if explore[v] == 0:
            DFS(G,v)
DFS(graph, e)