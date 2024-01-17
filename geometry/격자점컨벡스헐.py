import sys
ssr = sys.stdin.readline

def calTheta(p1, p2):
    dx = p2[1]-p1[1]
    ax = abs(dx)
    dy = p2[0]-p1[0]
    ay = abs(dy)
    t = dy/(ax + ay)
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    return t * 90

def ccw(p0, p1, p2):
    v1x = p1[1]-p0[1]   
    v1y = p1[0]-p0[0]
    v2x = p2[1]-p1[1]
    v2y = p2[0]-p1[0]
    c = v1x*v2y - v1y*v2x
    if c > 0:
        return 1
    elif c < 0:
        return -1
    else:   
        return 0

p = int(ssr())

for _ in range(p):

    n=int(ssr())

    point = [None for _ in range(n)]

    n2=n
    j=0
    while n2 > 0:
        l = list(ssr().strip().split())
        for i in range(len(l)//2):
            point[j]=(int(l[2*i+1]), int(l[2*i]))
            j+=1
        n2-=5
    point.sort(key=lambda x: (-x[0], x[1]))

    theta = [0 for _ in range(n)]


    po1 = (point[0][0], point[0][1])
    theta[0] = (361, po1[0], po1[1])

    for i in range(1, n):
        po2 = (point[i][0], point[i][1])
        t=calTheta(po1, po2)
        t = 360 if t==0 else t
        theta[i]=(t, po2[0], po2[1])

    theta.sort(key=lambda x: (-x[0], -x[1], x[2]))

    turn = [None for _ in range(n)]
    turn[0] = ((theta[0][1], theta[0][2]))
    turn[1] = ((theta[1][1], theta[1][2]))

    m = 1

    for i in range(2, n):
        po3=(theta[i][1], theta[i][2])
        tmp = ccw(turn[m-1],turn[m], po3)
        while tmp==1 or tmp == 0:
            m-=1
            if tmp==0: break
            tmp = ccw(turn[m-1],turn[m], po3)
        m+=1
        turn[m] = (po3)

    if m > 1:
        tmp = ccw(turn[m-1],turn[m], turn[0])
        if tmp==0 or tmp==1:
            m-=1

    print(m+1)
    for i in range(m+1):
        print(turn[i][1], turn[i][0])