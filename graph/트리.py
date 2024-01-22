import sys
ssr = sys.stdin.readline
from collections import deque

n = int(ssr())

parents = list(map(int, ssr().split()))
p = int(ssr())
child = [[] for _ in range(n)]

start=0
for i in range(n):
    if parents[i]==-1:
        start=i
        continue
    if i == p:
        continue
    child[parents[i]].append(i)

count = 0

d = deque()
if start!=p:
    d.append(start)

while d:
    v=d.popleft()
    if child[v]:
        for item in child[v]:
            d.append(item)
    elif not child[v] and v!=p:
        count+=1

print(count)