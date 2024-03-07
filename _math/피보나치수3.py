# 피사노 주기, N번째 피보나치 수를 어떤 값 M으로 나눌 때, M=10^k (k>2)라면 P=15*10^(k-1)이고, N%P번째 피보나치 수와 같다
n=int(input())
p=1500000
array = [0, 1] + [0 for _ in range(p)]
for  i in range(2, p):
    array[i]=(array[i-1]+array[i-2])%1000000
print(array[n%p])

### 코드리뷰 ###
'''
N = int(input()) % (15 * 10**5)
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
for i in range(2,N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 1000000
print(dp[N])
'''