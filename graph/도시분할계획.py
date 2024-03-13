import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(num):
    if parents[num]==num:
        return num
    return find(parents[num])

def union(num1, num2):
    p1, p2 = find(num1), find(num2)
    if p1 != p2:
        if p1 < p2:
            parents[p2]=p1
        else:
            parents[p1]=p2
        return True
    return False
    
N, M = map(int, input().split())

cost = [list(map(int, input().split())) for _ in range(M)]
cost.sort(key=lambda x: x[2], reverse=True)
parents=[i for i in range(N+1)]

answer=0
count=0

while count != N-2:
    a, b, c = cost.pop()
    if union(a, b):
        count+=1
        answer+=c

print(answer)

### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n: 
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a) 
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

N, M = map(int, input().split())

edges = []
parent = list(range(N + 1)) # 이런 리스트 생성 방법도 있구나, 응용할만 한 듯
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

answer = 0
last_edge = 0
for a, b, c in edges: # union한 간선 개수 생각해서 브레이크 걸어주면 for문도 덜 돌고 last-edge 생각할 필요 없을 듯
    if find(a) != find(b):
        union(a, b)
        answer += c
        last_edge = c
print(answer - last_edge)
'''