import sys
ssr = sys.stdin.readline

n = int(ssr())

board = [[False for _ in range(1001)] for _ in range(1001)]
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
cross = [[[False for _ in range(4)] for _ in range(1001)] for _ in range(1001)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, ssr().split())
    board[x2+500][y2+500]=True
    board[x2+500][y1+500]=True
    board[x1+500][y1+500]=True
    for i in range(x1+500, x2+500):
        board[i][y1+500]=True
        cross[i][y1+500][2]=True
        cross[i+1][y1+500][3]=True
        board[i][y2+500]=True
        cross[i][y2+500][2]=True
        cross[i+1][y2+500][3]=True
    for i in range(y1+500, y2+500):
        board[x1+500][i]=True
        cross[x1+500][i][1]=True
        cross[x1+500][i+1][0]=True
        board[x2+500][i]=True
        cross[x2+500][i][1]=True
        cross[x2+500][i+1][0]=True

count = 0

i, j = 500, 500
if board[i][j]:
    q = [(i, j)]
    board[i][j]=False
    while q:
        v=q.pop()
        for k in range(4):
            ti = v[0]+di[k]
            tj = v[1]+dj[k]
            if -1<ti<1001 and -1<tj<1001 and board[ti][tj] and cross[ti][tj][k]:
                board[ti][tj]=False
                q.append((ti, tj))


for i in range(1001):
    for j in range(1001):
        if board[i][j]:
            q=[(i, j)]
            board[i][j]=False
            count+=1
            while q:
                v=q.pop()
                for k in range(4):
                    ti = v[0]+di[k]
                    tj = v[1]+dj[k]
                    if -1<ti<1001 and -1<tj<1001 and board[ti][tj] and cross[ti][tj][k]:
                        board[ti][tj]=False
                        q.append((ti, tj))

print(count)