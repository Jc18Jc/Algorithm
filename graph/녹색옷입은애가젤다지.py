import sys
input = sys.stdin.readline
from queue import PriorityQueue

delta = [[0,0,1,-1], [1,-1,0,0]]

def dijkstra():
    pq=PriorityQueue()
    pq.put((board[0][0],0,0))
    k = [[10**6 for _ in range(n)] for _ in range(n)]
    while True:
        c, i, j = pq.get()
        if (i,j) == (n-1, n-1): return c
        for t in range(4):
            ni = i+delta[0][t]
            nj = j+delta[1][t]
            if -1 < ni < n and -1 < nj < n and k[ni][nj] > c+board[ni][nj]:
                pq.put((c+board[ni][nj],ni,nj))
                k[ni][nj]=c+board[ni][nj]

p=1
while True:
    n = int(input())
    if n == 0: break
    board = [list(map(int, input().split())) for _ in range(n)]
    print('Problem',p, end='')
    print(':',dijkstra())
    p+=1


### 코드리뷰 ###
# 나랑 거의 똑같아서 리뷰할게 없음, 코드 좀 길어지더라도 깔끔하게 new_cost처럼 표시한다는 정도 ?
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = cost + graph[new_x][new_y]
                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    dijkstra()
    count += 1

'''