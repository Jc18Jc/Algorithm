import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
INF=10000

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n, m = map(int, ssr().split())

board = []
birus=[]
wl=0
for i in range(n):
    l = list(map(int, ssr().split()))
    for j in range(n):
        if l[j]==2:
            birus.append([i,j])
        if l[j]==0:
            wl+=1
    board.append(l)

def dfs(index, count, bl):
    if count == m:
        bl.append(birus[index])
        d = deque()
        visited = [[True for _ in range(n)] for _ in range(n)]
        wc = 0
        for item in bl:
            d.append((item, 0))
        while d:
            v = d.popleft()
            i = v[0][0]
            j = v[0][1]
            for k in range(4):
                ii = i+di[k]
                jj = j+dj[k]
                if -1 < ii < n and -1 < jj < n and visited[ii][jj]:
                    if board[ii][jj]==0:
                        wc+=1
                        d.append(((ii,jj), v[1]+1))
                        visited[ii][jj]=False
                        if wc==wl:
                            return v[1]+1 
                    elif board[ii][jj] == 2:
                        d.append(((ii,jj), v[1]+1))
                        visited[ii][jj]=False
        return INF 
    minCount = INF
    for k in range(index+1, len(birus)):
        tmp = dfs(k, count+1, bl+[birus[index]])
        minCount = min(tmp, minCount)
    return minCount

if wl == 0:
    exit(print(0))

minC = INF
for k in range(len(birus)):
    minC = min(dfs(k, 1, []), minC)

if minC == INF:
    print(-1)
else:
    print(minC)