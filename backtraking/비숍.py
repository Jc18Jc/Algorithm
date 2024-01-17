import sys
ssr = sys.stdin.readline

n = int(ssr())

board = []

for _ in range(n):
    tmp = list(map(int, ssr().split()))
    board.append(tmp)

dia = [False for _ in range(2*n-1)]

def dfs(count, num):
    if num >= 2*n-1:
        return count
    if num < n:
        sx, sy = n-num-1, 0
    else:
        sx, sy = 0, num-n+1
    mc = dfs(count, num+2)
    while sx < n and sy < n:
        if board[sx][sy]:
            if not dia[sx+sy]:
                dia[sx+sy]=True
                result = dfs(count+1, num+2)
                dia[sx+sy]=False
                mc = mc if mc > result else result
        sx+=1
        sy+=1
    return mc

print(dfs(0, 0)+dfs(0, 1))