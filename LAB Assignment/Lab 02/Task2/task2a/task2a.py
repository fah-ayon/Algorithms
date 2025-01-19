f = open('input2a.txt', 'r')
f1 = open('output2a.txt', 'w')
t = f.readline()
arr1 = [int(i) for i in f.readline().split()]
t1 = f.readline()
arr2 = [int(i) for i in f.readline().split()]
new_arr = (arr1 + arr2)
def merge(a,b):
    merged = []
    while a and b:
        if a [0]<= b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    return merged + a + b

def mergeSort(arr):
    if len(arr)<= 1:
        return arr
    else:
        mid = len(arr)//2
        h1 = mergeSort (arr[mid:])
        h2 = mergeSort (arr[:mid])
        return merge(h1,h2)
        
tar = mergeSort(new_arr)
for i in tar:
    f1.write(f'{str(i)} ')

f1.close()