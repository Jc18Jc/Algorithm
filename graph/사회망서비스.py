import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
edge = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
dp = [[0,1] for _ in range(N+1)] # 0은 자기가 얼이어답터가 아닐 때, 1은 자기가 얼리어답터일 때
visited=[False for _ in range(N+1)]

def dnc(num):
    visited[num]=True
    for node in edge[num]:
        if not visited[node]:
            dnc(node)
            dp[num][0]+=dp[node][1]
            dp[num][1]+=min(dp[node][0], dp[node][1])

dnc(1)
print(min(dp[1][0], dp[1][1]))

### 코드리뷰 ###
'''
import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
c = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int , sys.stdin.readline().split(" "))
    c[a].append(b)
    c[b].append(a)

visited = [0 for i in range(n+1)]
def dfs(start):
    global c
    global visited
    visited[start] = 1
    if len(c[start]) == 0: # ▽ 그러면 이런 if문도 필요 없음, 이거말고는 다 똑같네
        dp[start][1] = 1 # 이렇게 1이 필요하면 선언할 때부터 하면 되지
        dp[start][0] = 0
    else:
        for i in c[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0] , dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0],dp[1][1]))
'''