f= open('input1b.txt','r')
f1 = open('output1b.txt', 'w')
n,m = [int(i) for i in f.readline().split()]
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a,b = [int(i) for i in f.readline().split()]
    graph[a].append(b)
    indegree[b] +=1

def bfs_toposort(graph,indegree):
    q = []
    for i in range(1, len(indegree)):
        if indegree[i]==0:
            q.append(i)
    res=[]
    while q:
        node = q.pop(0)
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -=1
            if indegree[neighbor] ==0:
                q.append(neighbor)
    if len(res) == len(indegree)-1:
        return res
    else:
        return None

res = bfs_toposort(graph,indegree)
if res is None:
    f1.write('IMPOSSIBLE')
else:
    f1.write(' '.join(str(j) for j in res) + "\n")

f.close()
f1.close()
