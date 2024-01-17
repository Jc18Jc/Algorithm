import sys
ssr = sys.stdin.readline
from queue import PriorityQueue
INF = 1000000

n, e = map(int, ssr().split())
node = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, ssr().split())
    node[a].append((b, c))
    node[b].append((a, c))

v1, v2 =map(int, ssr().split())

def dikj(start, end):
    if start==end:
        return 0
    distance = [INF for _ in range(n+1)]
    pq = PriorityQueue()
    check=[False for _ in range(n+1)]

    for item in node[start]:
        pq.put((item[1], item[0]))
        distance[item[0]]=item[1]
    check[start] = True
    while pq.qsize():
        v = pq.get()
        if check[v[1]]:
            continue
        check[v[1]]=True
        if v[1]==end:
            return distance[v[1]]
        for item in node[v[1]]:
            distance[item[0]]=min(distance[item[0]], v[0]+item[1])
            if not check[item[0]]:
                pq.put((distance[item[0]], item[0]))
    return -1

tmp1=[dikj(1, v1), dikj(v1, v2), dikj(v2, n)]
tmp2 = [dikj(1, v2), dikj(v2, v1), dikj(v1, n)]
if -1 in tmp1:
    if -1 in tmp2:
        print(-1)
    else:
        print(sum(tmp2))
else:
    if -1 in tmp2:
        print(sum(tmp1))
    else:
        print(min(sum(tmp1), sum(tmp2)))
