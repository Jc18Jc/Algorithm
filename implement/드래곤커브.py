N = int(input())
dragon = [list(map(int, input().split())) for _ in range(N)]
board = [[False for _ in range(101)] for _ in range(101)]

dir=[(0,1),(-1,0),(0,-1),(1,0)]

def curve():
    sx, sy = pointList[-1]
    for i in range(len(pointList)-2, -1, -1):
        dx, dy = pointList[i]
        pointList.append((sx+(dy-sy), sy+(sx-dx)))

def checkDragon(x, y):
    if board[x+1][y] and board[x+1][y+1] and board[x][y+1] and board[x][y]:
        return True
    return False

for y, x, d, g in dragon:
    pointList = [(x, y), (x+dir[d][0], y+dir[d][1])]
    for _ in range(g):
        curve()
    for tx, ty in pointList:
        board[tx][ty]=True

answer=0
for i in range(100):
    for j in range(100):
        if checkDragon(i, j):
            answer+=1
print(answer)


### 코드리뷰 ###
'''
n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    y, x, d, g = map(int, input().split(' '))
    graph[x][y] = 1
    curve = [d]
    for j in range(g): # 좌표가 아닌 각 좌표의 커브 방향으로 접근했네, 이해는 힘들지만 괜찮은 방법인 듯
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101: # 조건때문에 필요는 없을 듯
            continue
        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)
'''