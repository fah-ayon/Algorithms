f=open('input4.txt','r')
f1=open('output4.txt','w')
elem =int(f.readline())
arr=[int(i) for i in f.readline().split()]
query=int(f.readline())

def find_Kth(arr, k):
  p = 0
  r = len(arr) - 1
  while p<=r:
    pivot = arr[r]
    i = p - 1
    for j in range(p,r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    pivot_idx = i+1
    
    if k-1 == pivot_idx:
        return arr[pivot_idx]
    elif k-1 < pivot_idx:
        r = pivot_idx - 1
    else:
        p = pivot_idx + 1


for i in range(query):
  key=int(f.readline())
  k=(find_Kth(arr,key))
  f1.write(f'{str(k)}\n')
f1.close()
