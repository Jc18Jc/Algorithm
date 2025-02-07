import sys
ssr = sys.stdin.readline
from bisect import bisect_left

n = int(ssr())

array=list(map(int, ssr().split()))

an=[]

index=-1

for i in range(0, n):
    t = bisect_left(an, array[i])
    if index < t:
        an.append(array[i])
        index+=1
    else:
        an[t]=array[i]
print(len(an))
