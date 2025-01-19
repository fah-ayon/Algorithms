import math

f = open('input1.txt','r')
f1 =  open('output1.txt','w')
nodes,edges = [int(i) for i in f.readline().split()]
graph = [[] for i in range(nodes+1)]
for i in range(edges):
    u,v,w = [int(i) for i in f.readline().split()]
    graph[u].append((v,w))
source = int(f.readline())
#print(graph)
def dijkstra(graph,source):
    n = len(graph)
    distance = [float('inf')]*n
    distance[source] = 0
    visited = []
    while len(visited)<n:
        min_distance = float('inf')
        ver = -1
        for i in range(1,n):
            if i not in visited and distance[i]<min_distance:
                min_distance = distance[i]
                ver =i
        visited.append(ver)
        for v,w in graph[ver]:
            if distance[ver]+w < distance[v]:
                distance[v]= distance[ver]+w
            #print(distance)
    return distance

p = ''
distances = dijkstra(graph,source)
for f in distances[1:]:
    if f== float('inf'):
        p= p+str(-1)+' '
    else:
        p= p+str(f)+' '
f1.write(p)
f1.close()