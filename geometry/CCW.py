def ccw(p0, p1, p2):
    v1x = p1[1]-p0[1]
    v1y = p1[0]-p0[0]
    v2x = p2[1]-p1[1]
    v2y = p2[0]-p1[0]
    c = v1x*v2y - v1y*v2x
    if c > 0:
        return -1
    elif c<0:
        return 1
    else:
        return 0

p0 = list(map(int, input().split()))
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

print(ccw(p0, p1, p2))