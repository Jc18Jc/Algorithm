import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    runway = [False for _ in range(N)]
    j=0
    flag=True
    while j < N-1:
        if board[i][j] > board[i][j+1]:
            for k in range(j+1, j+1+L):
                if k < N and board[i][k]==board[i][j]-1:
                    runway[k]=True
                else:
                    flag=False
                    break
            j+=L-1
        elif board[i][j] < board[i][j+1]:
            for k in range(j, j-L, -1):
                if k > -1 and board[i][k]==board[i][j+1]-1 and not runway[k]:
                    runway[k]=True
                else:
                    flag=False
                    break
        j+=1
    if flag:
        answer+=1

for j in range(N):
    runway = [False for _ in range(N)]
    i=0
    flag=True
    while i < N-1:
        if board[i][j] > board[i+1][j]:
            for k in range(i+1, i+1+L):
                if k < N and board[k][j]==board[i][j]-1:
                    runway[k]=True
                else:
                    flag=False
                    break
            i+=L-1
        elif board[i][j] < board[i+1][j]:
            for k in range(i, i-L, -1):
                if k > -1 and board[k][j]==board[i+1][j]-1 and not runway[k]:
                    runway[k]=True
                else:
                    flag=False
                    break
        i+=1
    if flag:
        answer+=1

print(answer)


### 코드리뷰 ###
'''
import sys

N, L = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def check(line, L): # 가로,세로를 못 나눠서 함수로 못 만들었는데 해당 줄을 1차원 배열로 주면 가능.. 좋네, L 파라미터로 넘겨주는 것만 빼면 좋을 듯
    visited = [False for _ in range(N)]
    for i in range(0, N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i]-line[i+1]) > 1:
            return False
        elif line[i] > line[i+1]:
            temp = line[i+1] # 굳이 temp 선언까지 해야할까
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        else:
            temp = line[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

answer = 0
for i in board:
    if check(i, L):
        answer += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(board[j][i])
    if check(temp, L):
        answer += 1

print(answer)

'''