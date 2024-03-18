import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
que = Queue()
fade = []  # 사라질 치즈 조각의 좌표가 담길 배열
hours = 0  # 녹는데 걸린 시간


# 전부 방문했는지 확인해주는 함수
def isVisit(visited):
    for v in visited:
        if False in v:
            return False
    return True


# 현재 치즈 좌표와 접촉한 외부 공기의 개수를 세주는 함수
def countOutsideAir(x, y):
    count = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 2:
            count += 1

    return count


# 외부 공기만 2로 표시하는 함수
def denoteOutsideAir():
    tmp_que = Queue()

    tmp_que.put([0, 0])
    tmp_visted = [[False for _ in range(m)] for _ in range(n)]

    while tmp_que.qsize() != 0:
        v = tmp_que.get()
        x = v[0]
        y = v[1]
        tmp_visted[x][y] = True

        if cheese[x][y] != 1:
            cheese[x][y] = 2

        if x > 0 and not tmp_visted[x - 1][y]:
            if cheese[x - 1][y] == 0 or cheese[x - 1][y] == 2:
                tmp_visted[x - 1][y] = True
                cheese[x - 1][y] = 2
                tmp_que.put([x - 1, y])
            elif cheese[x - 1][y] == 1:
                tmp_visted[x - 1][y] = True

        if x < n - 1 and not tmp_visted[x + 1][y]:
            if cheese[x + 1][y] == 0 or cheese[x + 1][y] == 2:
                tmp_visted[x + 1][y] = True
                cheese[x + 1][y] = 2
                tmp_que.put([x + 1, y])
            elif cheese[x + 1][y] == 1:
                tmp_visted[x + 1][y] = True

        if y > 0 and not tmp_visted[x][y - 1]:
            if cheese[x][y - 1] == 0 or cheese[x][y - 1] == 2:
                tmp_visted[x][y - 1] = True
                cheese[x][y - 1] = 2
                tmp_que.put([x, y - 1])
            elif cheese[x][y - 1] == 1:
                tmp_visted[x][y - 1] = True

        if y < m - 1 and not tmp_visted[x][y + 1]:
            if cheese[x][y + 1] == 0 or cheese[x][y + 1] == 2:
                tmp_visted[x][y + 1] = True
                cheese[x][y + 1] = 2
                tmp_que.put([x, y + 1])
            elif cheese[x][y + 1] == 1:
                tmp_visted[x][y + 1] = True


que.put([0, 0])

while True:
    fade = []
    denoteOutsideAir()

    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]
        visited[x][y] = True

        if x > 0 and not visited[x - 1][y]: # 방문하지 않았는데
            if cheese[x - 1][y] == 1 and countOutsideAir(x - 1, y) > 1: # 외부 공기와 2면 이상 맞닿은 치즈라면 
                fade.append([x - 1, y]) # 사라질 치즈에 추가
                visited[x - 1][y] = True
            elif cheese[x - 1][y] != 1: # 치즈가 아니라면 큐에 넣고 방문표시만 해줌
                que.put([x - 1, y])
                visited[x - 1][y] = True

        if x < n - 1 and not visited[x + 1][y]:
            if cheese[x + 1][y] == 1 and countOutsideAir(x + 1, y) > 1:
                fade.append([x + 1, y])
                visited[x + 1][y] = True
            elif cheese[x + 1][y] != 1:
                que.put([x + 1, y])
                visited[x + 1][y] = True

        if y > 0 and not visited[x][y - 1]:
            if cheese[x][y - 1] == 1 and countOutsideAir(x, y - 1) > 1:
                fade.append([x, y - 1])
                visited[x][y - 1] = True
            elif cheese[x][y - 1] != 1:
                que.put([x, y - 1])
                visited[x][y - 1] = True

        if y < m - 1 and not visited[x][y + 1]:
            if cheese[x][y + 1] == 1 and countOutsideAir(x, y + 1) > 1:
                fade.append([x, y + 1])
                visited[x][y + 1] = True
            elif cheese[x][y + 1] != 1:
                que.put([x, y + 1])
                visited[x][y + 1] = True

    # 사라질 치즈 조각이 있다면 해당 좌표를 2로 바꿔주고 시간을 1추가해줌
    if len(fade) != 0:
        for f in fade:
            que.put(f)
            cheese[f[0]][f[1]] = 2
        hours += 1

    # 사라지지 않은 치즈 조각의 방문을 해제해줌
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                visited[i][j] = False

    # 전부 방문했다면 탈출
    if isVisit(visited):
        exit(print(hours))