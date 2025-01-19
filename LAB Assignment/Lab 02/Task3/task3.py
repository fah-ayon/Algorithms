f = open('input3.txt', 'r')
f1 = open('output3.txt', 'w')
t= f.readline()
arr1 = [int(i) for i in f.readline().split()]

def merge(a, b):
    merged =  []
    while a and b:
        if a[0]<=b [0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    return merged + a + b

def mergeSort(arr):
    if len(arr) <=1:
        return arr
    else:
        mid = len(arr)//2
        h1 = mergeSort(arr[mid:])
        h2 = mergeSort(arr[:mid])
        return merge(h1,h2)

new_arr = mergeSort(arr1)
for i in new_arr:
    f1.write(f'{i} ')

f1.close()