import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

board=[]
cctv = []
zero = 0
for i in range(n):
    l = list(map(int, ssr().split()))
    for j in range(m):
        if l[j] == 0:
            zero += 1
        elif l[j] != 6:
            cctv.append((i, j))
    board.append(l)


def white(i, j, methodList, cnt, index):
    whiteList = []
    count=0
    for method in methodList:
        if method == 1:
            for k in range(j+1, m):
                if board[i][k] == 6:
                    break
                if board[i][k] == 0:
                    whiteList.append((i, k))
                    count+=1
                    board[i][k]=7
        elif method == 2:
            for k in range(j-1, -1, -1):
                if board[i][k] == 6:
                    break
                if board[i][k] == 0:
                    whiteList.append((i, k))
                    count+=1
                    board[i][k]=7
        elif method == 3:
            for k in range(i+1, n):
                if board[k][j] == 6:
                    break
                if board[k][j] == 0:
                    whiteList.append((k, j))
                    count+=1
                    board[k][j]=7
            
        elif method == 4:
            for k in range(i-1, -1, -1):
                if board[k][j] == 6:
                    break
                if board[k][j] == 0:
                    whiteList.append((k, j))
                    count+=1
                    board[k][j]=7
    result = dfs(index+1, count+cnt)
    for i2, j2 in whiteList:
        board[i2][j2]=0
    return result

def dfs(index, cnt):
    if index == len(cctv):
        return cnt
    i = cctv[index][0]
    j = cctv[index][1]
    c = board[i][j]
    if c == 1:
        result = max(white(i,j,[1],cnt,index), white(i,j,[2],cnt,index), white(i,j,[3],cnt,index), white(i,j,[4],cnt,index))
    elif c == 2:
        result = max(white(i,j,[1,2],cnt,index), white(i,j,[3,4],cnt,index))
    elif c == 3:
        result = max(white(i,j,[1,3],cnt,index), white(i,j,[1,4],cnt,index),white(i,j,[2,3],cnt,index), white(i,j,[2,4],cnt,index))
    elif c == 4:
        result = max(white(i,j,[1,2,3],cnt,index), white(i,j,[1,3,4],cnt,index), white(i,j,[1,2,4],cnt,index), white(i,j,[2,3,4],cnt,index))
    else:
        result = white(i,j,[1,2,3,4],cnt,index)
    return result

print(zero-dfs(0, 0))