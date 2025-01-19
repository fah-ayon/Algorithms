f = open('input4.txt', 'r')
f1 =  open('output4.txt', 'w')


lst = f.readlines() [1:]
lst = [*lst[:-1], lst[-1]+"\n"]
trn = [line.split()[0] for line in lst]
trn_time = [line.split()[-1] for line in lst]


for i in range(len(lst)-1):
        count= 0
        for j in range(len(lst)-i-1):
            if trn[j] > trn[j+1] or (trn[j] == trn[j+1] and trn_time[j] > trn_time[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                trn[j], trn[j+1] = trn[j+1], trn[j]
                trn_time[j], trn_time[j+1] = trn_time[j+1], trn_time[j]
                count += 1
        if count == 0:
            break

f1.writelines(lst)

