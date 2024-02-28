import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = int(input()), int(input())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))
    edge[b].append((a, c))
h = [(0, 1)]
visited = [False for _ in range(N+1)]
answer = 0

while h:
    v=heappop(h)
    w = v[0]
    node = v[1]
    if visited[node]:
        continue
    visited[node]=True
    answer+=w
    for next, w2 in edge[node]:
        if not visited[next]:
            heappush(h, (w2, next))

print(answer)


### 코드리뷰 ###
'''
# 정석적인 방법은 크루스칼(최소신장트리) 알고리즘, 나는 다익스트라 응용인데 속도가 뒤떨어지긴 함
# 생각해보니 결국 edge 중에 작은거부터 고르게 한건데, 굳이 다익스트라로 조사할 필요가 없긴 했네
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b): # 작은게 부모가 되도록
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b): # 이러면 find를 4번 실행하는데, 값 저장해두면 좋을 듯, 그렇게 변형해봤는데 왜 더 느리지 ,,, ?
        union_parent(a, b)
        result += c

print(result)
'''