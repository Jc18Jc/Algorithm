import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

def convert(a):
    return int(a)-1

N, M, E = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(convert, input().split())
customer = [list(map(convert, input().split())) for _ in range(M)]
d=deque()

def initial():
    k=0
    for i, j, _, _ in customer:
        board[i][j]=k+2
        k+=1

def findDestination(index):
    si, sj, ei, ej = customer[index]
    visited = [[False for _ in range(N)] for _ in range(N)]
    d.append((si, sj, 0))
    visited[si][sj]=True
    while d:
        i, j, c = d.popleft()
        if (i, j) == (ei, ej):
            d.clear()
            return c
        for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if -1 < di < N and -1 < dj < N and not visited[di][dj] and board[di][dj] != 1:
                d.append((di, dj, c+1))
                visited[di][dj]=True
    return 10**10

def findCustomer():
    global ti, tj, E
    h=[(0, ti, tj)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[ti][tj]=True
    while h:
        c, i, j = heappop(h)
        if c > E:
            exit(print(-1))
        if board[i][j]>1:
            num = board[i][j]-2
            demand=findDestination(num)
            E=E-c-demand
            if E < 0:
                exit(print(-1)) 
            board[i][j]=0
            E+=demand*2
            ti, tj = customer[num][2], customer[num][3]
            return
        for di, dj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
            if -1 < di < N and -1 < dj < N and not visited[di][dj] and board[di][dj] != 1:
                heappush(h, (c+1, di, dj))
                visited[di][dj]=True
    exit(print(-1))

initial()
for _ in range(M):
    findCustomer()
print(E)

### 코드리뷰 ###
'''
from collections import deque
def findPassenger(taxi):
    q = deque()
    q.append(taxi)
    visited = [[0] * N for _ in range(N)]
    minDistance = float('inf')
    candidate = []
    while q:
        y, x = q.popleft()
        if visited[y][x] > minDistance:
            break
        if [y, x] in passenger_start: # 가장 우선순위가 높은 시작점을 찾는 의도 같은데, 모든 노드 방문마다 승객 정보를 꺼내서 비교하는 것도 비효율적이고 알아보기 힘든 듯
            minDistance = visited[y][x]
            candidate.append([y, x])
        else:
            for d in range(4):
                ny, nx = y + dirs[d][0], x + dirs[d][1] # 이건 괜찮은 듯 ? 배열 선언 한 줄에 되는구나, 2*4 말고 4*2면 더 좋을 듯
                if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
    if candidate:
       candidate.sort()
       return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    else:
       return -1, -1, -1


def goDestination(start, end): 
    q = deque()
    q.append(start)
    visited = [[0] * N for _ in range(N)]
    while q:
        y, x = q.popleft()
        if [y, x] == end:
            break
        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
    return visited[y][x], y, x # 목적지로 못가서 이상한 값 반환할 수도 있지 않나 ?

N, M, fuel = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
taxi = [ty - 1, tx - 1]

passenger_start = []
passenger_end = []
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    passenger_start.append([sy - 1, sx - 1])
    passenger_end.append([ey - 1, ex - 1])
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for _ in range(M):
    distance, py, px = findPassenger(taxi)
    if distance == -1 or fuel - distance < 0:  
        fuel = -1
        break
    fuel -= distance
    idx = passenger_start.index([py, px]) # 인덱스로 조사하면 나쁜 점이 이렇게 index로 찾아서 바꿔주던가 아예 remove or pop 해야해서, 맵에 표시했으면 지우면 땡인데
    passenger_start[idx] = [-1, -1]
    distance2, py2, px2 = goDestination([py, px], passenger_end[idx])
    if [py2, px2] != passenger_end[idx] or fuel - distance2 < 0:
        fuel = -1
        break
    fuel += distance2
    taxi = [py2, px2]

print(fuel)

'''