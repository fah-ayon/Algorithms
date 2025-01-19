f = open('input3.txt', 'r')
f1 = open('output3.txt', 'w')

nodes,edges = [int(i) for i in f.readline().split()]
graph = [[] for i in range(nodes+1)]
for i in range(edges):
    u,v,w = [int(i) for i in f.readline().split()]
    graph[u].append((v,w))
destination = nodes

def dijkstra(graph,nodes):
    n = len(graph)
    distance= [float('inf')]*n
    distance[1]= 0
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
            if v not in visited:
                new_dist = max(distance[ver],w)
                if new_dist<distance[v]:
                    distance[v]= new_dist
    if distance[nodes]== float('inf'):
        f1.write('Impossible')
    else:
        f1.write(str(distance[nodes]))      
dijkstra(graph,nodes)