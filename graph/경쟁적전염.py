import sys
input=sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
numArray = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        numArray[board[i][j]].append((i,j))

d=deque()
for i in range(1, K+1):
    for x, y in numArray[i]:
        d.append((x,y,0))

while d:
    x,y,s=d.popleft()
    if s==S:
        break
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if -1 < nx < N and -1 < ny < N and not board[nx][ny]:
            board[nx][ny]=board[x][y]
            d.append((nx,ny,s+1))

print(board[X-1][Y-1])


### 코드리뷰 ###
'''
from collections import deque
 
N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      virus.append(((graph[i][j], i, j))) # 이렇게 입력받을 때 값까지 같이 넣어서 정렬해주면 더 편하겠구나
S, X, Y = map(int, input().split())
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(s, X, Y):
  q = deque(virus) # 데크화 하기도 편하네 인정
  count = 0
  while q:
    if count == s:
      break
    for _ in range(len(q)): # q를 pop하고 append하는데 len을 써도 되나 ? 된다해도 데크에 count 요소 추가하는게 나을 듯
      prev, x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], nx, ny))
    count += 1
  return graph[X-1][Y-1]
 
virus.sort()
print(bfs(S, X, Y))

'''