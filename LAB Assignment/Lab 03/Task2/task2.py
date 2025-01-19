f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')
t = f.readline()
arr1 = [int(i) for i in f.readline().split()]
#print(arr1)
def abs_val(arr):
  ret = -10000000
  for i in arr:
    if abs(i)> ret:
      ret = abs(i)
  return ret


def getmax(arr):
  n =  len(arr)
  mid = n//2
  if n==1:
    return -10000000 
  if n ==2:
    return arr[0]+ arr[1]**2
  l_max = getmax(arr[:mid])
  r_max = getmax(arr[mid:])
  cross_max = max(arr[:mid])+ (abs_val(arr[mid:]))**2
  return max(l_max,r_max,cross_max)


res = getmax(arr1)
f1.write(f'{str(res)}')
f1.close()
