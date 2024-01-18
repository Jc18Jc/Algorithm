import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, c = map(int, ssr().split())

array = []
for _ in range(n):
    array.append(int(ssr()))
array.sort()

low = 1
high = array[-1]-array[0]
answer = 0
while low <= high:
    mid = (low+high)//2
    count=1
    i = 1
    lasti = 0
    while count < c and i < n:
        if array[i]-array[lasti] >= mid:
            lasti=i
            count+=1
        i+=1
    if count==c:
        answer=mid
        low=mid+1
    else:
        high=mid-1
print(answer)
    