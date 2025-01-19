
f = open('input1a.txt', 'r')
f1 = open('output1a.txt', 'w')

nodes, edges = [int(i) for i in f.readline().split()] 
matrix = []

for i in range(nodes+1):
    row = []
    for j in range(nodes+1):
        row.append(0)
    matrix.append(row)
def func(m):
    return map(int, m.split())
for u,v,w in map(func, f.readlines()):
    matrix [u][v] = w
for row in matrix:
    for i in row:
        f1.write(f'{str(i)} ')
    f1.write('\n') 