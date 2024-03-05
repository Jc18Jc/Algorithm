import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m = int(input()), int(input())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))
start, end = map(int, input().split())
h=[(0, start, start)]
route = [(-1, -1) for _ in range(n+1)]
while h:
    cost, pre, current = heappop(h)
    if route[current][1] != -1:
        continue
    route[current] = (cost, pre)
    for node, c in edge[current]:
        if route[node][0] == -1:
            heappush(h, (cost+c, current, node))

answer = [end]
node = end
while node != start:
    node = route[node][1]
    answer.append(node)
answer.reverse()
print(route[end][0])
print(len(answer))
print(*answer)


### 코드리뷰 ###
'''
import sys
from collections import defaultdict
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
# defaultdict는 dict와 동작은 거의 일치한데, 객체의 기본값을 초기화 가능, dict 쓸 때 존재 유무 확인 후 하는 작업이 필요없어짐, 좋다
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().rstrip().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight: # 어짜피 힙+다익스트라 쓰면 최소값부터 들어갈텐데 방문 표시만 하면 안되나?
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < dist[adj_node]: # 탐색하는 과정에서 dist를 갱신해주니까 거리 비교하는구나
                dist[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(dist[end])

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))
'''