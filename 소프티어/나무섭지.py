from collections import deque

n, m = map(int, input().split())
board = [[] for _ in range(n)]
ghostList = []
sx = sy = ex = ey = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
hVisited = [[False for _ in range(m)] for _ in range(n)]


d = deque()

for i in range(n):
  l = list(input().strip())
  for j in range(m):
    if l[j] == 'G':
      ghostList.append((i, j))
    elif l[j] == 'N':
      sx, sy = i, j
    elif l[j] == 'D':
      ex, ey = i, j
  board[i]=l

for (x, y) in ghostList:
  d.append((1, x, y))
  visited[x][y]=True
d.append((0, sx, sy))
hVisited[sx][sy]=True

def checkValid(x, y, n, m):
  return x > -1 and x < n and y > -1 and y < m

while d:
  w, x, y = d.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if checkValid(nx, ny, n, m):
      if visited[nx][ny]:
          continue
      if w == 1:
        visited[nx][ny] = True
      if w == 0:
        if hVisited[nx][ny]:
          continue
        if nx == ex and ny == ey:
          exit(print('Yes'))
        if board[nx][ny] != '.':
          continue
        hVisited[nx][ny] = True
      d.append((w, nx, ny))

print('No')