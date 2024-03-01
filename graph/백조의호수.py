import sys
input = sys.stdin.readline
from collections import deque
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def union(p1, p2):
    p1=find(p1)
    p2=find(p2)
    if p1 != p2:
        if p1 < p2:  parents[p2[0]][p2[1]]=p1
        else: parents[p1[0]][p1[1]]=p2

def find(p1):
    if parents[p1[0]][p1[1]]==(p1[0], p1[1]): return p1
    return find(parents[p1[0]][p1[1]])

def firstUnion():
    d = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]!='X' and not visited[i][j]:
                d.append((i, j))
                visited[i][j]=True
                while d:
                    ti, tj = d.popleft()
                    if board[ti][tj]=='L': swan.append((ti, tj))
                    for k in range(4):
                        tti, ttj = ti+di[k], tj+dj[k]
                        if -1 < tti < N and -1 < ttj < M and not visited[tti][ttj]:
                            if board[tti][ttj]=='X':
                                ice.append((tti, ttj))
                            else:
                                d.append((tti, ttj))
                                parents[tti][ttj]=(i, j)
                            visited[tti][ttj]=True                                
                            
def checkSwan():
    if find(swan[0])==find(swan[1]):
        return True
    else:
        return False

def iceBreak():
    s = set()
    for i, j in ice:
        board[i][j]='.'
        for k in range(4):
            ti, tj = i+di[k], j+dj[k]
            if -1 < ti < N and -1 < tj < M:
                if board[ti][tj]=='X': s.add((ti, tj))
                else: union((ti, tj), (i,j))
    ice.clear()
    for i, j in s: ice.append((i,j))

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
parents = [[(i, j) for j in range(M)] for i in range(N)]
swan = []
day=0
ice=[]

firstUnion()
while True:
    if checkSwan():
        print(day)
        break
    iceBreak()
    day+=1


### 코드리뷰 ###
# 나는 bfs하다가 포기 유니온 파인드로 풀었고, 이건 bfs, 내꺼랑 이거 둘 다 pypy만 통과함, 그래도 이게 압도적으로 빠르긴 하네
'''
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)] # wc가 visited인데 나는 왜 bfs로 풀 때 visited를 매 번 초기화 시켰을까,,

a, swan = [], []
# 왜 필요 없는 것까지 데크로 하나 했는데 덱으로 바꿔주려고 그랬구나
# 리스트로 만들어서 데크로 변환하는 코드로 해봤는데 많이 느려짐, 이게 정석이네
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque() 

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1]) # 가능하면 튜플로~
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1 # swan 저장해두고 .으로 바꿔두는 것 좋다. 나는 !='X'로 구현했는데 그럴 필요 없을 듯
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1

'''

### 코드리뷰 이후 코드 ###
# 속도는 더 느리네
'''
import sys
input = sys.stdin.readline
from collections import deque

def waterBfs():
    tmpWater = deque()
    while water:
        i, j = water.popleft()
        for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if -1 < di < N and -1 < dj < M and not visited[di][dj]:
                if board[di][dj]=='X': tmpWater.append((di,dj))
                else: water.append((di, dj))
                visited[di][dj]=True
    for i, j in tmpWater: board[i][j]='.'
    return tmpWater

def swanBfs():
    tmpSwan = deque()
    while swanD:
        i, j = swanD.popleft()
        if (i, j) == swan[1]:
            exit(print(day))
        for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if -1 < di < N and -1 < dj < M and not swanVisited[di][dj]:
                if board[di][dj]=='X': tmpSwan.append((di,dj))
                else: swanD.append((di, dj))
                swanVisited[di][dj]=True
    return tmpSwan

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
water, swanD = deque(), deque()
visited, swanVisited = [[False for _ in range(M)] for _ in range(N)], [[False for _ in range(M)] for _ in range(N)]
swan = []

for i in range(N):
    for j in range(M):
        if board[i][j]!='X':
            water.append((i,j))
            visited[i][j]=False
            if board[i][j]=='L':
                swan.append((i,j))
                board[i][j]='.'
swanD.append(swan[0])
swanVisited[swan[0][0]][swan[0][1]]=True
day=0
while True:
    swanD = swanBfs()
    water = waterBfs()
    day+=1
'''