import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

N=int(input())
M=int(input())
edge = [[] for _ in range(N)]
dir = [0 for _ in range(M)]
degree = [0 for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a-1].append((b-1, c, i))
    degree[b-1]+=1
    dir[i]=a-1
start, end = map(int, input().split())
start-=1
end-=1

distance=[0 for _ in range(N)]
rootList=[set() for _ in range(N)]
visited = [False for _ in range(N)]
s=set()

def search(node):
    if node==start:
        return
    if visited[node]:
        return
    visited[node]=True
    for edgeNum in rootList[node]:
        s.add(edgeNum)
        search(dir[edgeNum])

def dag():
    q=deque()
    q.append(start)
    while q:
        v=q.popleft()
        for node, cost, edgeNum in edge[v]:
            degree[node]-=1
            if distance[node] < distance[v]+cost:
                rootList[node].clear()
            if distance[node] <= distance[v]+cost:
                rootList[node].add(edgeNum)
                distance[node]=distance[v]+cost
            if degree[node]==0:
                q.append(node)

dag()
search(end)
print(distance[end])
print(len(s))


### 코드리뷰 ###
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input()) 

time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    in_degree[b] += 1

src, dst = map(int, input().split())

q = deque([])
q.append(src)

while q: # dag는 완전 똑같음
    now = q.popleft()
    for i in graph[now]:
        in_degree[i[1]] -= 1
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)
        if in_degree[i[1]] == 0:
            q.append(i[1])

q = deque([dst])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]: # 하나의 노드에서 하나의 노드로 가는 엣지는 하나라서 edgeNum 대신 이전 노드 저장해서 한 듯
        if (now, x) not in route: # visited 대신하는 느낌
            route.add((now, x))
            q.append(x)

print(time[dst])
print(len(route))

'''