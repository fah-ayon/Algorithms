import heapq
f = open('input2.txt', 'r')
f1 = open('output2.txt' , 'w')

n,m = [int(i) for i in f.readline().split()]
adj_list = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
visited_cycle = [0 for i in range(n+1)]
indegree = [0 for i in range(n+1)]

def bfs_toposort(adj_list, indegree):
    q = []
    for i in range(1, (n+1)):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    res= []
    while q:
        temp = heapq.heappop(q)
        res.append(temp)
        for adj_node in adj_list[temp]:
            indegree[adj_node] -=1
            if indegree[adj_node]==0:
                heapq.heappush(q, adj_node)
    return res

def Cycle_Detect(selected):
    visited_cycle[selected] = 1
    for adj_node in adj_list[selected]:
        if visited_cycle[adj_node]==0:
            cycle = Cycle_Detect(adj_node)
            if cycle:
                return True
        elif visited_cycle[adj_node] == 1:
            return True
    visited_cycle[selected] = 2
    return False




for i in range(1, (m+1)):
    a,b = [int(i) for i in f.readline().strip().split()]
    adj_list[a].append(b)
    indegree[b] += 1

Cycle_Exist = False
for i in range(1, n+1):
    if visited_cycle[i] == 0:
        is_Cyclic= Cycle_Detect(i)
        if is_Cyclic:
            Cycle_Exist = True
            break
if Cycle_Exist:
    print("IMMPOSSIBLE", file=f1)
else:
    print(*bfs_toposort(adj_list, indegree), file=f1)   

f.close()
f1.close()