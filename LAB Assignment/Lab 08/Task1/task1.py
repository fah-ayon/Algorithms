f =open('input1.txt', 'r')
f1 = open('output1.txt', 'w')
n, m = [int(i) for i in f.readline().split()]
graph = []
for i in range(m):
    u,v,w = [int(i) for i in f.readline().split()]
    graph.append((u,v,w))

class disjoint_set:
    def __init__(self,size):
        self.len = list(range(size))
    def find(self,i):
        if self.len[i] != i:
            self.len[i] = self.find(self.len[i])
        return self.len[i]
    def union(self,i,j):
        a = self.find(i)
        b = self.find(j)
        if a !=b:
            self.len[a] = b


def mini_cost(n,graph):
    graph.sort(key=lambda x:x[2])
    d_set = disjoint_set(n)
    total_cost = 0
    for u,v,w in graph:
        if d_set.find(u-1) != d_set.find(v-1):
            d_set.union(u-1,v-1)
            total_cost += w
    return total_cost
res = mini_cost(n,graph)
f1.write(str(res))
f.close()
f1.close()