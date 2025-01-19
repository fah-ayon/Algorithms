f = open('input1a.txt', 'r')
f1 = open('output1a.txt', 'w')

v,e = [int(i) for i in f.readline().split()]
adj_list = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
visited_cycle = [0 for i in range(v+1)]
stack = []

def dfs_traverse(parent):
    visited[parent]= 1
    for adj_node in adj_list[parent]:
        if visited[adj_node] ==0:
            dfs_traverse(adj_node)
    stack.append(parent)
    
def Cycle_Detect(selected):
    visited_cycle[selected]=1
    for adj_node in adj_list[selected]:
        if visited_cycle[adj_node] == 0:
            cycle_detected = Cycle_Detect(adj_node)
            if cycle_detected:
                return True
        elif visited_cycle[adj_node] == 1:
            return True
    visited_cycle[selected] = 2
    return False
for i in range(1, (e+1)):
    a,b= [int(i) for i in f.readline().strip().split()]
    #print(a,b)
    adj_list[a].append(b)

cycle_exist = False
for i in range(1, (v+1)):
    if visited_cycle[i]==0:
        is_cycle = Cycle_Detect(i)
        if is_cycle:
            cycle_exist = True
            break
if cycle_exist:
    f1.write('IMPOSSIBLE')
else:
    for i in range(1, (v+1)):
        if visited[i]==0:
            dfs_traverse(i)
    while len(stack)!=0:
        f1.write(f'{stack.pop(-1)} ')        
f.close()
f1.close()