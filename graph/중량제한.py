import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A].append((B, C))
    edge[B].append((A, C))

s, e = map(int, input().split())
wei = [-1 for _ in range(N+1)]
h = [(-1000000000, s)]

while h:
    v=heappop(h)
    cost = -v[0]
    node = v[1]
    if wei[node] != -1:
        continue
    wei[node]=cost
    for item in edge[node]:
        if wei[item[0]] != -1:
            continue
        cost2 = cost if cost < item[1] else item[1]
        heappush(h, (-cost2, item[0]))

print(wei[e])


### 코드리뷰 ###
'''
# 정석적인 방법이나 백준 분류는 BFS+이진탐색이라고 함, 나는 다익스트라 변형, 속도도 내꺼 좀 빠름
from collections import deque
import sys

input = sys.stdin.readline


def bfs(mid): # mid는 시작점부터 종점까지 옮길 수 있다고 가정한 가중치
    # bfs를 진행하는데, mid보다 가중치가 클 때만 q에 넣어줌, 목적지가 나오면 True 반환 아니면 False반환
    visited[start] = 1
    q = deque()
    q.append(start) 

    while q: # 각 노드가 가진 가중치를 직접적으로 안써서 bfs 구현이 쉬워보이긴 함
        now = q.popleft()
        if now == end:
            return True
        for nx, nc in graph[now]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1

    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n + 1):
    graph[i].sort(reverse=True) # 정렬을 왜 하지 ? 이유가 없어보이는데, ㅇㅇ 빼봤는데 똑같이 맞았음, 속도도 미미하게 향상

start, end = map(int, input().split())
low, high = 1, 1000000000 # 가중치의 최대 최소로 잡으면 더 빠를 것 같은데, 최악의 경우는 똑같긴 하겠네
while low <= high:
    visited = [0 for _ in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)
'''