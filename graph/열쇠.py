import sys
input = sys.stdin.readline
from collections import deque
delta = ((1, -1, 0, 0), (0, 0, 1, -1))

def check(i, j):
    global answer
    global keep
    global keyList
    c=board[i][j]
    if c=='.':
        return 1
    if c in keyList:
        return 2
    if c =='$':
        answer+=1
        return 3
    if c=='*':
        return 4
    if 97 <= ord(c) <= 122:
        keyList.append(board[i][j].upper())
        return 5
    keep.append((c, i, j))
    return 6

def init():
    tmp = []
    for i in range(M):
        c1, c2 = check(0, i), check(N-1, i)
        if c1 <= 3:
            tmp.append((0,i))
        if c2 <= 3:
            tmp.append((N-1, i))
    for i in range(1, N-1):
        c1, c2 = check(i, 0), check(i, M-1)
        if c1 <= 3:
            tmp.append((i,0))
        if c2 <= 3:
            tmp.append((i, M-1))
    return tmp

for _ in range(int(input())):
    N, M = map(int, input().split())
    board = list(list(input().strip()) for _ in range(N))
    keyList = list(input().strip())
    for i in range(len(keyList)):
        keyList[i]=keyList[i].upper()
    d=deque()
    visited=[[False for _ in range(M)] for _ in range(N)]
    keep=[]
    answer=0
    for item in init():
        d.append(item)
        visited[item[0]][item[1]] = True
    
    while d:
        i, j=d.popleft()
        for k in range(4):
            ni, nj = i+delta[0][k], j+delta[1][k]
            if -1 < ni < N and -1 < nj < M and not visited[ni][nj]:
                c=check(ni, nj)
                if c<=3 or c==5:
                    d.append((ni,nj))
                    visited[ni][nj]=True
                    if c==5:
                        for cc, ti, tj in keep:
                            if keyList[-1]==cc:
                                d.append((ti,tj))
                                visited[ti][tj]=True
    print(answer)