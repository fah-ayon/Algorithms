f = open('input1.txt', 'r')
f1 = open('output1.txt', 'w')
num_of_task = int(f.readline())
task = [[] for i in range(num_of_task)]
for i in range(num_of_task):
    start_time , end_time = [int(i) for i in f.readline().split()]
    task[i].append(start_time)
    task[i].append(end_time)
    #print(start_time,end_time)
task.sort(key=lambda x:x[1:])
#print(task)
list1 = []
list1.append(task[0])
#print(list1)
counter = 0
for i in range(1,num_of_task):
    if task[counter][1]<=task[i][0]:
        counter = i
        list1.append(task[i])
#print(len(list1))
f1.write(f'{str(len(list1))}\n')
for k in list1:
    x,y = k[0],k[1]
    print(f'{x} {y}')
    f1.write(f'{x} {y}\n')

