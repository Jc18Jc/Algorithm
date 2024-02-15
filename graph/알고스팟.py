from queue import PriorityQueue

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

m, n = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[True for _ in range(m)]for _ in range(n)]

pq = PriorityQueue()
pq.put((0, 0, 0))

while pq.qsize() > 0:
    v = pq.get()
    c, i, j =v[0], v[1], v[2]
    if i == n-1 and j == m-1:
        print(c)
        break
    if not visited[i][j]: continue
    visited[i][j]=False
    for k in range(4):
        ii, jj = i+di[k], j+dj[k]
        if -1 < ii < n and -1 < jj < m and visited[ii][jj]:
            if board[ii][jj]==1: pq.put((c+1, ii, jj))
            else: pq.put((c, ii, jj))


### 코드리뷰 ###
'''
import heapq

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
distance = [[1e10] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dijkstra(): # 다익스트라로 접근, 나도 우선순위큐 쓰면서 최단거리 찾아가는 거라 다익스트라 느낌이긴 함
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0 # 처음에 나도 코스트 저장하는 식으로 했는데, 어짜피 힙에 정보가 다 있어서 굳이? False, True로 충분
    while q:
        cost, r, c = heapq.heappop(q)

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if cost + arr[nr][nc] < distance[nr][nc]: # 다익스트라에선 필수적인 과정인데, 해당 문제는 먼저 뽑힌게 무조건 최단 거리라 방문체크만
                distance[nr][nc] = cost + arr[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))


dijkstra()
print(distance[N - 1][M - 1])
'''

### 숏코딩 코드 리뷰 ###
'''
from heapq import*
R=range
c,r=map(int,input().split())
m=[[*map(int,input())]for i in R(r)] # [*map(int, input())] = list(map(int, input()))
q=[[0,0,0]]
while q:
    b,x,y=heappop(q)
    if (x,y)==(r-1,c-1):print(b);break # (x,y)==(r-1,c-1) = x==r-1 and y==c-1
    for i,j in((0,1),(1,0),(0,-1),(-1,0)): # di, dj 설정안하고 for in 으로 네 가지 넣어주기
        nx,ny=x+i,y+j
        if 0<=nx<r and 0<=ny<c and m[nx][ny]<2:heappush(q,[b+m[nx][ny],nx,ny]);m[nx][ny]=2 # visited 배열 없이 맵에 바로 표시
'''