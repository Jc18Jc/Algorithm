import sys
ssr = sys.stdin.readline
INF=100000000

t = int(ssr())

for _ in range(t):
    n, m, w = map(int, ssr().split())
    edge = []
    for _ in range(m): 
        s, e, t = map(int, ssr().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, ssr().split())
        edge.append((s, e, -t))
    l = len(edge)
    distance = [0 for _ in range(n+1)]
    for j in range(n-1):
        for i in range(l):
            start = edge[i][0]
            end = edge[i][1]
            time = edge[i][2]
            if distance[start]+time < distance[end]:
                distance[end] = distance[start]+time
    flag=True
    for i in range(l):
        start = edge[i][0]
        end = edge[i][1]
        time = edge[i][2]
        if distance[start]+time < distance[end]:
            print('YES')
            flag=False
            break
    if flag:
        print('NO')