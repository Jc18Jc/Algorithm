import sys
ssr = sys.stdin.readline
from queue import PriorityQueue

n, m, x = map(int, ssr().split())
x-=1
w = [[] for _ in range(n)]

for _ in range(m):
    a, b, c=  map(int, ssr().split())
    w[a-1].append([b-1, c])

cost = [0 for _ in range(n)]

for i in range(n):
    if i==x:
        continue
    p = PriorityQueue()
    cost2=[0 for _ in range(n)]
    for item in w[i]:
        p.put([item[1], item[0]])
    while p.qsize():
        v = p.get()
        if cost2[v[1]]:
            continue
        cost2[v[1]]=v[0]
        if v[1]==x:
            break
        for item in w[v[1]]:
            if not cost2[item[0]]:
                p.put([item[1]+v[0], item[0]])
    cost[i]=cost2[x]

p2 = PriorityQueue()
cost3 = [0 for _ in range(n)]
for item in w[x]:
    p2.put([item[1], item[0]])

while p2.qsize():
    v=p2.get()
    if cost3[v[1]] or v[1]==x:
        continue
    cost3[v[1]]=v[0]
    for item in w[v[1]]:
        if not cost3[item[0]]:
            p2.put([item[1]+v[0], item[0]])

for i in range(n):
    cost[i]+=cost3[i]

print(max(cost))