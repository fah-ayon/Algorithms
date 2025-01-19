f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')

nodes , edges = [int(i) for i in f.readline().split()]
graph = []
for i in range(nodes):
    graph.append([])
for i in range(edges):
    u,v = [int(i) for i in f.readline().split()]
    graph[u-1].append(v)
    graph[v-1].append(u)

e =1
explore = [0]*nodes
q = []
explore[e-1] = 1
q.append(e)
while q:
    u = q[0]
    f1.write(f'{str(u)} ')
    q = q[1:]
    for v in graph[u-1]:
        if explore[v-1]==0:
            explore[v-1]= 1
            q.append(v)
            