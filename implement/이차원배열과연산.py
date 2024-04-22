from collections import defaultdict
r, c, k = map(int, input().split())
board = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    board[i][:3]=list(map(int, input().split()))
rl, cl = 3, 3
time = 0

def makeRArray():
    maxcl = 0
    for i in range(rl):
        d = defaultdict(int)
        for j in range(cl):
            if board[i][j]!=0:
                d[board[i][j]]+=1
                board[i][j]=0
        tmpArray = []
        for key, c in d.items():
            tmpArray.append([c, key])
        tmpArray.sort()
        t=0
        for c, n in tmpArray:
            if t >= 100:
                break
            board[i][t]=n
            board[i][t+1]=c
            t+=2
        maxcl = max(maxcl, t)
    return maxcl

def makeCArray():
    maxrl = 0
    for i in range(cl):
        d = defaultdict(int)
        for j in range(rl):
            if board[j][i]!=0:
                d[board[j][i]]+=1
                board[j][i]=0
        tmpArray = []
        for key, c in d.items():
            tmpArray.append([c, key])
        tmpArray.sort()
        t=0
        for c, n in tmpArray:
            if t >= 100:
                break
            board[t][i]=n
            board[t+1][i]=c
            t+=2
        maxrl = max(maxrl, t)
    return maxrl

while time <= 100:
    if rl >= r and cl >= c and board[r-1][c-1]==k:
        exit(print(time))
    if rl>=cl: cl=makeRArray()
    else: rl=makeCArray()
    time+=1
print(-1)

### 코드리뷰 ###
'''
import sys

r, c, k = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def calculate(matrix, dir):
    new_matrix, length = [], 0
    for row in matrix:
        num_cnt, new_row = [], []
        for num in set(row): # set으로 만들고 원소들 파악 후 그냥 count로 심플하게 괜찮네
            if num == 0: continue
            cnt = row.count(num)
            num_cnt.append((num, cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1], x[0]])
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_matrix.append(new_row)
        length = max(length, len(new_row))

    for row in new_matrix:
        row += [0] * (length - len(row))
        if len(row) > 100: row = row[:100]
    return list(zip(*new_matrix)) if dir == 'C' else new_matrix

time = 0
while True:
    if time > 100: time = -1; break
    if 0 <= r-1 < len(matrix) and 0 <= c-1 < len(matrix[0]) and matrix[r-1][c-1] == k: break
    if len(matrix) >= len(matrix[0]):
        matrix = calculate(matrix, 'R')
    else:
        matrix = calculate(list(zip(*matrix)), 'C')
    time += 1
print(time)

'''