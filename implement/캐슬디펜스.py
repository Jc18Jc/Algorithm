# 그래프, 브루트포스, 시뮬
import sys
input = sys.stdin.readline
from collections import deque

def findEnemy(turn):
    s=set()
    for archer in archerList:
        visited = [[False for _ in range(M)]for _ in range(N)]
        d.append((N-1-turn, archer, 1))
        visited[N-1-turn][archer] = True
        while d:
            i, j, c = d.popleft()
            if board[i][j]==1:
                s.add((i,j))
                break
            for ti, tj in (i, j-1), (i-1, j), (i, j+1):
                if c < D and -1 < ti < N and -1 < tj  < M and not visited[ti][tj]:
                    visited[ti][tj]=True
                    d.append((ti, tj, c+1))
        d.clear()  
    return s

def addArcher(num, index):
    result = -1
    if num != 0: archerList.append(index)
    if num == 3 and index < M:
        pValue = progress()
        archerList.pop()
        return pValue
    if index >= M-1:
        return -1
    for i in range(index+1, M-2+num):
        result = max(addArcher(num+1, i),result)
    if num != 0: archerList.pop()
    return result
        
def progress():
    removeEnermy = []
    for i in range(N):
        s=findEnemy(i)
        for ti, tj in s:
            board[ti][tj]=0
            removeEnermy.append((ti, tj))
    l=len(removeEnermy)
    for i, j in removeEnermy:
        board[i][j]=1
    return l
        
N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
archerList = []
d = deque()
print(addArcher(0, -1))


### 코드리뷰 ###
# 완전 탐색이 꽤 많이 들어가서 비효율적인 부분이 보임, 속도 안정권이긴 한데 내꺼보다 많이 느리고 배열 크기 커졌으면 위험할 듯
'''
import sys
import copy

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]] # yield 리턴과 비슷한데, 배열 같은 것을 반환하는 대신 하나씩 반환해줌, 여기선 굳이 쓸 필요 없었겠지만 나중에 유용할 수도
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next

def attack(list_):
    attack_list = list()
    cnt = 0
    for l in list_:
        pos = list()
        # 적 찾을 때 굳이 bfs 안돌리고 완전탐색으로 했구나 크기가 많이 크지 않아서 괜찮을 듯..이 아니고
        # 가능한거 다 추가한 다음에 정렬하는 과정까지 있어야 자기랑 가까운거 찾겠네,, 차라리 bfs
        # 각 궁수마다 완전탐색 + 정렬을 해야하는 것임
        for i in range(n): 
            for j in range(m):
                if temp[i][j] == 1:
                    now_d = abs(i - n) + abs(j - l)
                    if d >= now_d:
                        pos.append((now_d, i, j))
        pos.sort(key=(lambda x: (x[0], x[2])))
        if pos:
            attack_list.append(pos[0])
    for a in attack_list:
        _, i, j = a
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1
    return cnt

def move():
    for i in range(-1, -n, -1): # 이건 뭐지 ㅋㅋ n-1부터 -1까지 하면 안되나, 신박하네
        temp[i] = temp[i - 1]
    temp[0] = [0 for _ in range(m)]
# 매 턴마다 또 완전 탐색 ?? 적이 얼마없을 땐 괜찮겠지만 최악의 경우엔 비효율적일 듯, 없어도 되는 코드라 생각
# 실제로 이것만 빼고 메인에 while만 수정해서 제출해봤는데 50ms정도 줄었음, 그닥 큰 차이는 없구나
def is_empty(): 
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True

n, m, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
items = [i for i in range(m)]
result = 0

for a in combinations(items, 3):
    temp = copy.deepcopy(graph)
    count = 0
    while not is_empty():
        count += attack(a)
        move()
    result = max(result, count)
print(result)
'''