from collections import deque

HORIZON = 0
VERTICAL = 1

N = int(input())

board = list(list(input()) for _ in range(N))

s = []
e = []

for i in range(N):
  for j in range(N):
    if board[i][j] == 'B':
      s.append((i,j))
    elif board[i][j] == 'E':
      e.append((i,j))

visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]

state = HORIZON if s[0][0] == s[1][0] else VERTICAL

d = deque()
d.append((s[0], s[1], s[2], state, 0))
visited[state][s[0][0]][s[0][1]] = True

while d:
  l1, l2, l3, s, cost = d.popleft()
  
  if l1 == e[0] and l2 == e[1] and l3 == e[2]:
    exit(print(cost))

  if l1[0] > 0 and not visited[s][l1[0]-1][l1[1]]:
    if board[l1[0]-1][l1[1]] != '1' and board[l2[0]-1][l2[1]] != '1' and board[l3[0]-1][l3[1]] != '1':
      d.append(((l1[0]-1, l1[1]), (l2[0]-1, l2[1]), (l3[0]-1, l3[1]), s, cost+1))
      visited[s][l1[0]-1][l1[1]] = True
      
  if l3[0] < N-1 and not visited[s][l1[0]+1][l1[1]]:
    if board[l1[0]+1][l1[1]] != '1' and board[l2[0]+1][l2[1]] != '1' and board[l3[0]+1][l3[1]] != '1':
      d.append(((l1[0]+1, l1[1]), (l2[0]+1, l2[1]), (l3[0]+1, l3[1]), s, cost+1))
      visited[s][l1[0]+1][l1[1]] = True
  
  if l1[1] > 0 and not visited[s][l1[0]][l1[1]-1]:
    if board[l1[0]][l1[1]-1] != '1' and board[l2[0]][l2[1]-1] != '1' and board[l3[0]][l3[1]-1] != '1':
      d.append(((l1[0], l1[1]-1), (l2[0], l2[1]-1), (l3[0], l3[1]-1), s, cost+1))
      visited[s][l1[0]][l1[1]-1] = True

  if l3[1] < N-1 and not visited[s][l1[0]][l1[1]+1]:
    if board[l1[0]][l1[1]+1] != '1' and board[l2[0]][l2[1]+1] != '1' and board[l3[0]][l3[1]+1] != '1':
      d.append(((l1[0], l1[1]+1), (l2[0], l2[1]+1), (l3[0], l3[1]+1), s, cost+1))
      visited[s][l1[0]][l1[1]+1] = True

  if s==HORIZON and l1[0] > 0 and l1[0] < N-1 and not visited[VERTICAL][l1[0]-1][l1[1]+1]:
    flag = True
    for k in range(-1, 2):
      for t in range(-1, 2):
        if board[l2[0]+k][l2[1]+t] == '1':
          flag=False
          break
    if flag:
      d.append(((l1[0]-1, l1[1]+1), (l2[0], l2[1]), (l3[0]+1, l3[1]-1), VERTICAL, cost+1))
      visited[VERTICAL][l1[0]-1][l1[1]+1] = True

  if s==VERTICAL and l1[1] > 0 and l1[1] < N-1 and not visited[HORIZON][l1[0]+1][l1[1]-1]:
    flag = True
    for k in range(-1, 2):
      for t in range(-1, 2):
        if board[l2[0]+k][l2[1]+t] == '1':
          flag=False
          break
    if flag:
      d.append(((l1[0]+1, l1[1]-1), (l2[0], l2[1]), (l3[0]-1, l3[1]+1), HORIZON, cost+1))
      visited[HORIZON][l1[0]+1][l1[1]-1] = True

print(0)