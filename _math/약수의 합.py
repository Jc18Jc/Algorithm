import sys

# DP 1로 초기화
dp = [1]*(1000001)

# S: 값 누적 리스트
total = [0]*(1000001)

for i in range(2, 1000001):
    j=1
    while i*j <= 1000000:
        dp[i*j] += i
        j += 1

print(dp)

for i in range(1, 1000001):
    total[i] = total[i-1] + dp[i]

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    print(total[a])