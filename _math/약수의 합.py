import sys

dp = [1]*(1000001)
total = [0]*(1000001)

for i in range(2, 1000001):
    j=1
    while i*j <= 1000000:
        dp[i*j] += i
        j += 1

for i in range(1, 1000001):
    total[i] = total[i-1] + dp[i]

case_num = int(sys.stdin.readline())

for _ in range(case_num):
    a = int(sys.stdin.readline())
    print(total[a])