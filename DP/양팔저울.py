N=int(input())
weight=list(map(int, input().split()))
input()
marble=list(map(int, input().split()))

def dfs(index, w):
    if dp[index][w]: return
    dp[index][w]=True
    if index == N: return
    dfs(index+1, w)
    dfs(index+1, w+weight[index])
    dfs(index+1, abs(w-weight[index]))

dp=[[False for _ in range(15001)] for _ in range(N+1)]
dfs(0,0)

for m in marble:
    if sum(weight) < m:
        print('N', end=' ')
        continue
    for i in range(1, N+1):
        if dp[i][m]:
            print('Y', end=' ')
            break
    else:
        print('N', end=' ')


### 코드리뷰 ###
# 아이디어 자체는 해당 블로그에서 가져옴, 코드 구조 차이만 보자
'''
import sys
input = sys.stdin.readline

def cal(num, weight):
  if num > n:  return
  if d[num][weight]:  return
  d[num][weight] = True 
  cal(num + 1, weight + weights[num - 1])
  cal(num + 1, abs(weight - weights[num - 1]))
  cal(num + 1, weight)

n = int(input()) 
weights = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
d = [[False] * 15001 for _ in range(31)]

cal(0, 0)

for t in target:
  if t > 15000:  print("N", end=" ") 
  elif d[n][t]: print("Y", end=" ") # for문 안쓰고 마지막꺼만 봐도 되는구나
  else:  print("N", end=" ")
'''