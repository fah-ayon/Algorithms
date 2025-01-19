f = open('input6.txt', 'r')
f1 = open('output6.txt','w')
r,h = [int(i) for i in f.readline().split()]
graph = [f.readline() for i in range(r)]

def adj(i,j):
    return filter(lambda tup:tup[0]>=0 and tup[0]<r and tup[1]>=0 and tup[1]<h and graph[tup[0]][tup[1]]!="#", [(i+1, j), (i, j+1), (i-1, j), (i, j-1)])
matrix = [[0]*h for i in range(r)]
diamond = 0
def dfs(G, i, j):
    global diamond
    matrix[i][j] = 1
    if graph[i][j] == "D":
        diamond+=1
    for vIdx in adj(i, j):
        if matrix[vIdx[0]][vIdx[1]]==0:
            dfs(G, vIdx[0], vIdx[1])

max_diamond = 0
for i in range(r):
    for j in range(h):
        if graph[i][j]!="#":
            dfs(graph, i, j)
            if max_diamond<diamond:
                max_diamond = diamond
            diamond=0
f1.write(str(max_diamond))
