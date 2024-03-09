import sys
input = sys.stdin.readline
from collections import deque

delta = ((1, -1, 0, 0), (0, 0, 1, -1))
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
answer = 0
visited = [[False for _ in range(M)] for _ in range(N)]
d=deque()
cheese = []

def searchCheese(i, j):
    d.append((i, j))
    while d:
        v=d.popleft()
        for k in range(4):
            ti, tj = v[0]+delta[0][k], v[1]+delta[1][k]
            if -1 < ti < N and -1 < tj < M and not visited[ti][tj]:
                if board[ti][tj]:
                    cheese.append((ti, tj))
                else:
                    d.append((ti, tj))
                visited[ti][tj]=True

def meltCheese():
    l = len(cheese)
    tmp = cheese.copy()
    cheese.clear()
    for i, j in tmp:
        searchCheese(i, j)
    return l
        
searchCheese(0,0)

while True:
    if not cheese:
        print(time)
        print(answer)
        break
    answer = meltCheese()
    time+=1


### 코드리뷰 ###
'''
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0:
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1:
                    melt.append((nx, ny))
                    
    for x, y in melt:
        cheeze[x][y] = 0
    return len(melt)

n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i]) # 전체 치즈를 계산하고 빼는 식으로 했구나, 굳이 안해도 될 듯 meltCnt로 충분히 알 수 있는 정보
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)] # 매 타임마다 visited를 새로 만들고 있는데, 굳이 안해도 됨, 녹는 부분에서부터 bfs해도 무방
    meltCnt = bfs() # 대신 매 타임 visited 이용하면 이해는 쉬움, 0,0 넣고 bfs 돌리면 알 수 있기 때문
    cnt -= meltCnt
    if cnt == 0:
        print(time, meltCnt, sep='\n')
        break
    time += 1
'''