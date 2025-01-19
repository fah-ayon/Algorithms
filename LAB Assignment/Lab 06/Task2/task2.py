f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')
nodes,edges = [int(i) for i in f.readline().split()]
graph = [[] for i in range(nodes+1)]

for i in range(edges):
    u,v,w = [int(i) for i in f.readline().split()]
    graph[u].append((v,w))
#print(graph)
alice,bob = [int(i) for i in f.readline().split()]

def dijkstra(graph,source):
    n = len(graph)
    distance = [float('inf')]*n
    distance[source]= 0
    visited = []
    while len(visited)<n:
        min_distance = float('inf')
        ver = -1
        for i in range(1,n):
            if i not in visited and distance[i]<min_distance:
                min_distance = distance[i]
                ver = i
        visited.append(ver)
        for v,w in graph[ver]:
            if distance[ver]+w<distance[v]:
                distance[v]= distance[ver]+w
    return distance
alice_pos = dijkstra(graph, alice) 
bob_pos = dijkstra(graph, bob)

# print(alice_pos)
# print(bob_pos)

min_node = []
for u in range(nodes+1):
    if alice_pos[u] != float('inf') and bob_pos[u]!= float('inf'):
        if alice_pos[u]>bob_pos[u]:
            min_node.append(alice_pos[u])
        else:
            min_node.append(bob_pos[u])
    else:
        min_node.append(float('inf'))

min = float('inf')
node = None
for i in range(len(min_node)):
    if min_node[i]<min:
        min = min_node[i]
        node=i
if node is None:
    f1.write('Impossible')
else:
    f1.write(f'Time: {min}\nNode: {node}')