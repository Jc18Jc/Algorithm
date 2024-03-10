import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
visited=[[k+1 for _ in range(m)] for _ in range(n)]
board = [list(map(int, input().strip())) for _ in range(n)]
d=deque()
delta=[[1, -1, 0, 0], [0, 0, 1, -1]]

def bfs():
    d.append((0, 0, 0, 1))
    visited[0][0]=0
    while d:
        i, j, w, c= d.popleft()
        if (i, j) == (n-1, m-1):
            return c
        for t in range(4):
            di, dj = i+delta[0][t], j+delta[1][t]
            if -1 < di < n and -1 < dj < m:
                if visited[di][dj] <= w+board[di][dj]:
                    continue
                d.append((di, dj, w+board[di][dj], c+1))
                visited[di][dj] = w+board[di][dj]
                    
    return -1

print(bfs())


### 코드리뷰 ###
'''
from collections import deque
q = deque()
from sys import stdin
input = stdin.readline

n,m,k = map(int, input().split())
vis = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]
arr = [list(map(int,input().strip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q.append([0,0,k])
    vis[0][0][k] = 1
    while q :
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for i in range(4) :
            nx ,ny = dx[i] + x, dy[i]+y
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny]==1 and z>0 and vis[nx][ny][z-1]==0: # 벽 뚫은 횟수로 3차원 확장하면 왔던 길 또 갈 것 같은데
                    vis[nx][ny][z-1] = vis[x][y][z]+1
                    q.append([nx,ny,z-1])
                elif arr[nx][ny]==0 and vis[nx][ny][z]==0:
                    vis[nx][ny][z] = vis[x][y][z]+1
                    q.append([nx,ny,z]) 
    return -1

print(bfs())

'''