N=int(input())
student=list(list(map(int, input().split())) for _ in range(N**2))
board=[[-1 for _ in range(N)]for _ in range(N)]
delta = ((-1, 1, 0, 0), (0, 0, 1, -1))
putList = []

for k in range(N**2):
    cur=(-1, -1)
    emptySpace = -1
    like = -1
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1:
                continue
            em = 0
            li = 0
            for t in range(4):
                di, dj = i+delta[0][t], j+delta[1][t]
                if -1 < di < N and -1 < dj < N:
                    if board[di][dj]==-1:
                        em+=1
                    elif board[di][dj] in student[k][1:]:
                        li+=1
            if like < li or (like==li and emptySpace < em):
                cur=(i, j)
                like=li
                emptySpace=em
    board[cur[0]][cur[1]] = student[k][0]
    putList.append(cur)

answer=0
for k in range(N**2):
    i, j = putList[k]
    like=0
    for t in range(4):
        di, dj = i+delta[0][t], j+delta[1][t]
        if -1 < di < N and -1 < dj < N:
            if board[di][dj] in student[k][1:]:
                like+=1
    if like!=0: answer+=10**(like-1)
print(answer)

### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n = int(input())
arr = [[0]*n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

for order in range(n**2):
    student = students[order]
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j]) # 각 자리별 요소를 다 넣어놓고 정렬해서 꺼냈구나, 코드는 간결해지고 시간은 좀 오를 듯
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]: # 와 students를 정렬하면 이렇게 쓸 수 있구나.. 이건 생각도 못했네
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)
'''