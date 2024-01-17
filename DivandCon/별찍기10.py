n = int(input())

board = [[' ' for _ in range(n)] for _ in range(n)]

def recur(i, j, num):
    if num == 3:
        board[i][j]='*'
        board[i+1][j]='*'
        board[i+2][j]='*'
        board[i][j+1]='*'
        board[i][j+2]='*'
        board[i+1][j+2]='*'
        board[i+2][j+1]='*'
        board[i+2][j+2]='*'
        return
    t=num//3
    recur(i,j, t)
    recur(i+t,j, t)
    recur(i+2*t,j, t)
    recur(i,j+t, t)
    recur(i,j+2*t, t)
    recur(i+t,j+2*t, t)
    recur(i+2*t,j+t, t)
    recur(i+2*t,j+2*t, t)

recur(0, 0, n)

for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()