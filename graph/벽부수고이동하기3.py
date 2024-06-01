import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
visited=[[k+1 for _ in range(m)] for _ in range(n)]
duplication = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
d=deque()
delta=[[1, -1, 0, 0], [0, 0, 1, -1]]
board = [list(map(int, input().strip())) for _ in range(n)]

def bfs():
    d.append((0, 0, 0, 1))
    visited[0][0]=0
    while d:
        i, j, w, c= d.popleft()
        if (i, j) == (n-1, m-1):
            return c
        if not duplication[i][j][w]:
            duplication[i][j][w]=True
            d.append((i, j, w, c+1))
        for t in range(4):
            di, dj = i+delta[0][t], j+delta[1][t]
            if -1 < di < n and -1 < dj < m:
                if visited[di][dj] <= w+board[di][dj]:
                    continue
                if board[di][dj] and not c%2:
                    continue
                d.append((di, dj, w+board[di][dj], c+1))
                visited[di][dj] = w+board[di][dj]
    return -1

print(bfs())