f =  open('input3.txt', 'r')
f1 = open('output3.txt', 'w')
t = f.readline()
arr = [int(i) for i in f.readline().split()]

def quick_sort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)

    return arr

def partition(arr,p,r):
    pivot=arr[p]
    i=p

    for j in range (i+1,r+1):
        if arr[j]<pivot:
            i+=1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp

    temp=arr[i]
    arr[i]=pivot
    arr[p]=temp

    return i


n = len(arr)-1

res=(quick_sort(arr,0,n))
f1.write(str(res))
f1.close()