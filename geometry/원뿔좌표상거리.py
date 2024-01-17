import sys
import math
ssr = sys.stdin.readline

def customRound(n):
    multiplier = 10**2
    return math.floor(n * multiplier + 0.5) / multiplier

def distance(r, h, d1, a1, d2, a2):
    d=(r**2+h**2)**(1/2)
    rate = d1/d
    r1=r*rate
    x = abs(a2-a1)
    if x > 180:
        x=360-x
    x = r1*x/d1
    answer = (d1**2+d2**2-2*d1*d2*math.cos(math.pi*(x/180)))**(1/2)
    print("{:.2f}".format(customRound(answer)))


while True:
    try:
        r, h, d1, a1, d2, a2 = map(float, ssr().split())
        if d1==0 and d2==0:
            print("{:.2f}".format(0.00))
            continue    
        if d1 < d2:
            d1, a1, d2, a2 = d2, a2, d1, a1
        distance(r, h, d1, a1, d2, a2)
    except:
        break