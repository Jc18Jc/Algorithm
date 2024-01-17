import sys
ssr = sys.stdin.readline
from collections import deque

n = int(ssr())
ml = 0
while True:
    if 2**ml > n:
        break
    ml+=1
graph = [[] for _ in range(n+1)]
parents = [[[-1,0,1000000] for _ in range(ml)] for _ in range(n+1)]
dep = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, ssr().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dq = deque()

dq.append((1, 1))
parents[1][0][0]=0

while dq:
    v=dq.popleft()
    p=v[0]
    d=v[1]
    for item in graph[p]:
        child = item[0]
        cost = item[1]
        if parents[child][0][0] != -1:
            continue
        parents[child][0][0]=p
        parents[child][0][1]=cost
        parents[child][0][2]=cost
        dep[child]=d
        dq.append((child, d+1))

for i in range(1, ml):
    for j in range(1, n+1):
        parents[j][i][0] = parents[parents[j][i-1][0]][i-1][0]
        parents[j][i][1] = max(parents[j][i-1][1], parents[parents[j][i-1][0]][i-1][1])
        parents[j][i][2] = min(parents[j][i-1][2], parents[parents[j][i-1][0]][i-1][2])


k = int(ssr())
for _ in range(k):
    a, b = map(int, ssr().split())
    mi, ma = 1000000, 0
    if dep[a] > dep[b]:
        a, b = b, a
    for i in range(ml-1, -1, -1):
        if dep[b]-dep[a] >= (1 << i):
            mi = min(mi, parents[b][i][2])
            ma = max(ma, parents[b][i][1])
            b=parents[b][i][0]
    if a!=b:
        for i in range(ml-1, -1, -1):
            if parents[b][i][0]!=parents[a][i][0]:
                mi = min(mi, parents[b][i][2], parents[a][i][2])
                ma = max(ma, parents[b][i][1], parents[a][i][1])
                a=parents[a][i][0]
                b=parents[b][i][0]
        mi = min(mi, parents[b][0][2], parents[a][0][2])
        ma = max(ma, parents[b][0][1], parents[a][0][1])
    print(mi, ma)

    