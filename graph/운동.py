import sys
input=sys.stdin.readline

N, M = map(int, input().split())
dist = [[10**8 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1]=c

for i in range(N):
    for j in range(N):
        for k in range(N):
            if dist[j][k] > dist[j][i]+dist[i][k]:
                dist[j][k] = dist[j][i]+dist[i][k]
answer=dist[i][i]
for i in range(1,N):
    answer=min(answer, dist[i][i])
print(answer if answer != 10**8 else -1)

### 코드리뷰 ###
# 해당 문제는 python으로 제출하면 틀리고 pypy로 제출해야 맞음, 다른 사람들도 거의다 pypy로 풀었음
# 찾다가 개선된 다익스트라 방법으로 python 제출 맞은게 있길래 가져옴, 내껀 플로이드 워셜 방법
'''
import heapq as hq

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[1e9] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    hq.heappush(heap, [c, x, y])

while heap: # 크루스칼로 돌리는데 출발지와 목적지가 같으면 순환이구나, 크루스칼 생각했는데 종료 조건을 못찾았는데... 반성
    d, s, g = hq.heappop(heap)
    if s == g:
        print(d)
        break
    if dist[s][g] < d:
        continue
    for nd, ng in graph[g]:
        new_d = d + nd
        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            hq.heappush(heap, [new_d, s, ng])
else:
    print(-1)
'''