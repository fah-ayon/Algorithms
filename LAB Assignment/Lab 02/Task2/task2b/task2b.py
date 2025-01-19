f = open('input2b.txt', 'r')
f1 = open('output2b.txt', 'w')

t = f.readline()
arr1 =  [int(i) for i in f.readline().split()]
t2 = f.readline()
arr2 = [int(i) for i in f.readline().split()]


def merge(a,b ):
    merged = []
    while a and b:
        if a[0]<=b[0]:
            merged.append(a.pop(0))
        else:
            merged.append (b.pop(0))
    return merged + a + b

arr3= merge(arr1, arr2)
for i in arr3:
    f1.write(f'{str(i)} ')

f1.close()