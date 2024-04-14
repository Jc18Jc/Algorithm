import itertools
import copy

N, M, K =map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
O = list(list(map(int, input().split())) for _ in range(K))

def rotate(orderList):
    B=copy.deepcopy(A)
    for r, c, s in orderList:
        r, c = r-1, c-1
        for k in range(1, s+1):
            a, b = B[r-k+1][c-k], B[r+k-1][c+k]
            for t in range(1, k*2):
                B[r-k+t][c-k]=B[r-k+t+1][c-k]
                B[r+k-t][c+k]=B[r+k-t-1][c+k]
            B[r-k][c-k:c+k+1]=[a]+B[r-k][c-k:c+k]
            B[r+k][c-k:c+k+1]=B[r+k][c-k+1:c+k+1]+[b]
    m=10000
    for t in range(N):
        m=m if m < sum(B[t]) else sum(B[t])
    return m

def permutation():
    answer=10000
    for l in list(itertools.permutations(O, K)):
        tmp=rotate(l)
        answer = answer if answer < tmp else tmp
    print(answer)

permutation()


### 코드리뷰 ###
'''
from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(cnt): # 나도 처음에는 dfs로 경우의 수 구하려고 했는데 그냥 순열 함수 한 번이면 되는거라..
    global min_ans
    if cnt == k:
        q2 = deepcopy(q) # 아아 돌리는 순서를 pop으로 확인하니까 이것도 deep copy 했구나
        min_ans = min(min_ans, rotate(q2))
        return
    for i in range(k):
        if select[i]:
            continue
        select[i] = 1
        q.append(f[i])
        dfs(cnt+1)
        select[i] = 0
        q.pop()


def rotate(q):
    a2 = deepcopy(a)
    while q:
        x, y, z = q.popleft()
        lx, ly, rx, ry = x-z, y-z, x+z, y+z
        while True:
            if lx >= rx or ly >= ry:
                break
            dir = 0
            x, y, before = lx, ly, a2[lx][ly]
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if not lx <= nx <= rx or not ly <= ny <= ry: # 방향 정해서 하는 것도 괜찮은데 코드가 너무 길어진다
                    dir += 1
                    continue
                temp = a2[nx][ny]
                a2[nx][ny] = before
                before = temp
                x, y = nx, ny
                if [x, y] == [lx, ly]:
                    lx += 1; ly += 1; rx -= 1; ry -= 1
                    break

    ans = sys.maxsize
    for row in a2:
        ans = min(ans, sum(row))
    return ans


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

f = []
for _ in range(k):
    r, c, s = map(int, input().split())
    f.append([r-1, c-1, s])

select = [0 for _ in range(k)]
q = deque()
min_ans = sys.maxsize
dfs(0)
print(min_ans)


'''