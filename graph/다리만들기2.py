# import sys
# input = sys.stdin.readline
# from collections import deque
# from queue import PriorityQueue
# delta = ((0,0,1,-1), (1,-1,0,0))

# N, M = map(int, input().split())
# board = list(list(map(int, input().split()))for _ in range(N))

# def separateLand():
#     visited = [[False for _ in range(M)]for _ in range(N)]
#     d=deque()
#     landList=[]
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and board[i][j]:
#                 d.append((i, j))
#                 visited[i][j]=True
#                 tmp=[(i,j)]
#                 while d:
#                     ni, nj = d.popleft()
#                     for k in range(4):
#                         di, dj = ni+delta[0][k], nj+delta[1][k]
#                         if -1 < di < N and -1 < dj < M and board[di][dj] and not visited[di][dj]:
#                             d.append((di, dj))
#                             tmp.append((di, dj))
#                             visited[di][dj]=True
#                 landList.append(tmp)
#     return landList

# def putBridge(landList):
#     E=[[] for _ in range(len(landList))]
#     for i in range(len(landList)):
#         for j in range(len(landList[i])):
#             ni, nj = landList[i][j]
#             for k in range(4):
#                 di, dj = ni+delta[0][k], nj+delta[1][k]
#                 if -1 < di < N and -1 < dj < M and not board[di][dj]:
#                     count=0
#                     while -1 < di < N and -1 < dj < M:
#                         if board[di][dj]:
#                             if (di, dj) not in landList[i] and count > 1:
#                                 for t in range(len(landList)):
#                                     if (di, dj) in landList[t]:
#                                         E[i].append((t,count))
#                                         break
#                             break
#                         di+=delta[0][k]
#                         dj+=delta[1][k]
#                         count+=1
#     if not E[0]:
#         return -1
#     pq = PriorityQueue()
#     pq.put((0, 0))
#     dijkstra = [1000 for _ in range(len(landList))]
#     while pq.qsize():
#         cost, num = pq.get()
#         if dijkstra[num]!=1000:
#             continue
#         dijkstra[num]=cost
#         for node, c in E[num]:
#             if dijkstra[node]==1000:
#                 pq.put((c, node))
#     answer = sum(dijkstra)
#     return answer if answer < 1000 else -1
    

# landList = separateLand()
# print(putBridge(landList))

### 코드리뷰 ###
'''
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
edge = set()

def condition(ni, nj):
    return ni < 0 or ni >= n or nj < 0 or nj >= m
    
def marking(y, x, mark):
    q = deque()
    q.append((y, x))
    graph[y][x] = mark
    visited[y][x] = True
    while q:
        i, j = q.popleft()
        for dy, dx in dir:
            ni, nj = i + dy, j + dx
            if condition(ni, nj) or not graph[ni][nj] or visited[ni][nj]:   continue # or로 신기하게 짰네,, 비충족 조건을 만들었구나 보기 어렵다
            graph[ni][nj] = mark # 맵 자체에 숫자를 넣는건 내가 왜 생각 못했을까,, 훨씬 좋을 듯
            visited[ni][nj] = True
            q.append((ni, nj))

def getDist(y, x, now):
    q = deque()
    for idx in range(4):
        q.append((y, x, 0, dir[idx]))
    while q:
        i, j, cnt, nowDir = q.popleft()
        if graph[i][j] != 0 and graph[i][j] != now:
            if cnt > 2:
                edge.add((cnt - 1, now, graph[i][j]))
            continue
        ni, nj = i + nowDir[0], j + nowDir[1]
        if condition(ni, nj) or graph[ni][nj] == now:   continue
        q.append((ni, nj, cnt + 1, nowDir))
            

mark = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]: # visited도 없이 그냥 graph[i][j]==1해도 될 듯, mark를 2부터 시작하고
            marking(i, j, mark)
            mark += 1
        

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            visited = [[False] * m for _ in range(n)]
            getDist(i, j, graph[i][j])

edge = list(edge)
edge.sort()

def findParent(parent, x):
    if x != parent[x]:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
    
parent = [i for i in range(mark)]

result = 0

num = 0
for cost, a, b in edge: # 엣지 전체를 정렬해서 작은 것부터 안겹치게 하는 유니온-파인드인데, 그냥 다익스트라 돌려도 될 듯
    if findParent(parent, a) != findParent(parent, b):
        num += 1
        unionParent(parent, a, b)
        result += cost
        
if result == 0 or  num != mark - 2:
    print(-1)
else:   print(result)
'''

### 수정코드 ###
# 생각보다 드라마틱하게 코드길이가 줄진 않았네 2428 -> 2142, 시간은 104 -> 96
import sys
input = sys.stdin.readline
from collections import deque
from queue import PriorityQueue
delta = ((0,0,1,-1), (1,-1,0,0))

N, M = map(int, input().split())
board = list(list(map(int, input().split()))for _ in range(N))

def separateLand():
    d=deque()
    num=2
    for i in range(N):
        for j in range(M):
            if board[i][j]==1:
                d.append((i, j))
                board[i][j]=num
                while d:
                    ni, nj = d.popleft()
                    for k in range(4):
                        di, dj = ni+delta[0][k], nj+delta[1][k]
                        if -1 < di < N and -1 < dj < M and board[di][dj]==1:
                            d.append((di, dj))
                            board[di][dj]=num
                num+=1
    return num-2

def putBridge(landCount):
    E=[[] for _ in range(landCount)]
    for t in range(2,landCount+2):
        for i in range(N):
            for j in range(M):
                if board[i][j] == t:
                    for k in range(4):
                        di, dj = i+delta[0][k], j+delta[1][k]
                        if -1 < di < N and -1 < dj < M and not board[di][dj]:
                            count=0
                            while -1 < di < N and -1 < dj < M:
                                if board[di][dj]:
                                    if count > 1 and board[di][dj] != t:
                                        E[t-2].append((board[di][dj]-2,count))
                                    break
                                di+=delta[0][k]
                                dj+=delta[1][k]
                                count+=1
    if not E[0]:
        return -1
    pq = PriorityQueue()
    pq.put((0, 0))
    dijkstra = [1000 for _ in range(landCount)]
    while pq.qsize():
        cost, num = pq.get()
        if dijkstra[num]!=1000:
            continue
        dijkstra[num]=cost
        for node, c in E[num]:
            if dijkstra[node]==1000:
                pq.put((c, node))
    answer = sum(dijkstra)
    return answer if answer < 1000 else -1
    
landCount = separateLand()
print(putBridge(landCount))