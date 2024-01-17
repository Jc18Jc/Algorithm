import sys
ssr = sys.stdin.readline
from collections import deque

n, m = map(int, ssr().split())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

board = []
water=[[[0, 0] for _ in range(m)] for _ in range(n)]
ice = []

for i in range(n):
    l =list(map(int, ssr().split()))
    for j in range(m):
        if l[j]==0:
            for k in range(4):
                ip = i+di[k]
                jp = j+dj[k]
                if -1 < ip < n and -1 < jp < m:
                    water[ip][jp][0]+=1
        else:
            ice.append((i, j))
    board.append(l)
                    
answer = 0
rem = 0
while True:
    q = deque()
    visited = [[True for _ in range(m)] for _ in range(n)]
    count=0
    removeIndex=[]
    tmprem=0
    if not (len(ice)-rem):
        print(0)
        break
    for i, j in ice:
        if board[i][j]>0:
            q.append((i, j))
            visited[i][j]=False
            break
    while q:
        v=q.popleft()
        board[v[0]][v[1]]-=water[v[0]][v[1]][0]
        if board[v[0]][v[1]] <= 0:
            tmprem += 1
        count+=1
        for k in range(4):
            ip = v[0]+di[k]
            jp = v[1]+dj[k]
            if -1 < ip < n and -1 < jp < m:
                if board[v[0]][v[1]]<=0:
                    water[ip][jp][1]+=1
                if board[ip][jp] > 0 and visited[ip][jp]:
                    q.append((ip, jp))
                    visited[ip][jp]=False
    if len(ice)-rem != count:
        print(answer)
        break
    rem+=tmprem
    for i, j in ice:
        water[i][j][0] += water[i][j][1]
        water[i][j][1] = 0
    answer+=1