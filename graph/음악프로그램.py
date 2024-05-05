import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree =[1e8] + [0 for _ in range(n)]

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, tmp[0]):
        graph[tmp[i]].append(tmp[i+1])
        degree[tmp[i+1]] += 1

dq = deque()
ans = []
for i in range(1, len(degree)):
    if(degree[i] == 0):
        dq.append(i)
        ans.append(i)

while dq:
    v= dq.popleft()
    for g in graph[v]:
        degree[g] -= 1
        if(degree[g] == 0):
            dq.append(g)
            ans.append(g)

if(len(ans) != n):
    print(0)
else:
    for a in ans:
        print(a)