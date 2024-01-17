import sys
ssr = sys.stdin.readline

n, s = map(int, ssr().split())

array = list(map(int, ssr().split()))

start=0
end=0
total = 0
count = n+1

while True:
    if end==n:
        while start < n and total-array[start] >= s:
            total-=array[start]
            start += 1
        if total >= s:
            count = count if count < end-start else end-start
        break
    if total + array[end] >= s:
        total+=array[end]
        end+=1
        while total-array[start] >= s:
            total-=array[start]
            start += 1
        count = count if count < end-start else end-start
    else:
        total+=array[end]
        end+=1

if count == n+1:
    print(0)
else:
    print(count)