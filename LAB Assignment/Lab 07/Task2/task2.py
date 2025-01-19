f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')
num_of_task, num_of_man = [int(i) for i in f.readline().split()]
task = [[] for i in range(num_of_task)]

for i in range(num_of_task):
    start_time, end_time = [int(i) for i in f.readline().split()]
    task[i].extend([start_time, end_time])

task.sort(key=lambda x: x[1])

count = 0
assigned = [-1] * num_of_man

for i in task:
    start = i[0]
    end = i[1]
    temp = float('-inf')
    idx = -1
    for j in range(len(assigned)):
        if start >= assigned[j]:
            if assigned[j] >= temp:
                temp = assigned[j]
                idx = j
    if idx != -1:
        assigned[idx] = end
        count += 1

f1.write(str(count))


