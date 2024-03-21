import sys
input = sys.stdin.readline
from queue import PriorityQueue

def firstDijkstra():
    pq = PriorityQueue()
    total = [-1 for _ in range(N+1)]
    total[S]=0
    root = [set() for _ in range(N+1)]
    for item in E[S]:
        pq.put((item[1], item[0], S, item[2]))
    while pq.qsize():
        c, next, pre, num = pq.get()
        if total[next]==-1 or total[next]==c:
            root[next].update([num])
            root[next] = root[next].union(root[pre])
            if total[next]==-1:
                for item in E[next]:
                    pq.put((c+item[1], item[0], next, item[2]))
            total[next]=c
    for item in root[D]:
        exception[item]=True

def dijkstra():
    pq = PriorityQueue()
    total = [-1 for _ in range(N+1)]
    total[S]=0
    for item in E[S]:
        pq.put((item[1], item[0], item[2]))
    while pq.qsize():
        c, next, num = pq.get()
        if not exception[num] and total[next]==-1:
            total[next]=c
            if next==D:
                break
            for item in E[next]:
                pq.put((total[next]+item[1], item[0], item[2]))
    else:
        return -1
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
    firstDijkstra()
    print(dijkstra())


#### 코드리뷰 ###
'''
import sys
from collections import deque

def dijkstra(graph, costlist, s):
    minload = [[]for x in range(n)]
    queue = deque([(s, 0)])
    costlist[s] = 0
    while queue:
        node, cost = queue.popleft()
        if cost > costlist[node]:
            continue
        for nnode, ncost in graph[node]:
            if ncost != -1:
                if costlist[nnode] > costlist[node] + ncost:
                    costlist[nnode] = costlist[node]+ncost
                    minload[nnode].clear()
                    minload[nnode].append(node)
                    queue.append((nnode, ncost))
                elif costlist[nnode] == costlist[node] + ncost:
                    minload[nnode].append(node)
    return minload

def bfs(d, minload, visit, graph):
    queue = deque([d])
    visit[d] = True
    while queue:
        node = queue.popleft()
        for nnode in minload[node]:
            if visit[nnode]==False:
                queue.append(nnode)
                visit[nnode]=True
            for index in range(len(graph[nnode])):
                if graph[nnode][index][0] == node:
                    graph[nnode][index][1] = -1
    return graph

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        exit()
    graph = [[]for x in range(n)]
    s, d = map(int, sys.stdin.readline().split())
    for i in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append([v, p])
    costlist = [1e10 for x in range(n)]

    minload = dijkstra(graph, costlist, s)
    visit = [False for x in range(n)]
    bfs(d, minload, visit, graph) # bfs가 왜 들어가야하지 ? 다익 - bfs - 다익할꺼면 다익 한 번에 해도 되는데, 경로 기억 못해서 이렇게 한 듯
    costlist = [1e10 for x in range(n)]
    dijkstra(graph, costlist, s)
    if costlist[d] == 1e10:
        print(-1)
    else:
        print(costlist[d])
'''