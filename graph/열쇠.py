import sys
input = sys.stdin.readline
from collections import deque
delta = ((1, -1, 0, 0), (0, 0, 1, -1))

def check(i, j):
    global visited, d, answer, keyList, keep
    c=board[i][j]
    visited[i][j]=True
    if c=='.' or c in keyList or c =='$':
        d.append((i,j))
        if c =='$':
            answer+=1
    elif c=='*':
        pass
    elif 97 <= ord(c) <= 122:
        keyList.append(board[i][j].upper())
        d.append((i,j))
        for cc, ti, tj in keep:
            if keyList[-1]==cc:
                d.append((ti,tj))
    else:
        keep.append((c, i, j))

def init():
    for i in range(M):
        check(0, i), check(N-1, i)
    for i in range(1, N-1):
        check(i, 0), check(i, M-1)

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
    init()
    while d:
        i, j=d.popleft()
        for k in range(4):
            ni, nj = i+delta[0][k], j+delta[1][k]
            if -1 < ni < N and -1 < nj < M and not visited[ni][nj]:
                check(ni, nj)

    print(answer)