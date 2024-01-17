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

t = int(ssr())

for _ in range(t):
    tmp = list(map(int, ssr().split()))
    n = tmp[0]
    points=[]
    for i in range(1, n+1):
        points.append((tmp[i*2], tmp[i*2-1], i-1))
    points.sort()
    thetas = [(-1, points[0][0], points[0][1], points[0][2])]
    p1 = (points[0][0], points[0][1])
    for i in range(1, n):
        p2 = (points[i][0], points[i][1])
        theta = calTheta(p1, p2)
        thetas.append((theta, points[i][0], points[i][1], points[i][2]))
    thetas.sort()
    lastTheta = thetas[n-1][0]
    for i in range(n):
        if thetas[i][0]==lastTheta:
            j=n-1
            while i < j:
                thetas[i], thetas[j] = thetas[j], thetas[i]
                i+=1
                j-=1
            break
    for item in thetas:
        print(item[3], end=' ')
    print()