from math import inf
f = open('input5.txt', 'r')
f1 = open('output5.txt', 'w')
n,m,d = [int(i) for i in f.readline().split()]
s = 1
graph = [list() for i in range(n)]
for i in range(m):
    u,v = [int(i) for i in f.readline().split()]
    graph[u-1].append(v)
    graph[v-1].append(u)
time= [inf]*n
time[s-1]=0 
path = [list() for i in range(n)]
q = [s]
while q:
    u = q[0]
    q= q[1:]
    for v in graph[u-1]:
        if time[v-1]==inf:
            q.append(v)
            time[v-1]=time[u-1]+1
            path[v-1] = [*path[u-1], u]
path[d-1].append(d)
minTime = time[d-1]

f1.write(f"Time: {minTime}\n")
f1.write(f"Shortest Path: {' '.join(list(map(str, path[d-1])))}")
