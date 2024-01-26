import sys
ssr = sys.stdin.readline

n, m, k = map(int, ssr().split())

board=[[0 for _ in range(m)]for _ in range(n)]

def move(i, j, s, d):
    
    if d == 1:
        if i-s < 0:
            s-=i
            distance = s%(n-1)
            if s//(n-1) % 2 == 1:
                i = (n-1)-distance
            else:
                d=2
                i=distance
        else:
            i -= s
    elif d == 2:
        if i+s > n-1:
            s = s - n + 1 + i
            distance = s%(n-1)
            if s//(n-1) % 2 == 1:
                i = distance
            else:
                d=1
                i=(n-1)-distance
        else:
            i += s
    if d == 4:
        if j-s < 0:
            s-=j
            distance = s%(m-1)
            if s//(m-1) % 2 == 1:
                j = (m-1)-distance
            else:
                d=3
                j=distance
        else:
            j -= s
    elif d == 3:
        if j+s > m-1:
            s = s - m + 1 + j
            distance = s%(m-1)
            if s//(m-1) % 2 == 1:
                j = distance
            else:
                d=4
                j=(m-1)-distance
        else:
            j += s
    return (i, j, d)
for _ in range(k):
    i, j, s, d, z = map(int, ssr().split())
    board[i-1][j-1] = [s,d,z]

answer=0
for j in range(m):
    for i in range(n):
        if board[i][j] != 0:
            answer+=board[i][j][2]
            board[i][j]=0
            break
    board2=[[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                shark=board[i][j]
                result = move(i, j, shark[0], shark[1])
                if board2[result[0]][result[1]] != 0:
                    if shark[2] > board2[result[0]][result[1]][2]:
                        board2[result[0]][result[1]] = [shark[0], result[2], shark[2]]
                else:
                    board2[result[0]][result[1]] = [shark[0], result[2], shark[2]]
    board=board2
            
print(answer)    
