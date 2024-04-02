import sys
input = sys.stdin.readline
INF=10**10
N = int(input())
points = [[i]+list(map(int,input().split())) for i in range(N)]
dif = []
parents = [i for i in range(N)]
count=0
answer=0

def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)
    if p1 == p2: return False
    if p1 < p2: parents[p2]=p1
    else: parents[p1]=p2
    return True

def find(c):
    if parents[c]==c: return c
    return find(parents[c])

for k in range(1, 4):
    points.sort(key=lambda x: x[k])
    for j in range(N-1):
        dif.append((points[j+1][k]-points[j][k], points[j+1][0], points[j][0]))
dif.sort(reverse=True)

while count < N-1:
    v=dif.pop()
    if union(v[1], v[2]):
        answer+=v[0]
        count+=1
print(answer)


### 코드리뷰 ###
'''
import copy # 카피 안쓰잖아~

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

xlist, ylist, zlist = [], [], [] # 이렇게 저장하고 sort하면 시간이 덜 걸릴까? 똑같을까?
for i in range(n):
    x, y, z = map(int, input().split())
    xlist.append((x, i))
    ylist.append((y, i))
    zlist.append((z, i))

xlist.sort()
ylist.sort()
zlist.sort()

edges = []
for curList in xlist, ylist, zlist:
    for i in range(1, n):
        w1, a = curList[i-1]
        w2, b = curList[i]
        edges.append((abs(w1-w2), a, b)) # sort했으면 abs 쓸 필요 없죠
        
edges.sort()

parent = [i for i in range(n)]

def kruskal():
    result_cost = 0
    for cost, a, b  in edges:
        if find_parent(parent, a) != find_parent(parent, b): # 유니온에서도 find 쓰는데 굳이 여기서 find 써야할까? 안좋을 것 같음
            union_parent(parent, a, b)
            result_cost += cost

    print(result_cost)

kruskal()
'''