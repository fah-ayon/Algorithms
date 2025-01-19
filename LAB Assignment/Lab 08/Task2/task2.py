f= open('input2.txt','r')
f1 = open('output2.txt', 'w')
def fibo(n):
    if n == 0 or n==1:
        return 1
    step = [0]*(n+1)
    step[1]= 1
    step [2] = 2
    for i in range(3, n+1):
        step[i] = step[i-1] + step[i-2]
    return step[n]
n= int(f.readline())
total_step = fibo(n)
f1.write(str(total_step))
f.close()
f1.close()