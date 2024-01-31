import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

array = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, ssr().split())
    tmp = array[i:j+1]
    tmp.reverse()
    array[i:j+1] = tmp
    
array = array[1:]
print(*array)