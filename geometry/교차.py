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

t = int(ssr())

for _ in range(t):
    xstart, ystart, xend, yend, xleft, ytop, xright, ybottom = map(int, ssr().split())
    if xleft > xright:
        xleft, xright = xright, xleft
    if ybottom > ytop:
        ybottom, ytop = ytop, ybottom
    p = [(xleft, ytop), (xright, ytop), (xleft, ybottom), (xright,ybottom)]
    l = ((xstart, ystart), (xend, yend))
    if intersect(l, (p[0], p[1])):
        print('T')
        continue 
    if intersect(l, (p[0], p[2])):
        print('T')
        continue 
    if intersect(l, (p[1], p[3])):
        print('T')
        continue 
    if intersect(l, (p[2], p[3])):
        print('T')
        continue
    if xleft<xstart<xright and ybottom < ystart < ytop and xleft<xend<xright and ybottom < yend < ytop:
        print('T')
        continue
    print('F')