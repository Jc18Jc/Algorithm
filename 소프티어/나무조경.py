N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
pick = [[False for _ in range(N)] for _ in range(N)]

answer = 0

def checkValid(x, y):
  return x > -1 and x < N and y > -1 and y < N and not pick[x][y]

def bt(count, value):
  global answer

  if count == 4:
    answer = max(answer, value)
    return
  flag=False
  for i in range(N):
    for j in range(N):
      if not pick[i][j]:
        for k in  range(4):
          ni, nj = i+di[k], j+dj[k]
          if checkValid(ni, nj):
            pick[i][j]=True
            pick[ni][nj]=True
            bt(count+1, value+board[i][j]+board[ni][nj])
            pick[i][j]=False
            pick[ni][nj]=False
            flag=True
  if not flag:
    answer = max(answer, value)

bt(0, 0)

print(answer)