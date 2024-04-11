import sys
input = sys.stdin.readline
from collections import deque
delta = ((1, -1, 0, 0), (0, 0, 1, -1))

N, M = map(int, input().split())
board=[]
for i in range(N):
    l=list(input().strip())
    for j in range(M):
        l[j]=int(l[j])
    board.append(l)
parents = [[(y, x) for x in range(M)] for y in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]

def bfs(si, sj):
    d=deque()
    d.append((si, sj))
    visited[si][sj]=True
    c=0
    while d:
        i, j = d.popleft()
        c+=1
        for k in range(4):
            ni, nj = i+delta[0][k], j+delta[1][k]
            if -1 < ni < N and -1 < nj < M and not visited[ni][nj] and not board[ni][nj]:
                parents[ni][nj]=(si, sj)
                visited[ni][nj]=True
                d.append((ni, nj))
    count[si][sj]=c

def checkRoot(i, j):
    s=set()
    for k in range(4):
        ni, nj = i+delta[0][k], j+delta[1][k]
        if -1 < ni < N and -1 < nj < M and not board[ni][nj]:
            s.add(parents[ni][nj])
    total=1
    for pi, pj in s:
        total+=count[pi][pj]
    return total


visited=[[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and not board[i][j]:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if board[i][j]:
            print(checkRoot(i,j)%10, end='')
        else:
            print(0, end='')
    print()

### 코드리뷰 ###
# 코드 구조가 나랑 너무 비슷하다
'''
from collections import deque
input = __import__('sys').stdin.readline # 이런 신박한 방법도 있네 알수록 놀라운 파이썬 ,,

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10
# 이렇게 배열에 저장해서 join으로 출력하는 것도 괜찮은데 생각이 안나네
for g in graph:
    print("".join(map(str, g)))
'''