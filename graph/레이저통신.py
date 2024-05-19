from collections import deque
delta = [[1, -1, 0, 0], [0, 0, 1, -1]]
M, N = map(int, input().split())
board = list(list(input()) for _ in range(N))
ci = []
cj = []
for i in range(N):
    for j in range(M):
        if board[i][j]=='C':
            ci.append(i)
            cj.append(j)
visited = [[[10000 for _ in range(4)] for _ in range(M)] for _ in range(N)]
d = deque()
for k in range(4):
    visited[ci[0]][cj[0]][k]=0
    i, j = ci[0]+delta[0][k], cj[0]+delta[1][k]
    if -1 < i < N and -1 < j < M and board[i][j]=='.':
        if board[i][j]=='.':
            d.append((i,j,k,0))
        elif board[i][j]=='C':
            exit(print(0))
while d:
    i, j, t, c=d.popleft()
    di, dj = i, j
    nd = [0, 1]
    if t==0 or t==1: nd=[2, 3]
    while -1 < di < N and -1 < dj < M:
        if visited[di][dj][t] <= c or board[di][dj]=='*':
            break
        visited[di][dj][t]=c
        for k in range(2):
            dir=nd[k]
            ti, tj = di+delta[0][dir], dj+delta[1][dir]
            if -1 < ti < N and -1 < tj < M:
                if (board[ti][tj]=='.' or board[ti][tj]=='C') and visited[ti][tj][t] > c+1:
                    d.append((ti, tj, dir, c+1))
        di+=delta[0][t]
        dj+=delta[1][t]

print(min(visited[ci[1]][cj[1]]))