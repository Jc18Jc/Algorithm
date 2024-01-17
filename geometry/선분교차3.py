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

x1, y1, x2, y2 = map(int, ssr().split())
if x1 > x2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1
x3, y3, x4, y4 = map(int, ssr().split())
if x3 > x4:
    x3, x4 = x4, x3
    y3, y4 = y4, y3

l1 = ((x1, y1), (x2, y2))
l2 = ((x3, y3), (x4, y4))

if intersect(l1, l2):
    print(1)
    if x1==x2 and x3!=x4:
        m2 = (y4-y3)/(x4-x3)
        print(x1, m2*x1-m2*x3+y3)
    elif x3==x4 and x1!=x2:
        m1 = (y2-y1)/(x2-x1)
        print(x3, m1*x3-m1*x1+y1)
    elif x1==x2 and x3==x4:
        ty1, ty2 = y1, y2
        if y1 > y2:
            ty1, ty2 = y2, y1
        ty3, ty4 = y3, y4
        if y3 > y4:
            ty3, ty4 = y4, y3
        if ty2 == ty3:
            print(x1, ty2)
        elif ty4 == ty1:
            print(x1, ty4)
    else:
        m1 = (y2-y1)/(x2-x1)
        m2 = (y4-y3)/(x4-x3)
        if m1 == m2:
            if y3-m2*x3==y1-m1*x1 and (x3 <= x2 <= x4 or x1 <= x4 <= x2):
                if x2 == x3:
                    print(x3, y3)
                elif x4==x1:
                    print(x1, y1)
        else:
            x = (m2*x3-m1*x1+y1-y3)/(m2-m1)
            y = m2*(x-x3)+y3
            print(x, y)
else:
    print(0)