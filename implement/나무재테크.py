import sys
from collections import deque
ssr = sys.stdin.readline


n, m, k = map(int, ssr().split())
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

A = []
board = [[5 for _ in range(n)] for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    A.append(list(map(int, ssr().split())))

for _ in range(m):
    x, y, z = map(int, ssr().split())
    tree[x-1][y-1].append(z)

for i in range(n):
    for j in range(n):
        tree[i][j] = deque(sorted(tree[i][j]))

for _ in range(k):
    for i in range(n):
        for j in range(n):
            for t in range(len(tree[i][j])):
                if board[i][j] >= tree[i][j][t]:
                    board[i][j]-=tree[i][j][t]
                    tree[i][j][t]+=1
                else:
                    h = len(tree[i][j])-t 
                    for _ in range(h):
                        board[i][j]+=(tree[i][j].pop()//2)
                    break
                    
    for i in range(n):
        for j in range(n):
            board[i][j]+=A[i][j]
            for item in tree[i][j]:
                if item%5 == 0:
                    for t in range(8):
                        ti = i+di[t]
                        tj = j+dj[t]
                        if -1< ti < n and -1 < tj < n:
                            tree[ti][tj].appendleft(1)

count=0
for i in range(n):
    for j in range(n):
        count+=len(tree[i][j])
print(count)