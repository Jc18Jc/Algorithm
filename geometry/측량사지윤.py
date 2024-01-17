import sys
ssr = sys.stdin.readline

def check(l1, l2, l3):
    a1, b1, c1, a2, b2, c2, a3, b3, c3 = l1[0], l1[1], l1[2], l2[0], l2[1], l2[2], l3[0], l3[1], l3[2]
    if a1*b2==a2*b1:
        print('0.0000')
        return
    if a2*b3==b2*a3:
        print('0.0000')
        return
    if a1*b3==a3*b1:
        print('0.0000')
        return
    x1 = (c2*b1-b2*c1)/(a1*b2-a2*b1)
    x2 = (c2*b3-b2*c3)/(a3*b2-a2*b3)
    x3 = (c3*b1-b3*c1)/(a1*b3-a3*b1)
    y1 = 0
    y2 = 0
    y3 = 0
    if b1 != 0:
        y1 = (-c1-a1*x1)/b1
        y3 = (-c1-a1*x3)/b1
    else:
        y1 = (-c2-a2*x1)/b2
        y3 = (-c3-a1*x3)/b3
    if b2 != 0:
        y2 = (-c2-a2*x2)/b2
    else:
        y2 = (-c3-a3*x2)/b3
    answer = abs((x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/2)
    print('{:.4f}'.format(answer))
    


t = int(ssr())

for _ in range(t):
    line = []
    for _ in range(3):
        a, b, c = map(int, ssr().split())
        line.append((a,b,c))
    check(line[0], line[1], line[2])