import sys
ssr = sys.stdin.readline

def calTheta(p1, p2):
    dx = p2[1]-p1[1]
    ax = abs(dx)
    dy = p2[0]-p1[0]
    ay = abs(dy)
    if ax+ay == 0:
        return 0
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
    
n=int(ssr())

point = [None for _ in range(n)]
mindex=0
for i in range(n):
    x, y = map(int, ssr().split())
    point[i] = (y, x)
    mindex = mindex if point[mindex] < point[i] else i

if n == 2:
    exit(print((((point[1][0]-point[0][0])**2 + (point[1][1]-point[0][1])**2))))

theta = [0 for _ in range(n)]

po1 = (point[mindex][0], point[mindex][1])
theta[0] = (-1, po1[0], po1[1])

j=1
for i in range(0, n):
    if i == mindex:
        continue
    po2 = (point[i][0], point[i][1])
    t=calTheta(po1, po2)
    theta[j]=(t, po2[0], po2[1])
    j+=1


theta.sort()

turn = [None for _ in range(n)]
turn[0] = ((theta[0][1], theta[0][2]))
turn[1] = ((theta[1][1], theta[1][2]))

m = 1
for i in range(2, n):
    po3=(theta[i][1], theta[i][2])
    tmp = ccw(turn[m-1],turn[m], po3)
    while tmp==-1 or tmp == 0:
        m-=1
        if tmp==0: break
        tmp = ccw(turn[m-1],turn[m], po3)
    m+=1
    turn[m] = po3
    

if ccw(turn[m-1],turn[m], turn[0])==-1:
    m-=1

i=0
j=1
distance = 0
while True:
    a=turn[i]
    b=turn[(i+1)%(m+1)]
    c=turn[j]
    d=turn[(j+1)%(m+1)]
    
    tmp = (c[0]-a[0])**2 + (c[1]-a[1])**2
    distance = distance if distance > tmp else tmp
    cc = ccw(a, b, (d[0]+b[0]-c[0] , d[1]+b[1]-c[1]))
    if cc==1:
        j=(j+1)%(m+1)
    else:
        i=(i+1)%(m+1)
        if i==0:
            break

print(distance)
        