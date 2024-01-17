import sys
ssr = sys.stdin.readline

def calIncli(p1, p2):
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    if dx == 0:
        return 100000000
    return dy/dx

def ccw(p0, p1, p2):
    v1x = p1[0]-p0[0]   
    v1y = p1[1]-p0[1]
    v2x = p2[0]-p1[0]
    v2y = p2[1]-p1[1]
    c = v1x*v2y - v1y*v2x
    if c > 0:
        return 1
    elif c < 0:
        return -1
    else:   
        return 0


n=int(ssr())

point = []
n2=0
for _ in range(n):
    x, y, c = ssr().strip().split()
    if c=='N':
        continue
    point.append((int(x), int(y)))
    n2+=1
n=n2

theta = []

po1 = min(point)

theta.append((-1000000000, po1[0], po1[1]))

for i in range(n):
    if point[i]==po1:
        continue
    po2 = (point[i][0], point[i][1])
    t=calIncli(po1, po2)
    theta.append((t, po2[0], po2[1]))

theta.sort()
last = theta[n-1][0]

print(n)
for i in range(n):
    if theta[i][0]==last:
        for j in range(n-1, i-1, -1):
            print(theta[j][1], theta[j][2])
        break
    print(theta[i][1], theta[i][2])
