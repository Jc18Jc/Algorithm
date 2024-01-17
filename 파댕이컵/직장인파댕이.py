import sys
from heapq import heappop, heappush
ssr = sys.stdin.readline
INF = 1 << 40
n, m ,k = map(int, ssr().split())

can  = [[] for _ in range(n+1)]
di = [[0 for _ in range(n+1)] for _ in range(2)]
for _ in range(m):
    a, b, c = map(int, ssr().split())
    can[a].append((b,c))
    can[b].append((a,c))

visited = [[False for _ in range(n+1)] for _ in range(2)]

el = list(map(int, ssr().split()))
el.insert(0, -1)

h = []

for item in can[1]:
    heappush(h, (item[1], 0, item[0]))
if el[1] != -1:
    heappush(h, (el[1]*(k-1), 1, 1))
visited[0][1]=True

while h:
    v=heappop(h)
    if visited[v[1]][v[2]]:
        continue
    visited[v[1]][v[2]]=True
    di[v[1]][v[2]] = v[0]

    if v[1]==1 and v[2]==n:
        break
    for item in can[v[2]]:
        if not visited[v[1]][item[0]]:
            heappush(h, (v[0]+item[1], v[1], item[0]))
    if v[1]==0 and el[v[2]] != -1:
        heappush(h, (v[0]+el[v[2]]*(k-1), 1, v[2]))

if visited[1][n]:
    print(di[1][n])
else:
    print(-1)