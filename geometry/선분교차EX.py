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

n = int(ssr())
line = [() for _ in range(n)]
for i in range(n):
    x1, y1, x2, y2 = map(int, ssr().split())
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    line[i]=((x1, y1), (x2, y2))

answer = [[3 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):

        l1 = line[i]
        l2 = line[j]

        if intersect(l1, l2):
            if l1[0][0]==l1[1][0] and l2[0][0]!=l2[1][0]:
                dx2 = l2[1][0]-l2[0][0]
                dy2 = l2[1][1]-l2[0][1]
                y=dy2*(l1[0][0]-l2[0][0])+dx2*l2[0][1]
                if (l2[0][1]*dx2==y and l2[0][0]==l1[0][0]) or (l2[1][1]*dx2==y and l2[1][0]==l1[0][0]) or l1[0][1]*dx2==y or l1[1][1]*dx2==y:
                    answer[i][j], answer[j][i] = 1, 1
                else:
                    answer[i][j], answer[j][i] = 2, 2
            elif l1[0][0]!=l1[1][0] and l2[0][0]==l2[1][0]:
                dx1 = l1[1][0]-l1[0][0]
                dy1 = l1[1][1]-l1[0][1]
                y=dy1*(l2[0][0]-l1[0][0])+dx1*l1[0][1]
                if (l1[0][1]*dx1==y and l1[0][0]==l2[0][0]) or (l1[1][1]*dx1==y and l1[1][0]==l2[0][0]) or l2[0][1]*dx1==y or l2[1][1]*dx1==y:
                    answer[i][j], answer[j][i] = 1, 1
                else:
                    answer[i][j], answer[j][i] = 2, 2
            elif l1[0][0]==l1[1][0] and l2[0][0]==l2[1][0]:
                ty1, ty2 = l1[0][1], l1[1][1]
                if ty1 > ty2:
                    ty1, ty2 = ty2, ty1
                ty3, ty4 = l2[0][1], l2[1][1]
                if ty3 > ty4:
                    ty3, ty4 = ty4, ty3
                if ty2 == ty3:
                    answer[i][j], answer[j][i] = 1, 1
                elif ty4 == ty1:
                    answer[i][j], answer[j][i] = 1, 1
                else:
                    pass
            else:
                dx1 = l1[1][0]-l1[0][0]
                dy1 = l1[1][1]-l1[0][1]
                dx2 = l2[1][0]-l2[0][0]
                dy2 = l2[1][1]-l2[0][1]
                if dy2*dx1 == dy1*dx2:
                    tx1, tx2 = l1[0][0], l1[1][0]
                    if tx1 > tx2:
                        tx1, tx2 = tx2, tx1
                    tx3, tx4 = l2[0][0], l2[1][0]
                    if tx3 > tx4:
                        tx3, tx4 = tx4, tx3
                    if tx2 == tx3:
                        answer[i][j], answer[j][i] = 1, 1
                    elif tx4 == tx1:
                        answer[i][j], answer[j][i] = 1, 1
                    else:
                        pass
                else:
                    x = dy1*dx2*l1[0][0] - dy2*dx1*l2[0][0]+dx1*dx2*(l2[0][1]-l1[0][1])
                    tmp = dy1*dx2-dx1*dy2
                    if x == l1[0][0]*tmp or x == l1[1][0]*tmp or x == l2[0][0]*tmp or x == l2[1][0]*tmp:
                        answer[i][j], answer[j][i] = 1, 1
                    else:
                        answer[i][j], answer[j][i] = 2, 2
        else:
            answer[i][j], answer[j][i] = 0, 0

for item in answer:
    for item2 in item:
        print(item2, end='')
    print()
