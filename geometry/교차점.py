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
    xleft, ybottom, xright, ytop = map(int, ssr().split())
    xstart, ystart, xend, yend = map(int, ssr().split())
    p = [(xleft, ybottom), (xleft, ytop), (xright, ybottom), (xright,ytop)]
    l = [(xstart, ystart), (xend, yend)]
    l.sort()
    l2 = [(p[0], p[1]), (p[0], p[2]), (p[1], p[3]), (p[2], p[3])]

    dx = l[1][0]-l[0][0]
    dy = l[1][1]-l[0][1]

    if dx == 0:
        if l[0][0] == xleft:
            if intersect(l, l2[0]):
                if l[0][1]==ytop or l[1][1]==ybottom:
                    print(1)
                    continue
                print(4)
                continue
            print(0)
            continue
        elif l[0][0] == xright:
            if intersect(l, l2[3]):
                if l[0][1]==ytop or l[1][1]==ybottom:
                    print(1)
                    continue
                print(4)
                continue
            print(0)
            continue
        else:
            count=0
            if intersect(l, l2[1]):
                count+=1
            if intersect(l, l2[2]):
                count+=1
            print(count)
            continue
    if dy == 0:
        if l[0][1] == ybottom:
            if intersect(l, l2[1]):
                if l[0][0]==xright or l[1][0]==xleft:
                    print(1)
                    continue
                print(4)
                continue
            print(0)
            continue
        elif l[0][1] == ytop:
            if intersect(l, l2[2]):
                if l[0][0]==xright or l[1][0]==xleft:
                    print(1)
                    continue
                print(4)
                continue
            print(0)
            continue
        else:
            count=0
            if intersect(l, l2[0]):
                count+=1
            if intersect(l, l2[3]):
                count+=1
            print(count)
            continue
    lis = []
    x1 = l[0][0]
    y1 = l[0][1]
    if intersect(l, l2[0]):
        lis.append((dy*xleft, dy*(xleft-x1)+y1*dx))
    if intersect(l, l2[1]):
        tmp = (dx*(ybottom-y1)+x1*dy, ybottom*dx)
        if tmp not in lis:
            lis.append(tmp)
    if intersect(l, l2[2]):
        tmp = (dx*(ytop-y1)+x1*dy, ytop*dx)
        if tmp not in lis:
            lis.append(tmp)
    if intersect(l, l2[3]):
        tmp = (dy*xright, dy*(xright-x1)+y1*dx)
        if tmp not in lis:
            lis.append(tmp)
    print(len(lis))