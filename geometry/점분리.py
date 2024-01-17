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

tc = int(ssr())

for _ in range(tc):
    n, m = map(int, ssr().split())
    black = [() for _ in range(n)]
    white = [() for _ in range(n)]
    for i in range(n):
        x, y = map(int, ssr().split())
        black[i]=(y, x)
    for j in range(m):
        x, y = map(int, ssr().split())
        white[i]=(y, x)

    blackCon = [None for _ in range(n)]
    lb = 1
    if n <= 2:
        lb=n-1
        blackCon[0] = (black[0])
        if n == 2:
            blackCon[1] = (black[1])
    else:
        theta = [0 for _ in range(n)]

        mindex=black.index(min(black))
        po1 = (black[mindex][0], black[mindex][1])
        theta[0] = (-1, po1[0], po1[1])

        j=1
        for i in range(0, n):
            if i == mindex:
                continue
            po2 = (black[i][0], black[i][1])
            t=calTheta(po1, po2)
            theta[j]=(t, po2[0], po2[1])
            j+=1

        theta.sort()

        blackCon[0] = ((theta[0][1], theta[0][2]))
        blackCon[1] = ((theta[1][1], theta[1][2]))

        for i in range(2, n):
            po3=(theta[i][1], theta[i][2])
            tmp = ccw(blackCon[lb-1],blackCon[lb], po3)
            while tmp==-1 or tmp == 0:
                lb-=1
                if tmp==0: break
                tmp = ccw(blackCon[lb-1],blackCon[lb], po3)
            lb+=1
            blackCon[lb] = (po3)

        if ccw(blackCon[lb-1],blackCon[lb], blackCon[0])==2:
            lb-=1

    whiteCon = [None for _ in range(n)]
    lw = 1
    if n <= 2:
        lw=n-1
        whiteCon[0] = (white[0])
        if n == 2:
            whiteCon[1] = (white[1])
    else:
        theta = [0 for _ in range(m)]

        mindex=white.index(min(white))
        po1 = (white[mindex][0], white[mindex][1])
        theta[0] = (-1, po1[0], po1[1])

        j=1

        for i in range(0, m):
            if i == mindex:
                continue
            po2 = (white[i][0], white[i][1])
            t=calTheta(po1, po2)
            theta[j]=(t, po2[0], po2[1])
            j+=1

        theta.sort()

        whiteCon = [None for _ in range(n)]
        whiteCon[0] = ((theta[0][1], theta[0][2]))
        whiteCon[1] = ((theta[1][1], theta[1][2]))

        for i in range(2, n):
            po3=(theta[i][1], theta[i][2])
            tmp = ccw(whiteCon[lw-1],whiteCon[lw], po3)
            while tmp==-1 or tmp == 0:
                lw-=1
                if tmp==0: break
                tmp = ccw(whiteCon[lw-1],whiteCon[lw], po3)
            lw+=1
            whiteCon[lw] = (po3)

        if ccw(whiteCon[lw-1],whiteCon[lw], whiteCon[0])==2:
            lw-=1
    flag = True
    rflag = True
    lflag = True
    if n > 1:
        for i in range(n):
            l1 = (blackCon[i], blackCon[(i+1)%n]) 
            for j in range(m):
                cc = ccw(l1[0], l1[1], whiteCon[j])
                if  cc==1:
                    rflag=False
                elif cc==-1:
                    lflag=False
                if m > 1:
                    l2 = (whiteCon[i], whiteCon[(j+1)%m])
                    if intersect(l1, l2):
                        print('NO')
                        flag=False
                        break
            if not flag:
                break
    elif m > 1:
        for i in range(m):
            cc = ccw(whiteCon[i], whiteCon[(i+1)%n], blackCon[0])
            if  cc==1:
                rflag=False
            elif cc==-1:
                lflag=False
    
    if flag and (lflag or rflag):
        print('NO')
    elif flag:
        print('YES')
    