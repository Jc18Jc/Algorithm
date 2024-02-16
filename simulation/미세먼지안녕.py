import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
windDir = [[], []]

for i in range(N):
    if board[i][0]==-1:
        for k in range(1, M):
            windDir[0].append((i, k))
            windDir[1].append((i+1, k))
        for k in range(i-1, -1, -1):
            windDir[0].append((k ,M-1))
        for k in range(i+2, N):
            windDir[1].append((k, M-1))
        for k in range(M-2, -1, -1):
            windDir[0].append((0, k))
            windDir[1].append((N-1, k))
        for k in range(0, i):
            windDir[0].append((k, 0))
        for k in range(N-1, i+1, -1):
            windDir[1].append((k, 0))
        break

def spread():
    board2 = [[0 for _ in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                tmp = board[i][j]//5
                for ii, jj in (i+1,j), (i-1, j), (i, j+1), (i, j-1):
                    if -1 < ii < N and -1 < jj < M and board[ii][jj] != -1:
                        board2[ii][jj]+=tmp
                        board2[i][j]-=tmp
    for i in range(N):
        for j in range(M):
            board[i][j]+=board2[i][j]

def wind():
    for k in range(len(windDir[0])-1, 0, -1):
        i = windDir[0][k][0]
        j = windDir[0][k][1]
        ni = windDir[0][k-1][0]
        nj = windDir[0][k-1][1]
        board[i][j]=board[ni][nj]
    board[windDir[0][0][0]][windDir[0][0][1]]=0
    for k in range(len(windDir[1])-1, 0, -1):
        i = windDir[1][k][0]
        j = windDir[1][k][1]
        ni = windDir[1][k-1][0]
        nj = windDir[1][k-1][1]
        board[i][j]=board[ni][nj]
    board[windDir[1][0][0]][windDir[1][0][1]]=0

for _ in range(T):
    spread() 
    wind()

answer= 0 
for i in range(N):
    for j in range(M):
        answer+=board[i][j]
print(answer+2)


### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1: # > 0이면 됨
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]

def air_up(): # 아이디어는 괜찮네, 순환마다 if문이 많아서 이 방법으로 처음에 dir 배열을 만들어주면 더욱 좋을 듯
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0: # 차라리 마지막에 +2
            answer += arr[i][j]

print(answer)

'''