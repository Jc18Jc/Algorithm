def checkRect(num, x, y):
    for i in range(x,x+num):
        for j in range(y,y+num):
            if not board[i][j]:
                return False
    return True

def putRect(num, x, y):
    for i in range(x, x+num):
        for j in range(y, y+num):
            board[i][j]=0

def takeRect(num, x, y):
    for i in range(x, x+num):
        for j in range(y, y+num):
            board[i][j]=1

def bf(count, uses, i, j):
    c=100
    while j < 10:
        i=0
        while i < 10:
            if board[i][j]:
                for k in range(1, 6):
                    if uses[k]==5:
                        continue
                    if i+k > 10 or j+k > 10 or not checkRect(k, i, j):
                        break
                    uses[k]+=1
                    putRect(k, i, j)
                    c=min(c,bf(count+1, uses, i+1, j))
                    uses[k]-=1
                    takeRect(k, i, j)
                return c
            i+=1
        j+=1
    return count

board=[list(map(int, input().split())) for _ in range(10)]
result=bf(0, [0]*6, 0, 0)
print(result if result != 100 else -1)

### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

def func(x, y, cnt): # 인덱스 옮길 때마다 재귀를 해주네
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    if x >= 10:
        func(0, y+1, cnt)
        return
    if a[x][y] == 1:
        for k in range(5):
            # 여기 문제는 색종이 2번이 불가능하면 345도 불가능한데 그걸 체크 안해준다는 것과 12345 전부 실패했을 때 불가능 리턴 안해주는 것
            # 이상한 답이 나오는건 아니지만 시간 손해클 듯, 실제로 나랑 전체 로직은 같은데 1900 1400으로 500차이남
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue
            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0
                paper[k] += 1
                func(x + k + 1, y, cnt + 1)
                paper[k] -= 1
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1
    else:
        func(x + 1, y, cnt)

a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
func(0, 0, 0)
print(ans) if ans != sys.maxsize else print(-1)
'''
