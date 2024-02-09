import sys
input=sys.stdin.readline
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

ch = 2
q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=ch
            q.append((i,j))
            while q:
                v=q.popleft()
                for k in range(4):
                    ik = v[0]+di[k]
                    jk = v[1]+dj[k]
                    if -1 < ik < n and -1 < jk < n and board[ik][jk]==1:
                        board[ik][jk]=ch
                        q.append((ik, jk))
            ch+=1

checkSea = []

for i in range(n):
    for j in range(n):
        if not board[i][j]:
            for k in range(4):
                ik = i+di[k]
                jk = j+dj[k]
                if -1 < ik < n and -1 < jk < n and board[ik][jk]:
                    checkSea.append((i, j, board[ik][jk]))

visited = [[True for _ in range(n)] for _ in range(n)]

answer = 200

for t in range(len(checkSea)):
    i=checkSea[t][0]
    j=checkSea[t][1]
    l=checkSea[t][2]
    if not visited[i][j]:
        continue
    q.append((i, j, 1))
    visited2 = [[True for _ in range(n)] for _ in range(n)]
    visited[i][j]=False
    visited2[i][j]=False
    
    while q:
        v=q.popleft()
        for k in range(4):
            ik = v[0]+di[k]
            jk = v[1]+dj[k]
            if -1 < ik < n and -1 < jk < n:
                if not board[ik][jk] and visited2[ik][jk]:
                    visited2[ik][jk]=False
                    q.append((ik, jk, v[2]+1))
                if board[ik][jk] and board[ik][jk]!=l:
                    answer=min(answer, v[2])
                    q.clear()
print(answer)
            
        

### 코드 리뷰 ###
'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs1(i, j):  # 섬체크 함수, 함수화는 습관들여야겠다
    global count
    q = deque()
    q.append([i, j])
    vis[i][j] = True
    arr[i][j] = count # 나는 보드에다가 바로 섬마다 숫자 넣어놨는데 새로 배열 만들었음, vis나 새로운 배열의 자원 소모가 있을 듯

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                arr[nx][ny] = count
                q.append([nx, ny])

def bfs2(z): # 최단거리 함수
    global answer
    @visited 대신 dist로 거리 표시 겸 방문 체크도 했는데 깔끔하진 못한 듯 ? 나는 큐에 한 번에 코스트까지 넘겼으면 하는데 뭐가 보편적인지는 잘 ..
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    # 나는 육지가 옆에 있는 바다로 잡고 시작했는데 여기는 하나의 육지를 통째로 큐에 담음, 뭐가 이득일지는 상황에 따라 다를 듯
    for i in range(n):
        for j in range(n):
            if arr[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 왜 and 두개로 안쓰고 .. ?
                continue
            if arr[nx][ny] > 0 and arr[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            bfs1(i, j)
            count += 1

# print(arr)

for i in range(1, count):
    bfs2(i)

print(answer)
'''