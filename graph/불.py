import sys
from collections import deque
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

board = []
fire = []
starti = 0
startj = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(n):
    l = list(ssr().strip())
    for j in range(m):
        if l[j]=='F':
            fire.append((i,j))
        elif l[j]=='J':
            starti=i
            startj=j
    board.append(l)

d = deque()

for i in range(len(fire)):
    d.append((fire[i][0], fire[i][1], 0, 1))
d.append((starti, startj, 0, 0))

while d:
    v=d.popleft()
    for k in range(4):
        ti = v[0]+di[k]
        tj = v[1]+dj[k]
        if not v[3] and (ti < 0 or ti >= n or tj < 0 or tj >= m):
            exit(print(v[2]+1))
        if -1 < ti < n and -1 < tj < m and board[ti][tj]=='.':
            d.append((ti, tj, v[2]+1, v[3]))
            board[ti][tj]='#'

print('IMPOSSIBLE')

