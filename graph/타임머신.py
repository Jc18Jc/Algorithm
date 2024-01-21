import sys
ssr = sys.stdin.readline
INF = 100000000
n, m = map(int, ssr().split())
edge = []

for _ in range(m):
    a, b, c = map(int, ssr().split())
    edge.append((a,b,c))

distance = [INF for _ in range(n+1)]
distance[1] = 0
for i in range(n):
    for j in range(m):
        s = edge[j][0]
        e = edge[j][1]
        c = edge[j][2]
        if distance[s] != INF and distance[e] > distance[s]+c:
            distance[e]=distance[s]+c
            if i == n-1:
                exit(print(-1))
for i in range(2, n+1):
    if distance[i]==INF:
        print(-1)
        continue
    print(distance[i])