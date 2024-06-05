from collections import deque
delta = [[0, 0, 1, -1], [1, -1, 0, 0]]
N,M,T = map(int, input().split())
board=list(list(map(int, input().split())) for _ in range(N))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0]=True
d=deque()
d.append((0, 0, 0, False))
answer = T+1
while d:
    i, j, t, flag = d.popleft()
    if t==T+1:
        break
    if i==N-1 and j==M-1:
        exit(print(t if answer > t else answer))
    for k in range(4):
        di, dj = i+delta[0][k], j+delta[1][k]
        flag2 = flag
        if -1 < di < N and -1 < dj < M and not visited[di][dj]:
            if board[di][dj]==2:
                flag2=True
                answer = t+1+M-1-dj+N-1-di
            if board[di][dj]==1:
                if not flag:
                    continue
            d.append((di, dj, t+1, flag2))
            visited[di][dj]=True
print('Fail' if answer > T else answer)