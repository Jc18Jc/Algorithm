N,M,R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for i in range(min(N,M)//2):
    r=R%((N-i*2)*2+(M-i*2)*2-4)
    tmp = board[i][i:M-i]
    for j in range(i+1, N-i):
        tmp.append(board[j][M-i-1])
    for j in range(M-2-i, i-1, -1):
        tmp.append(board[N-i-1][j])
    for j in range(N-i-2, i, -1):
        tmp.append(board[j][i])
    tmp = tmp[r:]+tmp[:r]
    k=0
    for j in range(i, M-i):
        board[i][j]=tmp[k]
        k+=1
    for j in range(i+1, N-i):
        board[j][M-1-i]=tmp[k]
        k+=1
    for j in range(M-2-i, i-1, -1):
        board[N-1-i][j]=tmp[k]
        k+=1
    for j in range(N-2-i, i, -1):
        board[j][i]=tmp[k]
        k+=1

for item in board:
    print(*item)