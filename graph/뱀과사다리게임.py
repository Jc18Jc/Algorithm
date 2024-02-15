from collections import deque
n1, n2 = map(int, input().split())
board = [-1 for _ in range(101)]
for _ in range(n1+n2):
    x, y = map(int, input().split())
    board[x]=y
visited=[False for _ in range(101)]
q=deque()
q.append((1, 0))
while q:
    v=q.popleft()
    if v[0]>93:
        print(v[1]+1)
        break
    for i in range(1,7):
        num = v[0]+i
        if board[num] != -1:
            num=board[num]
        if not visited[num]:
            q.append((num, v[1]+1))
            visited[num]=True


### 코드리뷰 ###
'''
from collections import deque
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
board = [0] * 101
visited = [False] * 101
 
ladder = dict() # 보드도 선언하고 래더도 선언했네 ??
for _ in range(n):
    i,j = map(int,input().split())
    ladder[i] = j

snack = dict() # 어짜피 사다리랑 안겹쳐서 한 번에 받아도 되긴하겠지만, 가독성 향상 목적 ?
for _ in range(m):
    i,j = map(int,input().split())
    snack[i] = j
 
def bfs(start):
    q = deque()
    q.append(start)
 
    visited[start] = True # 방문 체크 큐에 넣을 시점에 해주는게 속도 면에서 더 나을 듯
 
    while q:
        cur = q.popleft()
 
        for i in range(1, 7): # 주사위 1 ~ 6
            next = cur + i
 
            if 0 < next <= 100 and not visited[next]:
                if next in ladder:
                    next = ladder[next] # 사다리를 두 번 타는 경우는 어떻게 해결하는거지 ?, 이게 문제가 풀린다고 ?
                                        # 추측컨데, 한 칸에 사다리가 최대 한 개라는 것이 사다리의 끝과 시작도 공존할 수 없다는 말인 듯
                                        # 나도 while로 했다가 if로 수정.
                
                if next in snack:
                    next = snack[next]
                
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[cur] + 1
 
bfs(1) # 1부터 시작
print(board[100]) # 종료 조건 없이 가능한 모든 노드를 다 방문하고 종료한 다음에 100에 저장된 코스트를 출력하는구나, 별로

'''