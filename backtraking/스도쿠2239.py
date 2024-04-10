import sys
ssr =sys.stdin.readline

board = [list(ssr()) for _ in range(9)]
ga = [[False for _ in range(10)] for _ in range(9)]
se = [[False for _ in range(10)] for _ in range(9)]
ne = [[False for _ in range(10)] for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        board[i][j]=int(board[i][j])

for i in range(9):
    for j in range(9):
        ga[i][board[i][j]]=True
        se[j][board[i][j]]=True
        if i < 3:
            ne[j//3][board[i][j]]=True
        elif i < 6:
            ne[j//3+3][board[i][j]]=True
        else:
            ne[j//3+6][board[i][j]]=True
        if board[i][j]==0:
            zero.append((i, j))

def bt(n):
    if n == len(zero):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        return 1
    i = zero[n][0]
    j = zero[n][1]
    nei=0
    if i < 3:
        nei = j//3
    elif i < 6:
        nei = j//3+3
    else:
        nei = j//3+6
    
    for k in range(1, 10):
        if not ga[i][k] and not se[j][k] and not ne[nei][k]:
            ga[i][k]=True
            se[j][k]=True
            ne[nei][k]=True
            board[i][j]=k
            result=bt(n+1)
            if result==1:
                return 1
            ga[i][k]=False
            se[j][k]=False
            ne[nei][k]=False
            board[i][j]=0
    return 0

bt(0)