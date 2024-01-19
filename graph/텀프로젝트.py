import sys
ssr = sys.stdin.readline

t = int(ssr())
for _ in range(t):
    n = int(ssr())
    array = list(map(int, ssr().split()))
    for i in range(n):
        array[i]-=1
    visited = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            l = [i]
            loc=i
            while not visited[array[i]]:
                l.append(array[i])
                i=array[i]
                visited[i]=True
            if array[i] in l:
                index = l.index(array[i])
                count+=index
            else:
                count+=len(l)
    print(count)