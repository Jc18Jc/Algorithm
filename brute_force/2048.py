import sys
ssr = sys.stdin.readline

n = int(ssr())
board = []
maxValue = 0
for _ in range(n):
    l=list(map(int, ssr().split()))
    maxValue = max(maxValue, max(l))
    board.append(l)

def dfs(num, method, board2):

    board3 = [[board2[i][j] for i in range(n)] for j in range(n)]
    if method==1:
        for i in range(n):
            k=0
            j=0
            last=0
            while j < n:
                if board3[i][j]==0:
                    j+=1
                    continue
                tmp = board3[i][j]
                board3[i][j]=0
                j+=1
                if last == tmp:
                    board3[i][k]=tmp*2
                    k+=1
                    last=0
                else:
                    if last==0:
                        board3[i][k]=tmp
                    else:
                        board3[i][k+1]=tmp
                        k+=1
                    last=tmp

    elif method==2:
        for i in range(n):
            k=n-1
            j=n-1
            last=0
            while j > -1:
                if board3[i][j]==0:
                    j-=1
                    continue
                tmp = board3[i][j]
                board3[i][j]=0
                j-=1
                if last == tmp:
                    board3[i][k]=tmp*2
                    k-=1
                    last=0
                    continue
                else:
                    if last==0:
                        board3[i][k]=tmp
                    else:
                        board3[i][k-1]=tmp
                        k-=1
                    last=tmp
                    continue
    elif method==3:
        for i in range(n):
            k=0
            j=0
            last=0
            while j < n:
                if board3[j][i]==0:
                    j+=1
                    continue
                tmp = board3[j][i]
                board3[j][i]=0
                j+=1
                if last == tmp:
                    board3[k][i]=tmp*2
                    k+=1
                    last=0
                    continue
                else:
                    if last==0:
                        board3[k][i]=tmp
                    else:
                        board3[k+1][i]=tmp
                        k+=1
                    last=tmp
                    continue
    elif method==4:
        for i in range(n):
            k=n-1
            j=n-1
            last=0
            while j > -1:
                if board3[j][i]==0:
                    j-=1
                    continue
                tmp = board3[j][i]
                board3[j][i]=0
                j-=1
                if last == tmp:
                    board3[k][i]=tmp*2
                    k-=1
                    last=0
                else:
                    if last==0:
                        board3[k][i]=tmp
                    else:
                        board3[k-1][i]=tmp
                        k-=1
                    last=tmp
    if num == 4:
        tmpMax = 0
        for item in board3:
            tmpMax = max(tmpMax, max(item))
        return tmpMax
    r1 = dfs(num+1, 1, board3)
    r2 = dfs(num+1, 2, board3)
    r3 = dfs(num+1, 3, board3)
    r4 = dfs(num+1, 4, board3)
    return max(r1, r2, r3, r4)

print(max(dfs(0, 1, board), dfs(0, 2, board), dfs(0, 3, board), dfs(0, 4, board)))
        
