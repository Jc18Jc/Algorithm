from collections import deque
S=int(input())

visited=[[False for _ in range(1001)] for _ in range(1001)]
d=deque()
d.append((1, 0, 0))

while d:
    n, p, c=d.popleft()
    if n==S:
        print(c)
        break
    if n+p < 1001 and not visited[n+p][p]:
        d.append((n+p,p, c+1))
        visited[n+p][p]=True
    if not visited[n][n]:
        d.append((n, n, c+1))
        visited[n][n]=True
    if n-1 > -1 and not visited[n-1][p]:
        d.append((n-1, p, c+1))
        visited[n-1][p]=True

### 코드리뷰 ###
'''
from collections import deque
n = int(input())
# n+1로 가능한가 ?? 500만들 때 502에서 2 뺄 수도 있을텐데,, 답은 같네 왜지
# 소름,, 500을 안넘기고 뺄 횟수의 반만큼 빼주고 곱2하면 같거나 작을 수밖에 없음, 홀수일 때는 잘 모르겠네
dist = [[-1]* (n+1) for _ in range(n+1)] 

q = deque()
q.append((1,0))
dist[1][0] = 0
while q: # 원리는 같은데 while에 break 거는걸 안해서 모든 dist를 채울 때까지 진행하고, 정답을 찾는 for문도 필요
    s,c = q.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer)
'''