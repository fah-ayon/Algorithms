f  = open('input1b.txt', 'r')
f1 = open('output1b.txt', 'w')
t, tar = [int(i) for i in f.readline().split()]
arr = [int(i) for i in f.readline().split()]
count1 = 0
count2 =0
flag = False

for i in range (len(arr)-1):
    count = 0
    for j in range(i+1 , len(arr)):
        if arr[i]+arr[j]==tar:
            flag = True
            count1 = i+1
            count2 = j+1
            count+=1
    if count == 0:
        break
    if count1 and count2 != 0:
        break

if flag == False :
    f1.write(f'IMPOSSIBLE')    
else:
    f1.write(str(count1)+" "+str(count2))

f1.close()
