f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')

fst_line = int(f.readline().strip())
arr = list(map(int , f.readline().split()))

def bubbleSort(arr): 
    for i in range(len(arr)-1):
        count =0 
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
               count += 1    
        if count == 0:
            break
               

bubbleSort(arr)
f1.write(" ".join(map(str, arr)))


#count is a variable that keeps track of swapping, if swap it will incrememt, if there is no swap thats mean the variable will be remain 0 thats mean the array is already sorted
#And after that the loop will break and it will reduce run time and the time complexity will be O(n)


