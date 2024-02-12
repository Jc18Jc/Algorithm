import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

board = []

for i in range(3*n):
    board.append(list(ssr().strip()))

for i in range(n):
    for j in range(m):
        tmp=5
        answer=False
        if board[i*3+1][8*j+6].isdigit():
            tmp+=1
        if int(board[i*3+1][8*j+1])+int(board[i*3+1][8*j+3]) == int(''.join(board[i*3+1][8*j+5:8*j+tmp+1])):
            answer=True
        if answer:
            for k in range(tmp):
                board[i*3][8*j+k+1]='*'
                board[i*3+2][8*j+k+1]='*'
                board[i*3+1][8*j]='*'
                board[i*3+1][8*j+tmp+1]='*'
        else:
            board[i*3+2][8*j+1]='/'
            board[i*3+1][8*j+2]='/'
            board[i*3][8*j+3]='/'

for item in board:
    for item2 in item:
        print(item2, end='')
    print()