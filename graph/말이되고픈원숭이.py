import sys
ssr = sys.stdin.readline
from collections import deque
dih = [2, 1, 2, 1, -2, -1, -2, -1]
djh = [1, 2, -1, -2, 1, 2, -1, -2]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
k = int(ssr())
w, h = map(int, ssr().split())
board = []

for _ in range(h):
    board.append(list(map(int, ssr().split())))
q = deque()
q.append((0, 0, k, 0))

visited = [[0 for _ in range(w)] for _ in range(h)]

while q:
    i, j, jump, c= q.popleft()
    if i==h-1 and j==w-1:
        exit(print(c))
    if jump:
        for t in range(8):
            ti = i+dih[t]
            tj = j+djh[t]
            if -1 < ti < h and -1 < tj < w and not board[ti][tj]:
                if visited[ti][tj] < jump:
                    q.append((ti, tj, jump-1, c+1))
                    visited[ti][tj]=jump
    for t in range(4):
        ti = i+di[t]
        tj = j+dj[t]
        if -1 < ti < h and -1 < tj < w and not board[ti][tj]:
             if visited[ti][tj] < jump+1:  
                q.append((ti, tj, jump, c+1))
                visited[ti][tj]=jump+1

print(-1)