import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
answer = 0

def bfs(i, j):
    q = deque()
    visited=[[True for _ in range(m)] for _ in range(n)]
    q.append([i,j, 0])
    visited[i][j]=False
    v=None
    while q:
        v = q.popleft()
        for k in range(4):
            ik = v[0]+di[k]
            jk = v[1]+dj[k]
            if -1 < ik < n and -1 < jk < m and visited[ik][jk] and board[ik][jk]=='L':
                q.append([ik, jk, v[2]+1])
                visited[ik][jk]=False
    return v[2]

for i in range(n):
    for j in range(m):
        if board[i][j]=='L':
            answer = max(bfs(i, j), answer)
print(answer)



### 코드 리뷰 ###
# 내 코드는 python은 실패 pypy는 통과하는 코드임
# 최대 가능한 시간을 한 번 찍으면 브레이크 거는 식으로 하면 통과 된다는데 굳이 그렇게 해야 하나 싶음
# 근데 이 코드는 python도 통과해서 확인해보려고 함
# 코드 리뷰 참고해서 함수화의 차이만 있다고 느껴져 함수화 해봤는데 아까보다 채점은 많이 됐음, 시간초과 여전, 함수화하고 어떤 부분이 시간에 영향을 미쳤을까
'''

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

max_time = -1e9

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b,t): # bfs의 함수화, 깔끔하긴 한 듯 참고
    q = deque()
    q.append((a,b,t))
    visited[a][b] = True
    while q:
        x,y,time = q.popleft()
        if t < time:    # 최대값이 나왔을 때 갱신해주려고 매번 비교, 이건 오히려 마이너스 일 것 같은데 ?
            t = time
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 'L':
                    visited[nx][ny] = True
                    q.append((nx,ny,time+1))
    return t

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            max_time = max(max_time, bfs(i,j,0))

print(max_time)

'''