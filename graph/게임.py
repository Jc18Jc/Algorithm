import sys
input=sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
edge = [[[] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] != 'H':
            num=int(board[i][j])
            for ni, nj in (i+num, j), (i-num, j), (i, j+num), (i, j-num):
                if -1 < ni < N and -1 < nj < M and board[ni][nj] != 'H':
                    edge[i][j].append((ni, nj))

distance = [[-1 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0]=True

for k in range(N*M-1):
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                for ni, nj in edge[i][j]:
                    visited[ni][nj]=True
                    if distance[ni][nj] > distance[i][j]-1:
                        distance[ni][nj] = distance[i][j]-1
                        if k==N*M-1: exit(print(-1))
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            for ni, nj in edge[i][j]:
                if distance[ni][nj] > distance[i][j]-1:
                    exit(print(-1))

print(-min(map(min, distance)))


### 코드리뷰 ###
# 정공법은 dp, 나는 직관대로 밸만 포드 사용, 시간이 많이 아슬아슬함, dp 사용시 50~300 나는 7500 ..
'''
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if visited[x][y] : # 루프 검사
        sys.stdout.write('-1')
        sys.exit()
    # 다른 루트에서 방문한 적이 있는 경우 리턴하는데 이번 루트가 더 길 수도 있는거 아닌가 ?
    # 그게 아니고 dp[x][y]는 해당 좌표에서 최대로 갈 수 있는 길이를 저장해둔거라 그냥 리턴하면 되네, 루트로 갈 수록 커지는 구조라 가능한 듯
    if dp[x][y] != 0 : 
        return dp[x][y]
    dp[x][y] = 1
    move = int(X[x][y])
    for dx, dy in [(move, 0), (0, move), (0, -move) , (-move, 0)] :
        nx, ny = x + dx, y + dy
        if (0 <= nx < N) and (0 <= ny < M) :
            if X[nx][ny] != 'H' :
                visited[x][y] = True
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 시작 노드로 갈수록 커지는 구조구나
                visited[x][y] = False
    return dp[x][y]

N, M = map(int, sys.stdin.readline().split())
X = []
for _ in range(N):
    temp = sys.stdin.readline()
    X.append(temp[:-1])

visited = [[False for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

dfs(0, 0)

sys.stdout.write(str(dp[0][0]))
'''