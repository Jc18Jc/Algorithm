import sys
ssr = sys.stdin.readline

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

n = int(ssr())

line = [None for _ in range(n)]

for i in range(n):
    x1, y1, x2, y2, w = map(int, ssr().split())
    line[i]=(w, ((y1,x1),(y2,x2)))

line.sort()
answer = 0

for i in range(n):
    count=1
    for j in range(i+1, n):
        if intersect(line[i][1], line[j][1]):
            count+=1
    answer+=count*line[i][0]
print(answer)