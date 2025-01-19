f =  open('input3.txt','r')
f1 =  open('output3.txt', 'w')

t = int(f.readline())
id =  list(map(int,f.readline().split()))
marks = list(map(int,f.readline().split()))

for i in range(t-1):
    count = 0
    for j in range(0-t-1):
        if mark[j] < mark[j+1] or mark[j]== mark[j+1] and id[j]> id [j+1]:
            mark[j], mark[j+1] = mark [j+1], mark[j]
            id [j], id[j+1] = id[j+1], id[j]
            count += 1
        
    if count== 0:
        break

for k in range(t):
    f1.write(f'ID: {id[k]} Marks: {marks[k]}\n')


