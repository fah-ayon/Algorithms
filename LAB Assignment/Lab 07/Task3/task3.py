f = open('input3.txt', 'r')
f1 = open('output3.txt' ,'w')

ppl, q = [int(i) for i in f.readline().split()]

queries = []
for i in range(q):
    a,b = [int(i) for i in f.readline().split()]
    queries.append((a,b))
#print(queries)
def find_grp(person, i):
    if person[i] == -1:
        return i
    return find_grp(person, person[i])

def union_set(person, size, i, j):
    root_i = find_grp(person, i)
    root_j = find_grp(person, j)
    if root_i != root_j:
        person[root_i] = root_j
        size[root_j] += size[root_i]

def max_friend(ppl, queries):
    size = [1]*(ppl+1)
    parents = [-1]*(ppl+1)
    for query in queries:
        a, b = query
        if find_grp(parents, a) != find_grp(parents, b):
            union_set(parents, size, a, b)
        #print(sizes[find_grp(parents, a)])
        total_size = size[find_grp(parents, a)]
        #print(str(total_size))
        f1.write(f'{str(total_size)}\n')

max_friend(ppl, queries)