import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
que = deque()
fade = []
hours = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def countOutsideAir(x, y):
    count = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 2:
            count += 1

    return count

def denoteOutsideAir(x, y):
    tmp_que = deque()
    tmp_que.append([x, y])
    while tmp_que:
        v = tmp_que.popleft()
        for k in range(4):
            nx, ny = dx[k]+v[0], dy[k]+v[1]
            if -1 < nx < n and -1 < ny < m and not cheese[nx][ny]:
                cheese[nx][ny]=2
                tmp_que.append([nx, ny])

denoteOutsideAir(0, 0)
que.append([0, 0])
visited[0][0]=True
while True:
    fade = []

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] == 1 and countOutsideAir(nx, ny) > 1:
                    fade.append([nx, ny])
                    visited[nx][ny] = True
                elif cheese[nx][ny] != 1:
                    que.append([nx, ny])
                    visited[nx][ny] = True

    if not fade:
        print(hours)
        break

    for f in fade:
        que.append(f)
        cheese[f[0]][f[1]] = 2
        denoteOutsideAir(f[0], f[1])
    hours += 1