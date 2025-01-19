f = open('input1b.txt', 'r')
f1 = open('output1b.txt', 'w')
nodes, edges = [int(i) for i in f.readline().split()]
graph = []
for i in range(nodes+1):
    graph.append([])
for i in range(nodes+1):
    u,v,w = [int(i) for i in f.readline().split()]
    graph[u].append((v,w))
for u,row in enumerate(graph):
    f1.write(f'{u}: {row}\n'.replace('[',' ').replace(']',' '))   
f1.close()


