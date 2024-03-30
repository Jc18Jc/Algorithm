import sys
input = sys.stdin.readline

N=int(input())
reserve = [list(map(int, input().split())) for _ in range(N)]
total = [0 for _ in range(N+1)]
for i in range(1, N+1):
    day, benefit = reserve[i-1]
    if i+day-1 < N+1:
        total[i+day-1]=max(total[i+day-1], total[i-1]+benefit)
    total[i] = max(total[i], total[i-1])

print(total[N])


### 코드리뷰 ###
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1): # 나랑 구현은 아예 똑같네 순서만 좀 다르고
    dp[i] = max(dp[i], dp[i - 1]) # 나는 1일짜리 일 생각해서 마지막에 넣었는데 1일짜리 일이어도 값 변동은 똑같네
    fin_date = i + t[i]
    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
print(max(dp)) # max가 아니고 dp[n]해도 될 듯
'''