f = open('input4.txt', 'r')
f1 = open('output4.txt', 'w')
t= f.readline()
arr1 = [int(i) for i in f.readline().split()]


def mergeSort(arr1):
    if len(arr1) <=1:   
        return arr1[0] 
    else:
        mid = len(arr1)//2
        h1 = mergeSort(arr1[mid:]) #...........T(n/2)
        h2 = mergeSort(arr1[:mid]) #...........T(n/2)
        if h1>h2:
            return h1
        return h2
        

max_val = mergeSort(arr1)
f1.write(str(max_val))
f1.close()
#Time complexity of this code is O(nlogn)
