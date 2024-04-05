from collections import deque
board = [list(input()) for _ in range(12)]

def bfs():
    visited = [[False for _ in range(6)] for _ in range(12)]
    d = deque()
    l=[]
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.' and not visited[i][j]:
                s=board[i][j]
                d.append((i,j))
                visited[i][j]=True
                tmp=[(i,j)]
                while d:
                    ti, tj = d.popleft()
                    for ni, nj in (ti+1, tj),(ti-1, tj),(ti, tj+1),(ti, tj-1):
                        if -1 < ni < 12 and -1 < nj < 6 and board[ni][nj]==s and not visited[ni][nj]:
                            visited[ni][nj]=True
                            tmp.append((ni,nj))
                            d.append((ni,nj))
                if len(tmp) > 3:
                    l.append(tmp)
    return l

def changeBoard(l):
    for item in l:
        for i, j in item:
            board[i][j]='.'
   
def downPuyo():
    for i in range(10, -1, -1):
        for j in range(6):
            if board[i][j]!='.':
                ti = i+1
                while ti < 12 and board[ti][j]=='.':
                    ti+=1
                ti-=1
                board[ti][j], board[i][j]=board[i][j], board[ti][j]

answer = 0
while True:
    l=bfs()
    if l:
        answer+=1
        changeBoard(l)
        downPuyo()
    else:
        break
print(answer)


### 코드리뷰 ###
'''
import sys
from collections import deque
input = sys.stdin.readline

data = [list(input().rstrip()) for _ in range(12)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1): # 내 방법보다 더 좋네
                if data[j][i] != "." and data[k][i] == ".": 
                    data[k][i] = data[j][i]
                    data[j][i] = "."
                    break
                           
def bfs(x,y):
    q = deque()
    q.append((x,y))
    temp.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < 12 and 0<= ny < 6 and data[nx][ny] == data[x][y] and visited[nx][ny] == 0:
                q.append((nx,ny))
                temp.append((nx,ny))
                visited[nx][ny] = 1

def delete(temp):
    for a,b in temp:
        data[a][b] = "."

# def show(data):
#     for i in range(12):
#         print(data[i],end="\n")

ans = 0
while 1:
    flag = 0
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if data[i][j] != '.' and visited[i][j] == 0: 
                visited[i][j] = 1
                temp = []
                bfs(i,j)
                # 4칸확인
                if len(temp) >= 4:
                    flag = 1
                    delete(temp) # 나는 당연히 다 찾고 터뜨릴 생각했는데, 내리지만 않으면 사실 상관없구나
    if flag == 0:
        break
    down()
    ans += 1

print(ans)

'''