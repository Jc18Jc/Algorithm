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

n  = int(ssr())
robot = [None for _ in range(n)]
avoid = [None for _ in range(n)]
for i in range(n):
    x, y = map(int, ssr().split())
    robot[i] = (y, x)
for i in range(n):
    x, y = map(int, ssr().split())
    avoid[i] = (y, x)

def combi(index, restList, preList):
    if index == n:
        for item in preList:
            print(item+1)
        return True
    for i in range(len(restList)):
        l1 = (robot[index],avoid[restList[i]])
        flag=True
        result=False
        for j in range(index):
            l2 = (robot[j], avoid[preList[j]])
            if intersect(l1, l2):
                flag=False
                break
        if flag:
            result = combi(index+1, restList[0:i]+restList[i+1:len(restList)], preList+[restList[i]])
        if result:
            return True

combi(0, [i for i in range(n)], [])
            
