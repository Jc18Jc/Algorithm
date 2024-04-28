import sys
input = sys.stdin.readline
from collections import deque
delta = ((1,-1,0,0,0,0),(0,0,1,-1,0,0),(0,0,0,0,1,-1))

def bfs(s, e):
    d=deque()
    d.append((s, 0))
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[s[0]][s[1]][s[2]]=True
    while d:
        v=d.popleft()
        if v[0]==e:
            print('Escaped in', v[1], 'minute(s).')
            return
        i,j,k = v[0]
        for t in range(6):
            ni, nj, nk = i+delta[0][t], j+delta[1][t], k+delta[2][t]
            if -1 < ni < L and -1 < nj < R and -1 < nk < C and not visited[ni][nj][nk] and (board[ni][nj][nk]=='.' or board[ni][nj][nk]=='E'):
                d.append(((ni, nj, nk), v[1]+1))
                visited[ni][nj][nk]=True
    print('Trapped!')    

while True:
    L,R,C=map(int, input().split())
    if not (L or R or C):
        break
    board=[[[] for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            tmp = list(input().strip())
            board[i][j]=tmp
            for k in range(C):
                if tmp[k]=='S':
                    s=(i,j,k)
                if tmp[k]=='E':
                    e=(i,j,k)
        input()
    bfs(s, e)