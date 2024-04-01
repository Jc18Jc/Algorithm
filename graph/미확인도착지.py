import sys
input = sys.stdin.readline
from queue import PriorityQueue

for _ in range(int(input())):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    E = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        E[a].append((b,d))
        E[b].append((a,d))
    cand = [int(input()) for _ in range(t)]
    visited = [10**8 for _ in range(n+1)]
    answer=set()
    pq = PriorityQueue()
    pq.put((0, True, s))

    while pq.qsize():
        cost, check, node=pq.get()
        if visited[node] <= cost:
            continue
        if node in cand and not check:
            answer.add(node)
        visited[node]=cost
        for next, c in E[node]:
            if visited[next] > cost+c and (node, next) == (g, h) or (node, next) == (h, g):
                pq.put((cost+c, False, next))
            elif visited[next] > cost+c :
                pq.put((cost+c, check, next))
    answer=list(answer)
    answer.sort()
    print(*answer)

### 코드리뷰 ###
# 해당 코드는 나랑 거의 일치하지만 다른 코드 보니 목표 간선의 가중치를 0.5 낮추면 flag없이도 그냥 다익스트라 돌려도 가능한 듯
'''
from sys import stdin
import heapq
input = stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start))
    while q:
        dist, flag, curr = heapq.heappop(q)
        if distance[curr] <= dist:
            continue
        distance[curr] = dist
        flaghg[curr] = flag
        for next, next_dist in roads[curr]:
            cost = dist + next_dist
            if distance[next] >= cost:
                if (next, curr) == (h, g) or (next, curr) == (g, h): # 이렇게 구현하는 사람이 더 있구나 똑같아서 소름
                    heapq.heappush(q, (cost, -1, next)) # cost 이후로 flag로 정렬되게 하는 것도 똑같네
                else:
                    heapq.heappush(q, (cost, flag, next))

T = int(input())
ans = []
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    roads = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    flaghg = [0] * (n + 1)
    destinations = set()
    for _ in range(m):
       a, b, d = map(int, input().split())
       roads[a].append((b, d))
       roads[b].append((a, d))
    for _ in range(t):
       destinations.add(int(input()))
    dijkstra(s)
    trueflaghg = set([x for x in range(n + 1) if flaghg[x] == -1]) # 중간에 목적지 체크하는게 아니고 목적지랑 교집합 괜찮네
    resList = sorted(list(destinations.intersection(trueflaghg)))
    ans.append(resList)

for answer in ans:
    for res in answer:
        print(res, end=' ')
    print()

'''