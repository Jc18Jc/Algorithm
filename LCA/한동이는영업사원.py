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
parents = [[-1 for _ in range(ml)] for _ in range(n+1)]
dep = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, ssr().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
dq.append((1, 1))
parents[1][0]=0

while dq:
    v=dq.popleft()
    p=v[0]
    d=v[1]
    for item in graph[p]:
        if parents[item][0] != -1:
            continue
        parents[item][0]=p
        dep[item]=d
        dq.append((item, d+1))


for i in range(1, ml):
    for j in range(1, n+1):
        parents[j][i] = parents[parents[j][i-1]][i-1]

start=1
count=0
m = int(ssr())
for _ in range(m):
    des = int(ssr())
    a,b =start, des
    if dep[a] > dep[b]:
        a, b = b, a
    for i in range(ml-1, -1, -1):
        if dep[b]-dep[a] >= (1 << i):
            b=parents[b][i]
            count+=1<<i
    if a!=b:
        for i in range(ml-1, -1, -1):
            if parents[b][i]!=parents[a][i]:
                a=parents[a][i]
                b=parents[b][i]
                count += 1<<(i+1)
        a=parents[a][0]
        count+=2
    start=des
print(count)

    