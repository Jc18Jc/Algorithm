import sys
ssr = sys.stdin.readline
from collections import deque

n, m  = map(int, ssr().split())

def ccw(p0, p1, p2):
    dx1 = p1[0]-p0[0]
    dy1 = p1[1]-p0[1]
    dx2 = p2[0]-p0[0]
    dy2 = p2[1]-p0[1]
    if dx1*dy2 > dy1*dx2:
        return 1
    if dx1*dy2 < dy1*dx2:
        return -1
    if dx1==0 and dy1==0:
        return 0
    if dx1*dx2 < 0 or dy1*dy2 < 0:
        return -1
    if dx1**2+dy1**2 < dx2**2+dy2**2:
        return 1
    return 0
    
def intersect(l1, l2):
    t1 = ccw(l1[0], l1[1], l2[0])*ccw(l1[0], l1[1], l2[1])
    t2 = ccw(l2[0], l2[1], l1[0])*ccw(l2[0], l2[1], l1[1])
    return t1<=0 and t2<=0

k = int(ssr())
can = [[] for _ in range(k+1)]
bus = [() for _ in range(k+1)]
for i in range(k):
    num, x1, y1, x2, y2 = map(int, ssr().split())
    bus[num]=((x1, y1), (x2, y2))

x1, y1, x2, y2 = map(int, ssr().split())
spoint = (x1, y1)
epoint = (x2, y2)

q = deque()
end = []
visited = [True for _ in range(k+1)]

for i in range(1, k+1):
    l=bus[i]
    dx = l[0][0]-l[1][0]
    if dx == 0:
        tmpy2 = max(l[0][1], l[1][1])
        tmpy1 = min(l[0][1], l[1][1])
        if spoint[0] == l[0][0]:
            if tmpy1 <= spoint[1] <=tmpy2:
                q.append((i,1))
                visited[i]=False
        if epoint[0] == l[0][0]:
            if tmpy1 <= epoint[1] <= tmpy2:
                end.append(i)
    else:
        tmpx2 = max(l[0][0], l[1][0])
        tmpx1 = min(l[0][0], l[1][0])
        if spoint[1] == l[0][1]:
            if tmpx1 <= spoint[0] <=tmpx2:
                q.append((i, 1))
                visited[i]=False
        if epoint[1] == l[0][1]:
            if tmpx1 <= epoint[0] <= tmpx2:
                end.append(i)
    for j in range(i+1, k+1):
        if intersect(l, bus[j]):
            can[i].append(j)
            can[j].append(i)

while q:
    v = q.popleft()
    if v[0] in end:
        print(v[1])
        break
    for item in can[v[0]]:
        if visited[item]:
            q.append((item, v[1]+1))
            visited[item]=False