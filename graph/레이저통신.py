from queue import PriorityQueue
delta = [[1, -1, 0, 0], [0, 0, 1, -1]]
dir = {'D':0, 'U':1, 'R':2, 'L':3}
M, N = map(int, input().split())
board = list(list(input()) for _ in range(N))
for i in range(N):
    for j in range(M):
        if board[i][j]=='C':
            si, sj = i, j
pq = PriorityQueue()
for k in range(4):
    i, j = si+delta[0][k], sj+delta[1][k]
    if -1 < i < N and -1 < j < M:
        if board[i][j] == '.':
            pq.put((0, i, j, k))
            board[i][j]=0
        elif board[i][j] == 'C':
            exit(print(0))
board[si][sj]=-1
tmp=10000
while True:
    c, i, j, d = pq.get()
    print(i,j)
    if tmp==c:
        exit(print(c))
    if board[i][j] < c:
        continue
    nd = [0,1]
    if d==0 or d==1:
        nd=[2,3]
    di, dj = i+delta[0][d], j+delta[1][d]
    for k in range(2):
        ti, tj = (i+delta[0][nd[k]], j+delta[1][nd[k]])
        if -1 < ti < N and -1 < tj < M:
            if board[ti][tj] == '.':
                pq.put((c+1, ti, tj, nd[k]))
                board[ti][tj]=c+1
            elif board[ti][tj] == 'C':
                tmp=c+1
    while -1 < di < N and -1 < dj < M:
        if board[di][dj]=='.':
            pq.put((c, di, dj, d))
            board[di][dj]=c
            for k in range(2):
                ti, tj = (di+delta[0][nd[k]], dj+delta[1][nd[k]])
                if -1 < ti < N and -1 < tj < M:
                    if board[ti][tj] == '.':
                        pq.put((c+1, ti, tj, nd[k]))
                        board[ti][tj]=c+1
                    elif board[ti][tj] == 'C':
                        for item in board:
                            print(*item)
                        tmp=c+1
        elif board[di][dj]=='C':
            exit(print(c))
        elif board[di][dj]!='*':
            if board[di][dj] > c:
                pq.put((c, di, dj, d))
                board[di][dj]=c
        else:
            break
        di+=delta[0][d]
        dj+=delta[1][d]