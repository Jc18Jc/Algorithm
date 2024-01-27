import sys
ssr= sys.stdin.readline

n, m, x, y, k = map(int, ssr().split())

board = []

for _ in range(n):
    board.append(list(map(int, ssr().split())))
order = list(map(int, ssr().split()))

dice = [0 for _ in range(6)]

bottom = 0

def roll(o, i, j):
    flag=False
    if o == 1 and j < m-1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
        j+=1
        flag=True
    elif o == 2 and j > 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
        j-=1
        flag=True
    elif o == 3 and i > 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
        i-=1
        flag=True
    elif o == 4 and i < n-1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        i+=1
        flag=True
    if flag:
        if board[i][j]==0:
            board[i][j]=dice[0]
        else:
            dice[0]=board[i][j]
            board[i][j]=0
        print(dice[5])
    return i, j
    
for o in range(k):
    x, y = roll(order[o], x, y)