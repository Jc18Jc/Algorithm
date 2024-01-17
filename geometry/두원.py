# 해결 못함,,


import sys
ssr = sys.stdin.readline
pi=3.141592

def calTheta(p1, p2):
    dx = p2[0]-p1[0]
    ax = abs(dx)
    dy = p2[1]-p1[1]
    ay = abs(dy)
    if ax+ay == 0:
        return 0
    t = dy/(ax + ay)
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    return t * 90

x1, y1, r1, x2, y2, r2 = map(float, ssr().split())

if r1 < r2:
    x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

if r1+r2 <= d:
    print(0)

elif r1 >= d+r2:
    print(r2*r2*pi)
else:
    x=(r1**2-r2**2+d**2)/(2*d)
    y=(r1**2-x**2)**(1/2)
    theta1 = calTheta((0,0), (x, y))*2
    print(theta1)

    ho1 = pi*r1*r1*theta1/360
    tri1 = y*(r1-x)

    theta2 = (180-calTheta((d, 0), (x,y)))*2
    print(theta2)
    ho2 = pi*r2*r2*theta2/360

    if theta2==180:
        print(ho1-tri1+ho2)
    tri2 = y*abs(x-d)

    if theta2 > 180:
        print(ho1, tri1, ho2, tri2)
        print(ho1-tri1+ho2+tri2)
    elif theta2 < 180:
        print(ho1-tri1+ho2-tri2)



        