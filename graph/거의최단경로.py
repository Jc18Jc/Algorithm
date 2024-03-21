import sys
input = sys.stdin.readline
from queue import PriorityQueue



def dijkstra():
    pq = PriorityQueue()
    total = [-1 for _ in range(N+1)]
    total[S]=0
    root = [[] for _ in range(N+1)]
    for item in E[S]:
        pq.put((item[1], item[0], S, item[2]))
    while pq.qsize():
        c, next, pre, num = pq.get()
        if not exception[num] and total[next]==-1:
            root[next]=root[pre]+[num]
            total[next]=c
            if next==D:
                break
            for item in E[next]:
                pq.put((total[next]+item[1], item[0], next, item[2]))
    else:
        return -1
    for item in root[D]:
        exception[item]=True
    print(root[D])
    return total[D]
        
        
while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    S, D = map(int, input().split())
    E=[[] for _ in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        E[a].append((b, c, i))
    exception=[False for _ in range(M)]
    cost=dijkstra()
    answer = cost
    while answer==cost and answer != -1:
        answer=dijkstra()
    print(answer)