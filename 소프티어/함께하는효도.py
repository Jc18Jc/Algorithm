import sys

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
route=[[[] for _ in range(m)] for _ in range(4)]

answer = 0

def checkValid(x, y, n):
  return x > -1 and x < n and y > -1 and y < n

def dfs(x, y, count, value, who):
  global answer

  if count == 3:
    if who == m-1:
      answer = max(answer, value)
    else:
      dfs(route[0][who+1][0], route[0][who+1][1], 0, value, who+1)
    return
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if checkValid(nx, ny, n):
      for j in range(who):
        if [nx, ny] in route[count+1][j]:
          break
      else:
        newValue = value+board[nx][ny] if not visited[nx][ny] else value
        visited[nx][ny]+=1
        route[count+1][who].append(nx)
        route[count+1][who].append(ny)
        dfs(nx, ny, count+1, newValue, who)
        route[count+1][who]=[]
        visited[nx][ny]-=1

value=0
for i in range(m):
  x, y = map(int, input().split())
  route[0][i].append(x-1)
  route[0][i].append(y-1)
  value += board[x-1][y-1]
  visited[x-1][y-1]+=1
dfs(route[0][0][0], route[0][0][1], 0, value, 0)
print(answer)