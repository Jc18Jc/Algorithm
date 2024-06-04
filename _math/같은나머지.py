import sys
from math import gcd

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

num.sort()

minus = []

for i in range(n - 1):
    minus.append(num[i + 1] - num[i])
    
print(gcd(*minus))