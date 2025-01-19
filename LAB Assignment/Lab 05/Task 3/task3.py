f= open('input3.txt', 'r')
f1 =  open('output3.txt', 'w')

n,m = [int(i) for i in f.readline().split()]
adj_list = [[] for i in range(n+1)]
in_adj_list = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
in_visited = [0 for i in range(n+1)]
stack  = []
components = []

def dfs(source):
    visited[source] = 1
    for adj_node in adj_list[source]:
        if visited[adj_node]==0:
            dfs(adj_node)
    stack.append(source)
def inverse_dfs(source,components):
    in_visited[source] =1
    for adj_node in in_adj_list[source]:
        if in_visited[adj_node] == 0:
            inverse_dfs(adj_node,components)
    components.append(source)
for i in range(1, (m+1)):
    a,b = [int(i) for i in f.readline().strip().split()]
    adj_list[a].append(b)
    in_adj_list[b].append(a)
for i in range(1, (n+1)):
    if visited[i] ==0:
        dfs(i)
stack.reverse()
for i in stack:
    if in_visited[i]==0:
        components = []
        inverse_dfs(i, components)
        print(*components, file=f1)

f.close()
f1.close()


