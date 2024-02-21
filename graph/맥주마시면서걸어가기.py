import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def incSearch(n, array):
    inc = [[] for _ in range(n+2)]
    for i in range(n+1):
        sx, sy = array[i][0], array[i][1]
        for j in range(i+1, n+2):
            ex, ey = array[j][0], array[j][1]
            if abs(ex-sx)+abs(ey-sy) <= 1000:
                inc[i].append(j)
                inc[j].append(i)
    return inc

def bfs(n, inc):
    q = deque()
    q.append(0)
    visited=[True] + [False for _ in range(n+1)]
    while q:
        v=q.popleft()
        if v==n+1:
            print('happy')
            return
        for item in inc[v]:
            if not visited[item]:
                q.append(item)
                visited[item]=True
    print('sad')

for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n+2):
        array.append(list(map(int, input().split())))
    bfs(n, incSearch(n, array))


### 코드리뷰 ###
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(): # incSearch 과정을 bfs할 때 직접 넣었구나 괜찮은 듯
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000: # 이 거리 비교 대신 q에 넣는 과정에서 i를 n+1까지 하고 i가 n일 때 happy 출력 좋을 듯 
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    # 여기에 if i==n: print('happy') return
                    q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    home = [int(x) for x in input().split()]
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    fest = [int(x) for x in input().split()]
    visited = [0 for i in range(n+1)] #home 제외
    bfs()

'''