N,M,R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board2 = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(min(N,M)//2):
    r=R%((N-i*2)*2+(M-i*2)*2-4)
    for j in range(i, M-i):
        if r-j+i < 0:
            board2[i][j-r]=board[i][j]
            board2[N-i-1][M-j-1+r]=board[N-i-1][M-j-1]
            continue
        if r-j+i < N-i:
            board2[i][j-r]=board[r-j+2*i-N][i]
            board2[N-i-1][M-j-1+r]=board[N-1+r-j][M-i-1]
            continue
        if r-j-N+3*i < M-i:
            board2[i][j-r]=board[r-j-N+4*i-M][i]
            board2[N-i-1][M-j-1+r]=board[i][M-i-1]
            continue