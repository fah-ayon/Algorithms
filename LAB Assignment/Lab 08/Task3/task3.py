f = open('input3.txt', 'r')
f1 = open('output3.txt', 'w')
n, x = [int(i) for i in f.readline().split()]
coins = [int(i) for i in f.readline().split()]

def min_coin(coin, tar):
    dp = [float('inf')] * (tar + 1)
    dp[0] = 0
    for i in range(1, tar + 1):
        for c in coin: 
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    if dp[tar] != float('inf'):
        return dp[tar]
    else:
        return -1

res = min_coin(coins, x)  
f1.write(str(res))
f.close()
f1.close()
