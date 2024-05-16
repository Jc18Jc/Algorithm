import sys
N=int(input())
array = [None for _ in range(N)]
for i in range(N):
    a, b, c, d = map(int,sys.stdin.readline().split())
    n = a*100+b
    m = c*100+d
    array[i]=[n, m]
array.sort(key=lambda x:x[1])

answer=0
start = 1131
while start > 301:
    tmp = 10000
    while True:
        if array:
            if array[-1][1] >= start:
                if array[-1][0] < start:
                    tmp = min(array[-1][0], tmp)
                array.pop()
            else:
                break
        else:
            break
    if tmp==10000:
        exit(print(0))
    start=tmp
    answer+=1
print(answer)