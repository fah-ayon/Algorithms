f =  open('input1.txt', 'r')
f1 = open('output1.txt', 'w')
t =  f.readline()
arr1= [int(i) for i in f.readline().split()] 

def pairs(arr):
    def mergeCount(arr, s, m, e):
        total_count = 0
        L_half = arr[s:m+1]
        R_half = arr[m+1:e+1]
        i= 0
        j = 0
        k = s
        while i < len(L_half) and j < len(R_half):
            if L_half[i] > R_half[j]:
                total_count += len(L_half) - i
                arr[k] = R_half[j]
                j += 1
            else:
                arr[k] = L_half[i]
                i += 1
            k += 1

        while i < len(L_half):
            arr[k] = L_half[i]
            i += 1
            k += 1

        while j < len(R_half):
            arr[k] = R_half[j]
            j += 1
            k += 1

        return total_count

    def mergeSort_counter(arr,s,e):
        if s>= e:
            return 0

        m = (s + e) // 2
        L_count = mergeSort_counter(arr, s, m)
        R_count = mergeSort_counter(arr, m+1, e)
        cross_count = mergeCount(arr, s, m, e)
        T_count = L_count+R_count+cross_count

        return T_count

    pair = mergeSort_counter(arr, 0, len(arr)-1)
    return pair

res = pairs(arr1)
f1.write(f'{str(res)}')
f1.close()
