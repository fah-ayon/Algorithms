f  = open('input1a.txt', 'r')
f1 = open('output1a.txt', 'w')
t, tar = [int(i) for i in f.readline().split()]
arr = [int(i) for i in f.readline().split()]
count1 = 0
count2 = 0
flag = False

for i in range (len(arr)-1):
    for j in range(i+1 , len(arr)):
        if arr[i]+arr[j]==tar:
            flag = True
            count1 = i+1
            count2 = j+1
            break
    if count1 and count2 != 0:
        break

if flag == False:
    f1.write(f'IMPOSSIBLE')    
else:
    f1.write(f'{str(count1)} {str(count2)}')

f1.close()
