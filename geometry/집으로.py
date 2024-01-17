import sys
ssr = sys.stdin.readline

x, y, d, t = map(int, ssr().split())

distance = (x**2 + y**2)**(1/2)

if t >= d:
    exit(print(distance))

time = 0
flag = False

while distance - d>= 0:
    distance-=d
    time+=t
    flag=True

addT=0

if flag:
    addT = min(t, t+d-distance, distance)
else:
    addT = min(2*t, t+d-distance, distance)

time += addT

print(time)

